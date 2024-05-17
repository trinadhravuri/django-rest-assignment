from django.urls import path
from . import views

urlpatterns = [
    path('/view-cart', views.view_cart, name='view-cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/remove/<int:product_id>', views.remove_from_cart, name="remove_from_cart"),
]
