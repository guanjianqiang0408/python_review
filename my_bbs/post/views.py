# 引入HttpResponse, 作为视图的返回类型
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from post.models import Topic, Comment
from post.post_service import build_topic_base_info, build_topic_detail_info, add_comment_to_topic
from post.forms import TopicSearchForm


def search_topic(request):
    form = TopicSearchForm(request.GET)
    if form.is_valid():
        topic_queryset = Topic.objects.filter(title__contains=form.cleaned_data.get("title"))
        return render(request, 'post/topic_list.html', context={"topics": topic_queryset})
    else:
        return render(request, "post/search_topic.html", context={"form": form})


def search_topic_form(request):
    """
     form view function
    :param request:
    :return:
    """
    form = TopicSearchForm()
    return render(request, "post/search_topic.html", context={"form": form})


def project_signature(request):
    """
    自定义处理器函数
    :param request:
    :return:
    """
    return {"project": "Django BBS"}


def hello_django(request):
    """
    :param request:
    :return:
    """
    return render(request, "post/hello_django.html")


def topic_list_view(request):
    """
    话题列表
    :param request:
    :return:
    """
    topic_queryset = Topic.objects.all()
    result = {
        "count": topic_queryset.count(),
        "info": [build_topic_base_info(topic) for topic in topic_queryset]
    }
    return JsonResponse(result)


def topic_detail_view(request, topic_id):
    """
    话题详细信息
    :param request:
    :param topic_id:
    :return:
    """
    try:
        result = build_topic_detail_info(Topic.objects.get(pk=topic_id))
    except Topic.DoesNotExist:
        pass
    else:
        return JsonResponse(result)


@csrf_exempt
def add_comment_to_topic_view(request):
    """
    给话题添加评论
    :param request:
    :return:
    """
    topic_id = int(request.POST.get("id", 0))
    content = request.POST.get("content", "")
    topic = None
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        pass
    if topic and content:
        return JsonResponse({"id": add_comment_to_topic(topic, content).id})
    return JsonResponse({"message": "Add comment failed"})
