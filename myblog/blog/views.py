from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, Banner, Tag, Link


# Create your views here.
def hello(request):
    return HttpResponse("欢迎Django")


# 首页
def index(request):
    categorys = Category.objects.all()
    banners = Banner.objects.filter(is_active=True)[0:4]
    tuis = Article.objects.filter(tui__id=1)
    articles = Article.objects.all().order_by("-id")[0:10]
    hot_articles = Article.objects.all().order_by("views")[:10]
    remens = Article.objects.filter(tui__id=2)
    tags = Tag.objects.all()
    link = Link.objects.all()
    # 构造上下文
    context = {
        "categorys": categorys,
        "banners": banners,
        "tuis": tuis,
        "articles": articles,
        "hot_articles": hot_articles,
        "remens": remens,
        "tags": tags,
        "link": link,
    }
    # 传递上下文
    return render(request, "index.html", context)


# 列表
def list(request, lid):
    pass


# 内容
def show(request, sid):
    pass


# 标签
def tag(request, tag):
    pass


#搜索
def search(request):
    pass


# 关于我们
def about(request):
    pass