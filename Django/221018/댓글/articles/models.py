from django.db import models
from django.forms import DateTimeField

# Create your models here.
"""
제목 (최대 80자)
내용
사진 (optional)
"""

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
