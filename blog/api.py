from typing import List
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Schema, ModelSchema, Field, Router
from ninja.pagination import paginate

from .models import Post, Category, Tag

router = Router()


class PostOut(ModelSchema):
    """
    generate a schema from models.
    use alias/resolver to override field. (https://django-ninja.rest-framework.com/guides/response/)
    """
    category: str = Field(None, alias="category.name")
    tag: List[str]
    owner: str = Field(None, alias="owner.username")

    @staticmethod
    def resolve_tag(obj):
        return [t.name for t in obj.tag.all()]

    class Config:
        model = Post
        model_fields = ["id", "title", "category", "desc", "content", "tag", "owner", "created_time"]


@router.get("/posts", response=List[PostOut])
@paginate   # 分页，后续可以考虑加上前一页和下一页的字段，值为url
def get_posts(request):
    """
    Get post list.
    """
    qs = Post.objects.all().prefetch_related("category", "tag", "owner").order_by("created_time")
    return qs


@router.get("/posts/{post_id}", response=PostOut)
def get_post(request, post_id: int):
    """
    get single post.
    """
    post = get_object_or_404(Post, pk=post_id)
    return post
