from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    """
        post应用的model基类
    """
    class Meta:
        # 声明该类为抽象类，不能被实例化
        abstract = True
        # 声明排序规则，按照创建时间降序排列
        ordering = ['-created_time']
    # 定义两个属性，创建时间和修改时间
    created_time = models.DateTimeField(auto_now_add=True, help_text="创建时间")
    last_modified = models.DateTimeField(auto_now=True, help_text="修改时间")

    # 定义一个抽象方法，作用是优化print出Model实例的样式
    def __str__(self):
        raise NotImplementedError


class Topic(BaseModel):
    """
    话题
    """
    title = models.CharField(max_length=255, unique=True, help_text="话题标题")
    content = models.TextField(help_text="话题内容")
    is_online = models.BooleanField(default=True, help_text="话题是否在线")
    # 外键关联User模型
    user = models.ForeignKey(to=User, to_field='id', on_delete=models.CASCADE, help_text="话题关联用户表")

    class Meta:
        verbose_name = "话题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.id}: {self.title[:20]}"


class Comment(BaseModel):
    """
    评论
    """
    content = models.CharField(max_length=255, help_text="话题评论")
    # 外键关联话题表
    topic = models.ForeignKey(to=Topic, to_field='id', on_delete=models.CASCADE, help_text="话题标题")
    up = models.IntegerField(default=0, help_text="支持")
    down = models.IntegerField(default=0, help_text="反对")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        # id 属性如果model中没有主动指定逐渐的情况，Django会自动添加一个主键
        return f"{self.id}: {self.content[:20]}"
