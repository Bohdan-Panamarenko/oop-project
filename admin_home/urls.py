from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name='admin_home'),
    path('employee_main/', views.employee_main, name='main_employee'),
    path('salary/<int:pk>', views.salary, name='salary'),
    path('info/<int:pk>', views.EmployeeDetailView.as_view(), name='info_employee'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update_employee'),
    path('roles_employee/<int:pk>', views.roles_employee, name='roles_employee'),
    path('requisite_employee/<int:pk>', views.requisite_employee, name='requisite_employee'),

]