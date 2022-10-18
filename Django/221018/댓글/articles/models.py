from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField

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
    image = ProcessedImageField(upload_to='images/',
                                blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})
    thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(240, 160)],
                                format='JPEG',
                                options={'quality': 100})


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)