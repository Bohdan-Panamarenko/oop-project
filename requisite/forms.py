from .models import Requisite, RequisiteType, RequisiteHistory, RequisitePosterRole
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, Select


class RequisiteTypeForm(ModelForm):
    class Meta:
        model = RequisiteType
        fields = ['type']
        widgets = {
            'type': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type'
            }),
        }


class RequisiteForm(ModelForm):
    class Meta:
        model = Requisite
        fields = ['name', 'requisite_type_id']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'requisite_type_id': Select(attrs={
                'class': 'form-control',
            }),
        }


class RequisiteHisForm(ModelForm):
    class Meta:
        model = RequisiteHistory
        fields = ['requisite_id', 'price', 'description']
        widgets = {
            'requisite_id': Select(attrs={
                'class': 'form-control',
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
        }


class RequisiteRoleForm(ModelForm):
    class Meta:
        model = RequisitePosterRole
        fields = ['requisite_id', 'poster_id', 'role_id']
        widgets = {
            'requisite_id': Select(attrs={
                'class': 'form-control',
            }),
            'poster_id': Select(attrs={
                'class': 'form-control',
            }),
            'role_id': Select(attrs={
                'class': 'form-control',
            }),
        }
