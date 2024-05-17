from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import AccountForm, AddressForm
from django.contrib import auth, messages
from products.models import Category, SubCategory, SubCategoryProducts

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
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request,"Username already Exists, please choose another")
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request,"EMAIL already Exists, please choose another")
                    else:
                        user =  User.objects.create_user(username=username, first_name=first_name,
                                             last_name = last_name, email=email, password=password)
                        user.save()
                        messages.success(request, f"Welcome {username}..! registration success Please Login ")
                        return redirect('login')
            else:
                messages.error(request,"Password do not match")
            
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
            messages.error(request,"Invalid username or password")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def user_dashboard(request):
    username = request.user.username
    products = SubCategoryProducts.objects.all()
    return render(request, 'dashboard.html',{'username':username,'products':products})

def user_logout(request):
    logout(request)
    return redirect('home')

def update_user(request):
    user = request.user
    if request.method == 'POST':
        # form = AccountForm(request, instance=user_account)
        # if form.is_valid():
        #     form.save()
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        User.objects.filter(id=user.id).update(username=username, 
                                          first_name=first_name, 
                                          last_name=last_name)
        
        messages.success(request,"Profile Updates successfully")
        return redirect('dashboard')
    else:
        # form = AccountForm(request, instance=user_account)
        return render(request, 'update_profile.html')
    

def password_reset(request):
    pass
