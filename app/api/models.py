from django.db import models

class User(models.Model):
    """用户"""
    class Gender(models.TextChoices):
        MALE = 'M', "男"
        FEMALE = 'F', "女"
        OTHER = 'O', "其他"
        UNKNOWN = 'U', "未知"

    name = models.CharField(max_length=20)                                          # 名字
    password = models.CharField(max_length=20)                                      # 密码
    created_at = models.DateTimeField(auto_now_add=True, null=True)                 # 帐号创建时间
    followings = models.ManyToManyField("User", related_name="following")        # 关注
    # 年龄
    age = models.IntegerField(default=0)

    # 性别
    gender = models.CharField(
        choices=Gender.choices,
        max_length=2,
        default=Gender.UNKNOWN
    )

    def __str__(self):
        return self.name

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