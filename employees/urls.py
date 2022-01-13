from django.contrib import admin
from django.urls import path
from employees import views


admin.autodiscover()

urlpatterns = [
    path('', views.main, name='employee'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employees/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_info'),
    path('employees/filter/<int:pk>', views.filter_employees, name='filter_employees'),
    path('hiring/<int:pk>/update/', views.HiringUpdateView.as_view(), name='hiring_update'),
    path('hiring/<int:pk>/delete/', views.HiringDeleteView.as_view(), name='hiring_delete'),
    path('hiring/<int:pk>', views.HiringDetailView.as_view(), name='hiring_info'),
    path('hiring/filter/<int:pk>', views.filter_hiring, name='filter_hiring'),
    path('roles_list/<int:pk>/update/', views.RolesListUpdateView.as_view(), name='roles_list_update'),
    path('roles_list/<int:pk>/delete/', views.RolesListDeleteView.as_view(), name='roles_list_delete'),
    path('roles_list/<int:pk>', views.RolesListDetailView.as_view(), name='roles_list_info'),
    path('roles_list/filter/<int:pk>', views.filter_roles_list, name='filter_roles_list'),
    path('positions/<int:pk>/update/', views.PositionsUpdateView.as_view(), name='positions_update'),
    path('positions/<int:pk>/delete/', views.PositionsDeleteView.as_view(), name='positions_delete'),
    path('positions/<int:pk>', views.PositionsDetailView.as_view(), name='positions_info'),
    path('positions/filter/<int:pk>', views.filter_positions, name='filter_positions'),
    path('roles/<int:pk>/update/', views.RolesUpdateView.as_view(), name='roles_update'),
    path('roles/<int:pk>/delete/', views.RolesDeleteView.as_view(), name='roles_delete'),
    path('roles/<int:pk>', views.RolesDetailView.as_view(), name='roles_info'),
    path('roles/filter/<int:pk>', views.filter_roles, name='filter_roles'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('create_position/', views.create_position, name='create_position'),
    path('create_role/', views.create_role, name='create_role'),
    path('create_role_list/', views.create_role_list, name='create_role_list'),
    path('create_hiring/', views.create_hiring, name='create_hiring'),
    path('employees/', views.employees, name='employees'),
    path('roles_list/', views.roles_list, name='roles_list'),
    path('hiring/', views.hiring, name='hiring'),
    path('roles/', views.roles, name='roles'),
    path('positions/', views.positions, name='positions')
]