from django.urls import path, re_path
from post import views
from post.converters import MonthConverter
from django.urls import register_converter

register_converter(MonthConverter, "mth")

urlpatterns = [
    path("topic_list_view/", views.topic_list_view),
    path("topic/<int:topic_id>/", views.topic_detail_view),
    path("topic_comment/", views.add_comment_to_topic_view)
]