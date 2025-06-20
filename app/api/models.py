from django.db import models

"""用户"""
class User(models.Model):
    username = models.CharField("用户名", max_length=20)
    password = models.CharField("用户密码", max_length=20)
    created_at = models.DateTimeField("帐号创建时间", auto_now_add=True, null=True)
    age = models.IntegerField("年龄", default=0)
    gender = models.CharField("性别", max_length=3, default="未知")

    followings = models.ManyToManyField("User", related_name="following", verbose_name="用户关注的人")

    def __str__(self):
        return self.username

class Blog(models.Model):
    """文章"""
    title = models.CharField(max_length=20)         # 标题
    content = models.TextField()                    # 内容
    date = models.DateTimeField(auto_now_add=True)  # 日期和时间
    # 作者, models.CASCADE表示引用一个父模型
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """评论"""
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.content