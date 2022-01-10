from django.contrib import admin
from .models import Employee, Role, Hiring, Position

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Role)
admin.site.register(Hiring)
