from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from blog.models import Post, Category, Tag
from blog.adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.

# class PostInline(admin.TabularInline):
#     fields = ("title", "desc")
#     extra =1
#     model = Post


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = (PostInline, )
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
class TagAdmin(BaseOwnerAdmin):
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


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器，只展示当前用户分类"""

    title = "分类过滤器"
    parameter_name = "owner_category"

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return Category.objects.filter(owner=request.user).values_list("id", "name")
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset
    

@admin.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = (
        "title", "category", "status",
        "created_time", "operator", "owner"
    )
    fieldsets = (
        (
            "基础配置", 
            {
                "description": "基础配置描述",
                "fields": (
                    ("title", "category"),
                    "status",
                )
            }
        ),
        (
            "内容",
            {
                "fields": (
                    "desc",
                    "content",
                )
            }
        ),
        (
            "额外信息",
            {
                "classes": ("collapse",),
                "fields": ("tag",),
            }
        )
    )
    # filter_horizontal = ("tag",)
    list_display_links = []
    list_filter = (CategoryOwnerFilter,)
    search_fields = ("title", "category__name")

    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True

    # fields = (
    #     ("category", "title"),
    #     "desc",
    #     "status",
    #     "content",
    #     "tag",
    # )

    def operator(self, obj):
        return format_html(
            "<a href='{}'>编辑</a>",
            reverse("admin:blog_post_change", args=(obj.id,))
        )
    operator.short_description = "操作"

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)
    
    # class Media:
    #     css = {
    #         "all": ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
    #     }
    #     js = ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js",)



@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "object_repr", "object_id", "action_flag", "user",
        "change_message",
    )