from django.urls import include, path
from .import views
urlpatterns = [
    path('',views.home),
    path('delete/<int:id>',views.deleteproduct,name="deleprod"),
    path('edit/<int:id>',views.updateproduct,name="editprod")
]