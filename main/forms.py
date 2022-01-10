from employees.models import Account
from django.forms import ModelForm, TextInput, PasswordInput


class EmployeeForm(ModelForm):
    class Meta:
        model = Account
        fields = ['employee_id', 'login', 'password']
        widgets = {
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Login'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "employee_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee Id'
            })
        }
