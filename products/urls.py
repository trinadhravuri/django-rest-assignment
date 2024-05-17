from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home', views.home, name='home'),
    path('products_list', views.products_list, name="products_list")
]
