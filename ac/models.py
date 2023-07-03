from django.db import models

# 사용자 계정 관련은 공식페이지 가이드 따라
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class User(AbstractUser):
    pass
# 그대로 상속받아 사용하고 별도 변경은 없음