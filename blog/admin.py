from typing import Any
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blog.models import Post, Category, Tag
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
        "is_nav",
        "created_time",
        "post_count",
    )
    fields = (
        "name",
        "status",
        "is_nav",
    )

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = "文章数量"

    # 重写ModelAdmin的save_model方法，把数据保存到数据库中
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
        "created_time",
    )
    fields = (
        "name",
        "status",
    )

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title", "category", "status",
        "created_time", "operator",
    )
    list_display_links = []
    list_filter = ("category",)
    search_fields = ("title", "category__name")

    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True

    fields = (
        ("category", "title"),
        "desc",
        "status",
        "content",
        "tag",
    )

    def operator(self, obj):
        return format_html(
            "<a href='{}'>编辑</a>",
            reverse("admin:blog_post_change", args=(obj.id,))
        )
    operator.short_description = "操作"

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)