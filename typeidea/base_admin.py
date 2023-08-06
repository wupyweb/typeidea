from typing import Any

from django.contrib import admin
from django.http import HttpRequest
from django.db.models.query import QuerySet


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1.自动补充owner
    2.过滤当前用户的数据
    """

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)