from django.urls import path
from . import views

urlpatterns = [
    path('order-history', views.order_history, name="order-history"),
]


