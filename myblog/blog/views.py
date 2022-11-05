from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, Banner, Tag, Link


def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    return locals()


# Create your views here.
def hello(request):
    return HttpResponse("欢迎Django")


# 首页
def index(request):
    banners = Banner.objects.filter(is_active=True)[0:4]
    tuis = Article.objects.filter(tui__id=1)
    articles = Article.objects.all().order_by("-id")[0:10]
    hot_articles = Article.objects.all().order_by("views")[:10]
    link = Link.objects.all()

    return render(request, "index.html", locals())


# 列表
def list(request, lid):
    list = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    # 分页处理
    page = request.GET.get("page")
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, "list.html", locals())


# 内容
def show(request, sid):
    show = Article.objects.get(id=sid)
    # 随机推荐
    hot = Article.objects.all().order_by("?")[:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    # 增加文章浏览数
    show.views = show.views + 1
    show.save()
    return render(request, "show.html", locals())


# 标签
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)
    page = request.GET.get("page")
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, "tags.html", locals())


#搜索
def search(request):
    ss = request.GET.get("search")
    list = Article.objects.filter(title__icontains=ss)
    allcategory = Category.objects.all()
    page = request.GET.get("page")
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, "search.html", locals())


# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())
