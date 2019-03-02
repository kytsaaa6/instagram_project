from django.db import models
from accounts.models import Account
import re


class Post(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    text = models.CharField(max_length=150, help_text="최대 150자 입력 가능")
    post_like = models.ManyToManyField(Account, related_name='post_like')
    tag_set = models.ManyToManyField('Tag', blank=True)

    @property
    def total_likes(self):
        return self.post_like.count()  # likes 컬럼의 값의 갯수를 센다

    # NOTE: content에서 tags를 추출하여, Tag 객체 가져오기, 신규 태그는 Tag instance 생성, 본인의 tag_set에 등록,
    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.text)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가


class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True)
