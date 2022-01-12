from django.contrib import admin
from django.urls import path, include
from ticketStore import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('performances/', include('performance.urls')),
    path('ticketStore/', include('ticketStore.urls')),
    path('', include('main.urls')),
    path('requisite/', include('requisite.urls')),
    path('employees/', include('employees.urls')),
    path('admin_home/', include('admin_home.urls')),
    path('orders/', views.ordersList, name='orders'),
    path('orders/<int:pk>/delete/', views.OrdersDeleteView.as_view(), name='orders_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
