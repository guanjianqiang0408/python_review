from django.shortcuts import render
# 引入HttpResponse, 作为视图的返回类型
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views import View


# Create your views here.
# 函数视图 FBV
# 视图函数的第一个参数是HttpRequest类型对象
# 添加csrf_exempt装饰器函数，用POST方法请求对应的URL，可以获得GET请求同样的响应
@csrf_exempt
# 添加require_http_methods装饰器指定视图可以接受的方法, 这里指定该视图只允许接受GET POST请求
@require_http_methods(["GET", "POST"])
# @require_GET 该装饰指定视图只可以接受GET方法
# @require_POST 该装饰指定视图只可以接受POST方法
def hello_django_bbs(request):
    """
    :param request:
    :return:
    """
    # 函数内部定义业务处理逻辑, 这里简单定义了视图的相应内容
    html = "<h1>Hello Django BBS</h1>"
    # 视图最后返回一个HttpResponse对象，标识一次Web请求的结束
    return HttpResponse(html)


# 利用Mixin实现代码复用
"""
    一个Mixin就是一个python对象，但是这个类不一定需要又明确的语义, 其主要目的是实现代码复用。
Mixin在表现形式上是多重继承，运行期间，实现动态改变父类或类的方法。一个视图类可以继承多个Mixin，
但是只能继承一个View，写法通常会把Mixin放在View前面
"""


class ExecTimeMixin:
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        类视图重写的父类的dispatch方法, dispatch根据HTTP类型实现请求分发
        类对象中定义的方法与普通函数不同, 所以，应用于函数的装饰器不能直接应用到类方法上,
        需要将它最喜欢更换为类方法的装饰器. 可以看到在dispatch方法上添加了@method_decorator装饰器
        该装饰器可以将函数装饰器转换为类方法装饰器，所以csrf_exempt装饰可以被用在类方法上
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().dispatch(request, *args, **kwargs)


# 类视图, CBV, 类视图最大的特点是可以利用不同实例方法响应不同HTTP请求方法，
# 且可以利用面向对象的技术将代码费解为可重用组件
class FisrtView(ExecTimeMixin, View):
    html = "hello django bbs"

    def get(self, request):
        return HttpResponse(self.html + "GET")

    def post(self, request):
        return HttpResponse(self.html + "POST")


# 动态路由使用
def dyanmic_hello(request, year, month, day):
    """
    视图函数也是普通的python函数，所以除了django规定的HttpRequest对象之外，还可以定义其他额外参数。
    那么对于视图函数中的其他参数，如何传值，这就引出的动态路由的概念，即URL不是固定的，URL中包含了传递给
    视图函数的参数变量。
    相对于动态路由，之前定义的就是静态路由
    :param request:
    :param year:
    :param month:
    :param day:
    :return:
    """
    html = "hello django, {}-{}-{}".format(year, month, day)
    return HttpResponse(html)

