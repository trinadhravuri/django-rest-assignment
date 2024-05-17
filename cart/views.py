from django.shortcuts import render, redirect
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from products.models import SubCategoryProducts
# Create your views here.

@login_required
def view_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)
    return render(request, 'view_cart.html', {'cart': cart})

@login_required
def add_to_cart(request, id):
    product = SubCategoryProducts.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, product_id):
    product = SubCategoryProducts.objects.get(pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')