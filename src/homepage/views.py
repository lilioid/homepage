from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.cache import cache_control

from . import blog

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
    return render(request, "homepage/cv.html")


@cache_control(**CACHE_ARGS_STATIC)
def legal(request: HttpRequest) -> HttpResponse:
    return render(request, "homepage/legal.html")


@cache_control(**CACHE_ARGS_STATIC)
def projects(request: HttpRequest) -> HttpResponse:
    return render(request, "homepage/projects.html")


@cache_control(**CACHE_ARGS_BLOG)
async def blog_index(request: HttpRequest) -> HttpResponse:
    post_collection = await blog.BlogCollection.get_instance()

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
            "post_collection": post_collection,
        },
    )


@cache_control(**CACHE_ARGS_BLOG)
async def blog_tag_index(request: HttpRequest) -> HttpResponse:
    post_collection = await blog.BlogCollection.get_instance()

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
            "tags": tags,
        },
    )


@cache_control(**CACHE_ARGS_BLOG)
async def blog_lang_index(request: HttpRequest) -> HttpResponse:
    post_collection = await blog.BlogCollection.get_instance()

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
            "langs": langs,
        },
    )


@cache_control(**CACHE_ARGS_BLOG)
async def blog_article(request: HttpRequest, article_ref: str) -> HttpResponse:
    post_collection = await blog.BlogCollection.get_instance()
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
            "post": post,
        },
    )
