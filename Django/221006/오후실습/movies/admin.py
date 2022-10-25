from django.contrib import admin
from .models import Movie


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'running_time', 'created_at', 'updated_at']

admin.site.register(Movie, MovieAdmin)
