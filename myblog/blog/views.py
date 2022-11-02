from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def hello(request):
    return HttpResponse("欢迎Django")


# 首页
def index(request):
    pass


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