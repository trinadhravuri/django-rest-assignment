from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home', views.home, name='home'),
    path('product-detail/<int:id>', views.product_detail, name='product-detail'),
    path('products_list', views.products_list, name="products_list"),
]
