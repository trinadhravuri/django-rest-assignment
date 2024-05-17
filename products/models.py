from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class SubCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sub_desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.name


class SubCategoryProducts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name