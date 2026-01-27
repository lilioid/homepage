from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from datetime import datetime

from . import blog


class BlogSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return blog.BlogCollection.get_instance().posts

    def location(self, item: blog.Post):
        return reverse("blog-article", args=[item.ref])

    def lastmod(self, item: blog.Post) -> datetime:
        return item.last_modified
    

class StaticSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return [ "home", "cv", "legal", "projects", "blog-index", ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item in [ "home", "projects" ]:
            return 0.6
        elif item in [ "blog-index" ]:
            return 0.5
        else:
            return 0.4


sitemaps = {
    "static": StaticSitemap,
    "blog": BlogSitemap,
}

