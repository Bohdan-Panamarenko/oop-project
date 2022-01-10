import django_filters

from .models import *


class RequisiteTypeFilter(django_filters.FilterSet):
    class Meta:
        model = Requisite
        fields = ['requisite_type_id']


class RequisiteFilter(django_filters.FilterSet):
    class Meta:
        model = RequisiteHistory
        fields = ['requisite_id', 'requisite_id__name']
