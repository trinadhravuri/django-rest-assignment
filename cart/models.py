from django.db import models
from django.contrib.auth.models import User
from products.models import SubCategoryProducts


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(SubCategoryProducts, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(SubCategoryProducts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

