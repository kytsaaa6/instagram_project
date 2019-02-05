from django.db import models
from accounts.models import Account

class Post(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    text = models.TextField()


# Create your models here.
