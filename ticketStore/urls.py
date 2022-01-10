from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticketStore_main, name='ticketStore_main'),
    path('hot', views.ticketStore_hot, name='ticketStore_hot'),
    path('<int:pk>', views.ticketStore_performance, name='ticketStore_performance'),
    path('order/<int:pk>/<int:pkt>', views.ticketStore_order, name='ticketStore_order'),
    path('form', views.ticketStore_form, name='ticketStore_form'),
    path('filter/<int:pk>', views.performance_filter, name='performance_filter'),
    path('<str:pk>', views.ticketStore_main, name='ticketStore_main'),
]
