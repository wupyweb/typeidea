from typing import Any
from django.contrib import admin

from config.models import Link, SideBar

# Register your models here.

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "href",
        "status",
        "weight",
        "created_time",
    )
    fields = (
        "title",
        "href",
        "status",
        "weight",
    )

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)

@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "display_type",
        "content",
        "created_time",
    )
    fields = (
        "title",
        "display_type",
        "content",
    )

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)