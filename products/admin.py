from django.contrib import admin
from .models import Category, SubCategory, SubCategoryProducts
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategoryProducts)
class SubCategoryProductsAdmin(admin.ModelAdmin):
    pass
