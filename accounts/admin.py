from django.contrib import admin
from .models import Address, Account
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
