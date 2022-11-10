from django.urls import path, re_path
from post import views
from post.converters import MonthConverter
from django.urls import register_converter

register_converter(MonthConverter, "mth")

urlpatterns = [
    path("hello/", views.hello_django_bbs),
    # URL解析器会将请求发送到一个函数而不是一个类,所以需要用到View提供的as_view方法完成URL定义
    path("hello_class/", views.FisrtView.as_view()),
    # 这里将转换器类型名设置为mth，这样月份字段就只能传递1-12数字
    path("dynamic/<int:year>/<mth:month>/<int:day>", views.dyanmic_hello),
    # 正则表达式路由, 这样可以实现与之前path自定义转换器类似的匹配功能
    re_path("re_dynamic/(?p<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/", views.dyanmic_hello)
]