from django.db import models
# 导入Django自带的User模型
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField

# Create your models here.
# 文章分类
class Category(models.Model):
    name = models.CharField("博客分类", max_length=100)
    index = models.IntegerField(default=999, verbose_name="分类排序")

    class Mete:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField("文章标签", max_length=100)

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐位
class Tui(models.Model):
    name = models.CharField("推荐位", max_length=100)

    class Mete:
        verbose_name = "推荐位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField("标题", max_length=70)
    excerpt = models.TextField("摘要", max_length=200, blank=True)
    # 外键关联分类表，一对多关系
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="分类", blank=True, null=True)
    # 外键关联标签表，多对多关系
    tags = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    img = models.ImageField(upload_to="article_img/%Y/%m/%d", verbose_name="文章图片", blank=True, null=True)
    # body = models.TextField()
    body = UEditorField(
        "内容",
        width=800,
        height=500,
        toolbars="full",
        imagePath="upimg/",
        filePath="upfile/",
        upload_settings={"imageMaxSize": 120400},
        settings={},
        command=None,
        blank=True
    )
    # 外键关联用户表，一对多关系
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    views = models.PositiveIntegerField("阅读量", default=0)
    # 外键关联推荐位，一对多关系
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name="推荐位", blank=True, null=True)
    created_time = models.DateTimeField("发布时间", auto_now_add=True)
    modified_time = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name


# 轮播图
class Banner(models.Model):
    text_info = models.CharField("标题", max_length=50, default="")
    img = models.ImageField("轮播图", upload_to="banner/")
    link_url = models.URLField("图片链接", max_length=100)
    is_active = models.BooleanField("是否激活", default=False)

    class Mete:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info


# 友情链接
class Link(models.Model):
    name = models.CharField("链接名称", max_length=20)
    linkurl = models.URLField("网址", max_length=100)

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name