from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('performance', views.performance, name='performance'),
    path('performancesoon', views.performance_to_be, name='performancesoon'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]