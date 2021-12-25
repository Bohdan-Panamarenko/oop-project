from django.contrib import admin
from .models import Performance, Genre, Rating, Hall, Tier, Poster
# Register your models here.

admin.site.register(Performance)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(Hall)
admin.site.register(Tier)
admin.site.register(Poster)

