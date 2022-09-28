from email.policy import default
from django.db import models

# Create your models here.


class Todo(models.Model):
    # django에서 pk는 자동으로 만들어준다.
    # => id를 정해줄 필요가 없다.
    content = models.CharField(max_length=80)
    """
    default
     : 데이터를 생성할 때 값을 넣지 않으면
     자동으로 값을 채워서 데이터를 생성하겠다.
    """
    completed = models.BooleanField(default=False)
