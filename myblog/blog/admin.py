from django.contrib import admin
from .models import Category, Tag, Tui, Article, Link, Banner


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 显示字段内容
    list_display = ("id", "category", "title", "tui", "user", "views", "created_time")
    # 自动分页条目
    list_per_page = 50
    # 排序
    ordering = ("-created_time",)
    # 可编辑字段
    list_display_links = ("id", "title")


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "text_info", "img", "link_url", "is_active")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "index")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "linkurl")
