import json
from http import HTTPStatus
from urllib.parse import urlparse

from django import forms
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import is_valid_path, reverse, reverse_lazy
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt

from . import blog, models

CACHE_ARGS_STATIC = (
    {"no_store": True}
    if settings.DEBUG
    else {
        "max_age": 60 * 60,  # fresh for one hour
        "stale_if_error": 60 * 60 * 24 * 31,  # may reuse stale content for one month if revalidation fails
    }
)

CACHE_ARGS_BLOG = (
    {"no_store": True}
    if settings.DEBUG
    else {
        "max_age": 60 * 5,  # fresh for 5 minutes
        "stale_if_error": 60 * 60 * 24,  # may reuse stale content for one day if revalidation fails
    }
)


def redirect_to_index_html(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect(request.build_absolute_uri("./index.html"))


@cache_control(**CACHE_ARGS_STATIC)
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "homepage/index.html")


@cache_control(**CACHE_ARGS_STATIC)
def cv(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "homepage/cv.html",
        context={
            "title": "CV | Lillys Homepage",
        },
    )


@cache_control(**CACHE_ARGS_STATIC)
def legal(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "homepage/legal.html",
        context={
            "title": "Legal | Lillys Homepage",
        },
    )


@cache_control(**CACHE_ARGS_STATIC)
def projects(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "homepage/projects.html",
        context={
            "title": "Projects | Lillys Homepage",
        },
    )


@cache_control(**CACHE_ARGS_BLOG)
def blog_index(request: HttpRequest) -> HttpResponse:
    post_collection = blog.BlogCollection.get_instance()

    if "lang" in request.GET:
        post_collection.posts = [post for post in post_collection.posts if post.lang == request.GET["lang"]]

    if "tag" in request.GET:
        post_collection.posts = [post for post in post_collection.posts if request.GET["tag"] in post.tags]

    if "with_drafts" not in request.GET or request.GET["with_drafts"] == "false":
        post_collection.posts = [post for post in post_collection.posts if not post.is_draft]

    return render(
        request,
        "homepage/blog-index.html",
        context={
            "title": "Lillys Blog",
            "post_collection": post_collection,
        },
    )


@cache_control(**CACHE_ARGS_BLOG)
def blog_tag_index(request: HttpRequest) -> HttpResponse:
    post_collection = blog.BlogCollection.get_instance()

    tags = {}
    for i_tag in (i_tag for i_post in post_collection for i_tag in i_post.tags if not i_post.is_draft):
        if i_tag in tags:
            tags[i_tag] += 1
        else:
            tags[i_tag] = 1

    return render(
        request,
        "homepage/blog-tag-index.html",
        context={
            "title": "Lillys Blog",
            "tags": tags,
        },
    )


@cache_control(**CACHE_ARGS_BLOG)
def blog_lang_index(request: HttpRequest) -> HttpResponse:
    post_collection = blog.BlogCollection.get_instance()

    langs = {}
    for i_lang in (i_post.lang for i_post in post_collection if not i_post.is_draft):
        if i_lang in langs:
            langs[i_lang] += 1
        else:
            langs[i_lang] = 1

    return render(
        request,
        "homepage/blog-lang-index.html",
        context={
            "title": "Lillys Blog",
            "langs": langs,
        },
    )


@cache_control(**CACHE_ARGS_BLOG)
def blog_article(request: HttpRequest, article_ref: str) -> HttpResponse:
    post_collection = blog.BlogCollection.get_instance()
    post_id = blog.extract_post_id(article_ref)
    for post in post_collection:
        if post.id == post_id:
            post = post
            break
    else:
        raise Http404()

    if article_ref != post.ref:
        return HttpResponseRedirect(reverse("blog-article", args=[post.ref]))

    return render(
        request,
        "homepage/blog-article.html",
        context={
            "title": f"{post.title} | Lillys Blog",
            "post": post,
        },
    )


def webmention_test(request: HttpRequest) -> HttpResponse:
    return render(request, "homepage/webmention-test.html")


@csrf_exempt
async def webmention_endpoint(request: HttpRequest) -> HttpResponse:
    class WebmentionPayload(forms.Form):
        source = forms.CharField(max_length=256, strip=True)
        target = forms.CharField(max_length=256, strip=True)

        def clean_source(self):
            url = urlparse(self.data["source"])
            if url.scheme not in ["http", "https"]:
                raise forms.ValidationError("URL scheme must be http or https")

            return url

        def clean_target(self):
            url = urlparse(self.data["target"])
            if url.scheme not in ["http", "https"]:
                raise forms.ValidationError("URL scheme must be http or https")

            if not is_valid_path(url.path):
                raise forms.ValidationError("Path is not valid on this site")

            if url.netloc != settings.BASE_URI.netloc:
                raise forms.ValidationError(
                    f"Webmentions can only be sent to canonical location {settings.BASE_URI.netloc}"
                )

            return url

        def clean(self):
            if self.data["target"] == self.data["source"]:
                raise forms.ValidationError("Source and Target must not be the same")

            return super().clean()

    if request.method != "POST":
        return HttpResponse(content="Must use POST", status=HTTPStatus.METHOD_NOT_ALLOWED)

    form_data = WebmentionPayload(data=request.POST)
    if not form_data.is_valid():
        return HttpResponse(
            content=json.dumps(form_data.errors), content_type="application/json", status=HTTPStatus.BAD_REQUEST
        )

    await models.InboundWebmention.objects.acreate(
        own_path=form_data.cleaned_data["target"].path,
        source=form_data.cleaned_data["source"].geturl(),
    )
    return HttpResponse("ok")


class RssFeed(Feed):
    title = "Lillys Blog"
    link = reverse_lazy("blog-index")
    feed_type = Rss201rev2Feed

    def items(self) -> blog.BlogCollection:
        collection = blog.BlogCollection.get_instance()
        collection.posts = [i for i in collection.posts if not i.is_draft]
        return collection

    def item_link(self, item: blog.Post) -> str:
        return reverse("blog-article", args=[item.ref])

    def item_title(self, item: blog.Post) -> str:
        return item.title

    def item_description(self, item: blog.Post) -> str:
        return item.excerpt


class AtomFeed(RssFeed):
    feed_type = Atom1Feed


async def robots_txt(request: HttpRequest) -> HttpResponse:
    return render(request, "homepage/robots.txt")

