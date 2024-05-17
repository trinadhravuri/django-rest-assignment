from django.forms import ModelForm
from .models import Account, Address
from django import forms
from django.forms import widgets


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

        widgets = {
            'password':forms.PasswordInput(),
            'confirm_password':forms.PasswordInput(),
        }
        
        
            

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        error_messages = {
            "username": {
                'required':"Please enter your username"
            }
        }