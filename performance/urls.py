from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='perf_home'),
    path('performance', views.performance, name='performance'),
    path('sort_performance/<int:pk>', views.sort_performance, name='sort_performance'),
    path('performance_on_going', views.performance_on_going, name='performance_on_going'),
    path('sort_performance_on_going/<int:pk>', views.sort_performance_on_going, name='sort_performance_on_going')
]
