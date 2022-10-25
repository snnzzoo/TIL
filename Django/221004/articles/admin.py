from django.contrib import admin
from .models import Article

# Register your models here.
# https://docs.djangoproject.com/ko/4.1/intro/tutorial07/


class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)
