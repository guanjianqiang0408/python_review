from django import template
register = template.Library()


# 简单标签, 通过接收参数，对输入参数做一些处理并返回结果
@register.simple_tag
def prefix_tags(cur_str):
    """
    自定义标签，为传入值添加指定前缀
    使用自定义标签需要在模板中使用load标签声明
    {% load custom_tags %}
    {% prefix_tag "xxx"%}
    :param cur_str:
    :return:
    """
    return f"Hello {cur_str}"


@register.simple_tag(takes_context=True)
def prefix_tags_bk(context, cur_str):
    """
    如果想在标签中访问字典上下文，需要指定takes_context=True
    且第一个参数是context
    使用该标签t.render(Context({prefix: XXX}))
    :param context:
    :param cur_str:
    :return:
    """
    return f"{context['prefix']} {cur_str}"


# 引入标签， 可以被其他模板进行渲染，然后将渲染结果输出
# 第一个参数指定模板文件，第二个参数可以使用上下文字典
# 对于具有通用展现样式但不同数据渲染的页面，考虑使用引入标签
@register.inclusion_tag("post/inclusion.html", takes_context=True)
def hello_inclusion_tag(context, cur_str):
    return {"hello": f"{context['prefix']} {cur_str}"}


# 赋值标签， 与简单标签类似，但是结果不被直接输出，而是存储到上下文变量中
# 目的是降低传递上下文成本
# 使用方式
"""
{% hello_assignment_tag 'Django BBS' as hello %}
{{ hello }}
"""
# 模板中使用hello_assignment_tag标签的地方用as参数将标签的返回结果保存在hello中，所以模板渲染
# 的时候不需要传递hello到上下文中
@register.simple_tag
def hello_assignment_tag(cur_str):
    return f"Hello {cur_str}"


# 过滤器 {{ hello | length }}
"""
   过滤器用于在显示变量之前对变量的值进行调整，它们在模板中很常见，使用管道符号（|）指定
        length 获取变量长度
        lower   转小写
        upper   转大写
   自定义过滤方便了对变量的处理过程
"""
@register.filter
def replace_django(value):
    """
    自定义过滤器，转换指定字符串
    模板中使用自定义过滤器需要{% load custom_tags %}
    {{ hello django | replace_django}}
    可以通过register.filter(name="r_django")方式指定过滤器名称
    :param value:
    :return:
    """
    return value.replace("django", "Django")


@register.filter
def replace_django_args(value, base):
    """
    带有参数的自定义过滤器
    :param value:
    :param base:
    :return:
    """
    return value.replace("django", base)
