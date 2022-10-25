from email.policy import default
from django.db import models

# Create your models here.
"""
- 영화 제목 (50글자 이내)
- 영화 줄거리 (긴 글)
- 상영 시간 (0 이상)
- 작성 날짜 / 수정 날짜 (자동으로 기록, 월 / 년)
"""

class Movie(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    running_time = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)