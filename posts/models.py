from django.db import models
from accounts.models import Account


class Post(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True)
    text = models.TextField()

    @property
    def like_count(self):
        return self.like_set.all().count()


class Like(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
