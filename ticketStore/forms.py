from django import forms
from .models import Order
from django.forms import ModelForm, TextInput, DateInput
from datetime import date
from phone_field import PhoneField
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'mail', 'cc_number', 'cc_expiry', 'cc_code']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Surname Name'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'mail': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'cc_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Card number'
            }),
            'cc_expiry': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Expiry date'
            }),
            'cc_code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CVC code'
            }),
        }