from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.admin, name='admin_home'),
    path('employee_main/', views.employee_main, name='employee_main'),
    path('salary/<int:pk>', views.salary, name='salary'),
    path('roles_employee/<int:pk>', views.roles_employee, name='roles_employee'),
    path('requisite_employee/<int:pk>', views.requisite_employee, name='requisite_employee'),
=======
    path('', views.admin, name='admin_home')
>>>>>>> 2e166d30e963d225d123d3ad03c11980f04e4c4d
]