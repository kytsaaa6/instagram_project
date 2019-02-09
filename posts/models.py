from django.db import models
from accounts.models import Account

class Post(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    text = models.TextField()
    post_like = models.ManyToManyField(Account, related_name='post_like')

    @property
    def total_likes(self):
        return self.post_like.count()  # likes 컬럼의 값의 갯수를 센다


# Create your models here.
