from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import AccountForm, AddressForm
from django.contrib import auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user =  User.objects.create_user(username=username, first_name=first_name,
                                             last_name = last_name, email=email, password=password)   
            user.save()
            return redirect('home')
    else:
        form = AccountForm(initial={})
    return render(request, 'register.html', {'form': form})
        
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def user_dashboard(request):
    username = request.user.username
    return render(request, 'dashboard.html',{'username':username})

def user_logout(request):
    logout(request)
    return redirect('home')