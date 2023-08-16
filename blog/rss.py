from typing import Any, Dict
from xml.sax import ContentHandler
from django.contrib.syndication.views import Feed
from django.db.models.base import Model
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed

from .models import Post


class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler: ContentHandler, item: Dict[str, Any]) -> None:
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement("content:html", item["content_html"])


class LatestPostsFeed(Feed):
    feed_type = Rss201rev2Feed
    title = "Blog"
    link = "/rss/"
    description = "Latest blog posts"

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)[:5]
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc

    def item_link(self, item):
        return reverse("post-detail", args=[item.pk])
    
    def item_extra_kwargs(self, item: Model) -> Dict[Any, Any]:
        return {"content_html": self.item_content_html(item)}
    
    def item_content_html(self, item: Model) -> str:
        return item.content_html

