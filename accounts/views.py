from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
# Create your views here.


def register(request):
    if request.method == 'POST':
        pass
