from django.shortcuts import render
from .models import Order, OrderItem

# Create your views here.

def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html',{'orders':orders})