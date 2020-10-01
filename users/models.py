from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  age = models.PositiveIntegerField(default=0)
  fullname = models.CharField(max_length=10)

  def __str__(self):
    return self.fullname


