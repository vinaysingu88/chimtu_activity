from django.shortcuts import redirect, render
products_list=[
    {'id':1 , 'name':'pant','cost':100},
    {'id':2 , 'name':'pant1','cost':110},
    {'id':3 , 'name':'pant2','cost':120},
    {'id':4 , 'name':'shirt','cost':200}
]

# Create your views here.
def home(req):
    if req.method=='POST':
        id=len(products_list)+1
        name=req.POST.get('name')
        cost=req.POST.get('cost')
        new={
            'id':id,
            'name':name,
            'cost':cost
        }
        products_list.append(new)
    return render(req,'home.html',{'products_list':products_list})

def deleteproduct(req,id):
    global products_list
    list=[]
    for p in products_list:
        if p['id']!=id:
            list.append(p)
    products_list=list
    return redirect('/')

def updateproduct(req,id):
    global products_list
    if req.method=='POST':
        n=req.POST.get('new_product')
        c=req.POST.get('new_cost')
        for k in products_list:
            if k.get('id')==id:
                k['name']=n
                k['cost']=c
                return redirect('/')

    productedit=None
    for p in products_list:
        if p.get('id')==id:
            productedit=p
            break
    return render(req,'editpage.html',productedit)