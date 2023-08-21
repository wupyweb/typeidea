"""
URL configuration for typeidea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps import views as sitemap_views
from django.conf.urls.static import static

from typeidea.custom_site import custom_site
from blog.views import (
    post_list, post_detail, PostDetailView, 
    PostListView, IndexView, CategoryView, 
    TagView, SearchView, AuthorView
)
from config.views import LinkListView
from comment.views import CommentView
from blog.rss import LatestPostsFeed
from blog.sitemap import PostSitemap

from typeidea.api import api

# from config.views import links

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("admin/", custom_site.urls),

    path("", IndexView.as_view(), name="index"),
    path("category/<int:category_id>/", CategoryView.as_view(), name="category-list"),
    path("tag/<int:tag_id>/", TagView.as_view(), name="tag-list"),
    path("post/<int:post_id>.html", PostDetailView.as_view(), name="post-detail"),   #pk,主键查询
    path("search/", SearchView.as_view(), name="search"),
    path("author/<int:owner_id>/", AuthorView.as_view(), name="author"),
    path("links/", LinkListView.as_view(), name="links"),
    path("comment/", CommentView.as_view(), name="comment"),
    path("rss/", LatestPostsFeed(), name="rss"),
    path("sitemap.xml", sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    path("ckeditor/", include('ckeditor_uploader.urls')),

    path("api/", api.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('silk/', include('silk.urls', namespace='silk')),
    ] + urlpatterns