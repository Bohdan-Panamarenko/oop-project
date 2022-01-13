from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name="req_home"),
    path('requisite/', views.requisite, name='requisite'),
    path('requisite_history/', views.requisite_history, name='requisite_history'),
    path('requisite_poster_role/', views.requisite_poster_role, name='requisite_poster_role'),
    path('create_requisite_type/', views.create_requisite_type, name='create_requisite_type'),
    path('create_requisite/', views.create_requisite, name='create_requisite'),
    path('create_requisite_his/', views.create_requisite_his, name='create_requisite_his'),
    path('create_requisite_role/', views.create_requisite_role, name='create_requisite_role'),
    path('requisite/<int:pk>/delete/', views.RequisiteDeleteView.as_view(), name='requisite_delete'),
    path('requisite_history/<int:pk>/delete/', views.RequisiteHisDeleteView.as_view(), name='requisite_his_delete'),
    path('requisite_poster_role/<int:pk>/delete/', views.RequisiteRoleDeleteView.as_view(),
                                                                                        name='requisite_role_delete'),
    path('requisite/<int:pk>/update/', views.RequisiteUpdateView.as_view(), name='requisite_update'),
    path('requisite_poster_role/<int:pk>/update/', views.RequisiteRoleUpdateView.as_view(),
                                                                                        name='requisite_role_update'),
    path('requisite/filter/<int:pk>', views.filter_requisite, name='requisite_filter'),
    path('requisite_history/filter/<int:pk>', views.filter_req_his, name='req_his_filter'),
    path('requisite_poster_role/filter/<int:pk>', views.filter_req_pos_role, name='req_pos_role_filter'),
]