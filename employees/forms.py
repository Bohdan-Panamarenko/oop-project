from .models import Employee, Position, Role, Hiring, Roles
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['id', 'position']
        widgets = {
            "id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Id'
            }),
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Position'
            })
        }


class HiringForm(ModelForm):
    class Meta:
        model = Hiring
        fields = ['id', 'employee_id', 'position_id', 'hiring_date']
        widgets = {
            "id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Id'
            }),
            "employee_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee id'
            }),
            "position_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Position id'
            }),
            "hiring_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of hiring'
            })
        }


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['id', 'employee_id', 'poster_id', 'role_id', 'fee']
        widgets = {
            "id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Id'
            }),
            "employee_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee id'
            }),
            "poster_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Poster id'
            }),
            "role_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            "fee": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fee'
            })
        }


class RoleListForm(ModelForm):
    class Meta:
        model = Roles
        fields = ['name', 'performance_id']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee id'
            }),
            "performance_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Poster id'
            })
        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'patronymic', 'phone', 'work_book', 'email', 'address', 'date_of_birth']
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Patronymic'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }),
            "work_book": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Work book'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            "date_of_birth": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of birth'
            })
        }
