from django.db import models
from ac.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


