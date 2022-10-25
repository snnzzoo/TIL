from django.db import models
from django.forms import DateTimeField

# Create your models here.
"""
게시판 기능
- 제목
- 내용
- 글 작성시간 / 수정시간 (자동으로 기록, 날짜 / 시간)
"""

# 모델 설계 (DB 스키마 설계)


class Appp(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
