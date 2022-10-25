from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'content']

admin.site.register(Article, ArticleAdmin)