from django.urls.converters import IntConverter


# 自定义月份转换器，定义完成后需要注册才能使用,在post.urls文件中完成注册
class MonthConverter(IntConverter):
    regex = "0?[1-9]|1[0-2]"


