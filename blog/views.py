from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q

from blog.models import Post, Tag, Category
from comment.forms import CommentForm
from comment.models import Comment
from config.models import SideBar

# Create your views here.
def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()
    
    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SideBar.get_all(),
    }
    # 是否导航
    context.update(Category.get_navs())
    return render(request, "blog/list.html", context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        "post": post,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, "blog/detail.html", context=context)


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "sidebars": SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context


class IndexView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    template_name = "blog/list.html"
    context_object_name = "post_list"
    paginate_by = 5


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get("category_id")
        context.update({
            "category": get_object_or_404(Category, pk=category_id)
        })
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get("category_id")
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "tag": get_object_or_404(Tag, pk=self.kwargs.get("tag_id"))
        })
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(tag__id=self.kwargs.get("tag_id"))
    

class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.latest_posts()
    template_name = "blog/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update({
    #         "comment_form": CommentForm,
    #         "comment_list": Comment.get_by_target(self.request.path)
    #     })
    #     return context


class PostListView(ListView):
    model = Post
    template_name = "blog/list.html"
    context_object_name = "post_list"
    paginate_by = 1


class SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "keyword": self.request.GET.get("keyword", "")
        })
        print("search: 1 step")
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get("keyword", "")
        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))
        print("search: 2 step")
        return queryset
    

class AuthorView(IndexView):
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(owner_id=self.kwargs["owner_id"])