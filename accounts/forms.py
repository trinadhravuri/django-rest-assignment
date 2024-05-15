from django.forms import ModelForm
from .models import Account, Address


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        error_messages = {
            "username": {
                'required':"Please enter your username"
            }
        }