from django.contrib import admin
from .models import Topic, Comment


# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    自定义管理后台，添加批量上下线功能
    """
    # 减低数据库检索开销
    raw_id_fields = ("user",)

    # 指定只读，不可修改的属性内容
    readonly_fields = ("user", "title", "content_length")

    # 分页管理
    list_per_page = 5
    list_max_show_all = 10

    # 添加排序
    ordering = ["id"]

    # 添加过滤器
    list_filter = ["title", "user__username"]

    # 添加搜索框
    search_fields = ["title", "user__username"]

    # 指定显示列
    list_display = ("title", "content", "is_online", "user", "created_time", "topic_is_online", "topic_content")

    # # 指定不展示列
    # exclude = ["content"]

    # 添加动作
    actions = ["topic_online", "topic_offline"]

    def content_length(self, obj):
        """
        该函数返回话题内容长度，该返回属性为只读属性不可修改
        :param obj:
        :return:
        """
        return len(obj.content)

    content_length.short_description = "话题内容长度"

    def save_model(self, request, obj, form, change):
        """
        该函数允许用户操作数据保存前后做一些自定义的操作内容
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        if change and "is_online" in form.changed_data and not obj.is_online:
            self.message_user(request, "Topic: {} 被管理员删除了".format(obj.id))
            obj.title = "{}({})".format(obj.title, "管理员删除")
            super(TopicAdmin, self).save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     """
    #     该函数可以限制返回数据的内容
    #     :param request:
    #     :return:
    #     """
    #     return self.model._default_manager.filter(title__contains="first")

    def topic_is_online(self, obj):
        """
        展示列不仅可以接受属性，也可以接受函数
        :param obj:
        :return:
        """
        return "是" if obj.is_online else "否"

    topic_is_online.short_description = "话题是否在线"

    def topic_content(self, obj):
        return obj.content[:30]

    topic_content.short_description = "话题内容"

    def topic_online(self, request, queryset):
        """
        批量上线
        :param request:
        :param queryset:
        :return:
        """
        rows_updated = queryset.update(is_online=True)
        self.message_user(request, "{} topic online".format(rows_updated))

    # 添加功能描述
    topic_online.short_description = "上线所选的{}".format(Topic._meta.verbose_name)

    def topic_offline(self, request, queryset):
        """
        批量下线
        :param request:
        :param queryset:
        :return:
        """
        rows_updated = queryset.update(is_online=False)
        self.message_user(request, "{} topic offline".format(rows_updated))

    # 添加下线动作描述
    topic_offline.short_description = "下线所选的{}".format(Topic._meta.verbose_name)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
