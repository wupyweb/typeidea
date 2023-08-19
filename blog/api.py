from typing import List
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Schema, ModelSchema, Field, Router

from .models import Post, Category, Tag

router = Router()


class PostOut(ModelSchema):
    """
    generate a schema from models.
    """
    category: str = Field(None, alias="category.name")
    tag: List[str] = Field(None, alias="tags.all")
    owner: str = Field(None, alias="owner.username")

    class Config:
        model = Post
        model_fields = ["id", "title", "category", "desc", "content", "tag", "owner", "created_time"]


@router.get("/posts", response=List[PostOut])
def get_posts(request):
    """
    Get post list.
    """
    qs = Post.objects.all().prefetch_related("category", "tag", "owner")
    from django.db import connection
    print(connection.queries)
    return qs


@router.post("/posts/{post_id}", response=PostOut)
def get_post(request, post_id: int):
    """
    get single post.
    """
    post = get_object_or_404(Post, pk=post_id)
    return post
