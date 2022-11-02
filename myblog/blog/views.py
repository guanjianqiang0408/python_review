from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("欢迎Django")


def index(request):
    sitename, url = "Django中文网", "www.django.cn"
    step_list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型'
    ]
    info_dict = {
        'name': '小强',
        'qq': '905685941',
        'wx': 'G13304473252',
        'email': '905685941@qq.com',
    }
    # 封装上下文
    context = {
        "sitename": sitename,
        "url": url,
        "step_list": step_list,
        "info_dict": info_dict
    }
    return render(request, "index.html", context)
