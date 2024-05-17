from django.urls import path
from . import views

urlpatterns = [
    path('view_cart', views.view_cart, name='view_cart'),
    path('/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('cart/remove/<int:product_id>', views.remove_from_cart, name="remove_from_cart"),
]
