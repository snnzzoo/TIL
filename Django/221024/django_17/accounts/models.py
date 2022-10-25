from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    # pass
    # A가 B를 팔로잉, 맞팔은 아님(symmetrical=False)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'