from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    # 한국식 이름 출력 (성 + 이름)
    # @property
    # def get_full_name(self):
    #     return f'{self.last_name} {self.first_name}'