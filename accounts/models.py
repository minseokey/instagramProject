from django.db import models
from django.contrib.auth.models import AbstractUser

# 기본 장고의 회원가입 방법 사용
class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)

# class Profile(models.Model):
