# 引入HttpResponse, 作为视图的返回类型
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from post.models import Topic, Comment
from post.post_service import build_topic_base_info, build_topic_detail_info, add_comment_to_topic


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
