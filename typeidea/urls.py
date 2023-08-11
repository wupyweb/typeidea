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
from django.contrib import admin
from django.urls import path

from typeidea.custom_site import custom_site
from blog.views import post_list, post_detail, PostDetailView, PostListView, IndexView, CategoryView, TagView
# from config.views import links

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("admin/", custom_site.urls),

    path("", IndexView.as_view(), name="index"),
    path("category/<int:category_id>/", CategoryView.as_view(), name="category-list"),
    path("tag/<int:tag_id>/", TagView.as_view(), name="tag-list"),
    path("post/<int:post_id>.html", PostDetailView.as_view(), name="post-detail"),   #pk,主键查询
    # path("links/", links, name="links"),
]
