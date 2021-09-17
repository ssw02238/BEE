from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass



# ESG 성향 테스트 추가
class Survey(models.Model):
    pass