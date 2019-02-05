from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    phone = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)



