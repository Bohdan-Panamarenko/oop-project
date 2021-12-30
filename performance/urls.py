from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='perf_home'),
    path('performance', views.performance, name='performance'),
    path('sort_performance/<int:pk>', views.sort_performance, name='sort_performance'),
    path('create_performance', views.create_performance, name='create_performance'),
    path('performance/<int:pk>/update', views.PerformanceUpdateView.as_view(), name='performance_update'),
    path('performance/<int:pk>/delete', views.PerformanceDeleteView.as_view(), name='performance_delete'),
    path('performance/<int:pk>', views.PerformanceDetailView.as_view(), name='performance_info'),
    path('performance_on_going', views.performance_on_going, name='performance_on_going'),
    path('sort_performance_on_going/<int:pk>', views.sort_performance_on_going, name='sort_performance_on_going'),
    path('create_performance_on_going', views.create_performance_on_going, name='create_performance_on_going'),
    path('performance_on_going/<int:pk>/update', views.PerformanceOnGoingUpdateView.as_view(), name='performance_on_going_update'),
    path('performance_on_going/<int:pk>/delete', views.PerformanceOnGoingDeleteView.as_view(), name='performance_on_going_delete'),
    path('performance_on_going/<int:pk>', views.PerformanceOnGoingDetailView.as_view(), name='performance_on_going_info'),
]
