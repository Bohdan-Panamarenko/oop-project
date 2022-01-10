from django.urls import path
from .views import main, authorization
from admin_home import views

urlpatterns = [
    path('', main, name='home'),
    path('authorization/', authorization, name='authorization'),
    path('', views.admin, name='admin_home'),
    path('requisite_admin', views.admin, name='requisite_admin')
]