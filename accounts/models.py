from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255, default ='')
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Account"
        
        
class Address(models.Model):
    address_user = models.ForeignKey(Account, related_name='account', on_delete=models.CASCADE)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    door_no = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=200)
    
    def __str__(self):
        return self.address_user
    
    class Meta:
        verbose_name_plural = "Address"

# @receiver(post_save, sender = User)
# def create_auth_token(sender, instance= None,created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)