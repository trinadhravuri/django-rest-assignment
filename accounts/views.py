from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login

from .forms import AccountForm, AddressForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AccountForm(initial={})
    return render(request, 'register.html', {'form': form})
        
