from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at', 'image')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'article')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
