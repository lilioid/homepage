from http import HTTPStatus

import markdown
from django.http import HttpRequest, HttpResponseBase
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import TemplateView, View

from homepage.blog import models


class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        categories = models.Category.objects.all()

        ctx = super().get_context_data(**kwargs)
        ctx.update({"categories": categories})
        return ctx


class CategoryIndexView(TemplateView):
    template_name = "blog/category_index.html"

    def get_context_data(self, category: str, **kwargs):
        category = get_object_or_404(models.Category.objects.prefetch_related("posts"), tag=category)

        ctx = super().get_context_data(**kwargs)
        ctx.update({"category": category})
        return ctx


class PostView(View):
    def get(self, request: HttpRequest, category: str, post: str) -> HttpResponseBase:
        post = get_object_or_404(
            models.Post.objects.select_related("markdownpost", "templatepost", "category"),
            category__tag=category,
            slug=post,
        )

        if hasattr(post, "markdownpost"):
            return self.render_markdown_post(request, post.markdownpost)
        elif hasattr(post, "templatepost"):
            return self.render_template_post(request, post.templatepost)
        else:
            raise Exception("post object is neither template nor markdown, cannot render")

    def render_template_post(self, request: HttpRequest, post: models.TemplatePost) -> HttpResponseBase:
        pass

    def render_markdown_post(self, request: HttpRequest, post: models.MarkdownPost) -> HttpResponseBase:
        ctx = {
            "post": post,
            "rendered_text": markdown.markdown(
                text=post.text,
                extensions=[
                    "nl2br",
                    "toc",
                    "attr_list",
                    "fenced_code",
                    "tables",
                ],
            ),
        }
        return TemplateResponse(
            request=request,
            template="blog/markdown_post.html",
            context=ctx,
            status=HTTPStatus.OK,
        )
