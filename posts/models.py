from django.db import models
from accounts.models import Account
import re


class Post(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True)
    text = models.CharField(max_length=150, help_text="최대 150자 입력 가능")
    tags = models.ManyToManyField('Tag', blank=True)

    @property
    def like_count(self):
        return self.like_set.all().count()

    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.text)

        if not tags:
            return

        for taged in tags:
            tag, tag_created = Tag.objects.get_or_create(name=taged)
            self.tags.add(tag)


class Like(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
