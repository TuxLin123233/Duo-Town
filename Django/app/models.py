from django.db import models
from .choices import *

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")

    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default='U',
        verbose_name="性别",
    )

    headshot = models.CharField(
        choices=HEADSHOT_CHOICES,
        default='U',
        verbose_name="头像"
    )

    age = models.IntegerField(default=0, verbose_name="年龄")

    fans = models.ManyToManyField(
        to="User",
        related_name="following",
        verbose_name="粉丝",
        blank=True,
    )

    likes = models.IntegerField(default=0, verbose_name="点赞数")

    def __str__(self):
        return self.username

    """获取粉丝数量"""
    def get_fans_length(self):
        return self.fans.count()

    def get_following_length(self):
        return self.following.count()

    def get_friends_length(self):
        friends = self.fans.all() & self.following.all()
        return friends.count()

    class Meta:
        verbose_name = "居民"