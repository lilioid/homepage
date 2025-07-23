"""
URL configuration for homepage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.urls import include, path, re_path

from . import views

urlpatterns = list(
    filter(
        lambda i: i is not None,
        [
            # static pages
            path("index.html", views.home, name="home"),
            path("cv.html", views.cv, name="cv"),
            path("legal.html", views.legal, name="legal"),
            path("projects.html", views.projects, name="projects"),
            # blog
            path("blog/index.html", views.blog_index, name="blog-index"),
            path("blog/tag-index.html", views.blog_tag_index, name="blog-tag-index"),
            path("blog/lang-index.html", views.blog_lang_index, name="blog-lang-index"),
            path("blog/<slug:article_ref>.html", views.blog_article, name="blog-article"),
            path("blog/<slug:article_ref>", views.blog_article),
            path("blog/feed.xml", views.RssFeed(), name="rss-feed"),
            path("blog/feed.atom", views.AtomFeed(), name="atom-feed"),
            # DEBUG only paths
            path("__reload__/", include("django_browser_reload.urls")) if settings.DEBUG else None,
            path("", include(debug_toolbar_urls(prefix="__debug__"))),
            # fallbacks which redirect to ./index.html
            re_path(r"^.+/$", views.redirect_to_index_html),
            path("", views.redirect_to_index_html),
        ],
    )
)
