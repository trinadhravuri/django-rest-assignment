from django.urls import path
from .import views

urlpatterns = [
    path('token-auth', views.TokenAuthView.as_view(), name='token-auth'),
]
