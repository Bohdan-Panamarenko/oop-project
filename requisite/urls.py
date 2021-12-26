from django.contrib import admin
from django.urls import path, include
from . import views


admin.autodiscover()

urlpatterns = [
    path('', views.main, name="req_home"),
    path('requisite/', views.requisite, name='requisite'),
    path('requisite_history/', views.requisite_history, name='requisite_history'),
    path('requisite_poster_role/', views.requisite_poster_role, name='requisite_poster_role')
]