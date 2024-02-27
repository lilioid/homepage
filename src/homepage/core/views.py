from pathlib import Path

from django.contrib.staticfiles import finders
from django.http import (
    FileResponse,
    HttpRequest,
    HttpResponseBase,
    HttpResponseNotFound,
)
from django.template.loader import render_to_string
from django.urls import Resolver404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, never_cache
from django.views.generic import TemplateView, View

MINUTE = 60


@method_decorator(cache_control(max_age=60 * MINUTE), name="get")
class RobotsView(View):
    def get(self, _request: HttpRequest) -> HttpResponseBase:
        file = finders.find("core/assets/robots.txt")
        return FileResponse(open(file, "rb"))


@never_cache
def not_found_view(request: HttpRequest, exception: Resolver404) -> HttpResponseNotFound:
    if request.accepts("text/html"):
        content = render_to_string("core/views/404.html", context=None, request=request)
        return HttpResponseNotFound(content=content.encode("UTF-8"), content_type="text/html")

    return HttpResponseNotFound(content="Not Found")


@method_decorator(cache_control(max_age=10 * MINUTE), name="get")
class HomeView(TemplateView):
    template_name = "core/views/index.html"


@method_decorator(cache_control(max_age=10 * MINUTE), name="get")
class ProjectsView(TemplateView):
    template_name = "core/views/projects.html"
