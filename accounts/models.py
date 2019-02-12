from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    phone = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)

    @property
    def follow_count(self):
        return self.follows.all().count()

    @property
    def follower_count(self):
        return self.followers.all().count()


class Follow(models.Model):
    follow = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='follows')
    follower = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='followers')

