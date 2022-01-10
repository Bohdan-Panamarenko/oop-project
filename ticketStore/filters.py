import django_filters

from performance.models import *


class PerformanceFilter(django_filters.FilterSet):
    class Meta:
        model = Performance
        fields = ['name']


class PosterFilter(django_filters.FilterSet):
    class Meta:
        model = Poster
        fields = ['performance_id__name']
