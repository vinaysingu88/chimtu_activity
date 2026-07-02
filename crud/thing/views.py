from django.shortcuts import render

# Create your views here.
products_list=[
    {'id':1 , 'name':'pant','cost':100},
    {'id':2 , 'name':'pant1','cost':110},
    {'id':3 , 'name':'pant2','cost':120},
    {'id':4 , 'name':'shirt','cost':200}
]


def thank(req):
    return render(req,'thank.html')


def product_view(req):
    if req.method=='POST':
        id=len(products_list)+1
        name=req.POST.get('name')
        cost=req.POST.get('cost')
        new={
            'id': id,
            'name':name,
            'cost':cost
        }
        products_list.append(new)
    return render(req,'home.html',{'products_list':products_list})

    