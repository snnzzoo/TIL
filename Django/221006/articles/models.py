from django.db import models

# Create your models here.
"""
게시판 기능
- 제목 (20글자 이내)
- 내용
- 작성 일시 / 수정 일시 (자동으로 기록, 날짜 / 시간)
"""

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
