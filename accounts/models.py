from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account(AbstractUser):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

    @property
    def total_follow(self):
        return self.follow.all().count()

    @property
    def total_follower(self):
        return self.follower.all().count()

class Follow(models.Model):
    follow = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='follow')
    follower = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='follower')

