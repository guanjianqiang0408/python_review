from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def hello(request):
    return HttpResponse("欢迎Django")


def index(request):
    # 更多ORM操作文章参见https://www.django.cn/course/show-18.html and https://www.django.cn/course/show-31.html
    articles = Article.objects.all()
    # 封装上下文
    context = {
      "articles": articles
    }
    return render(request, "index.html", context)
