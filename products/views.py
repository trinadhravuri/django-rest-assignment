from django.shortcuts import render
from .models import Category, SubCategory, SubCategoryProducts
# Create your views here.


def base(request):
    return render(request,'base.html')


def home(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    products = SubCategoryProducts.objects.all()
    context = {
        'categories': categories,
        'subcategories': subcategories,
        'products': products
    }
    return render(request,'home.html', context)

def product_detail(request,id):
    product = SubCategoryProducts.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request,'product_detail.html', context)

def products_list(request):
    
    queryset = SubCategoryProducts.objects.all()
    categories = SubCategory.objects.all()
    
    query = request.GET.get('x')
    
    if query:
        queryset = queryset.filter(name__icontains=query)
    
    category = request.GET.get('category')
    
    if category:
        queryset = queryset.filter(subcategory__name__contains = category)
    
    order_by = request.GET.get('order_by')
    if order_by:
        queryset = queryset.order_by(order_by)
    
    context = {'products': queryset, 'categories': categories}
    
    return render(request, 'products_list.html', context)