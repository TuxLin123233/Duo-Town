from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)    # 用户名
    password = models.CharField(max_length=20)                 # 密码

    def __str__(self):
        return self.username