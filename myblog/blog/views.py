from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    list = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
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
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
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
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)
    page = request.GET.get("page")
    tags = Tag.objects.all()
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
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get("page")
    tags = Tag.objects.all()
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
