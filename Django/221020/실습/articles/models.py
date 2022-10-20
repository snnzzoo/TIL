from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
"""
미술 감상
- 제목 (20자 이내)
- 내용 (긴 글)
- 글 작성시간 / 글 수정시간 (자동으로 기록, 날짜 / 시간)
- 이미지
- 한줄 감상평 (30자 이내)
"""

class Article(models.Model):
    title = models.CharField(max_length=20)
    art_title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(960, 540)],
                                format='JPEG',
                                options={'quality': 100})
    one_line = models.CharField(max_length=30)
    thumbnail = ImageSpecField(source='image', 
                                processors=[ResizeToFill(120,80)], 
                                format='JPEG')

