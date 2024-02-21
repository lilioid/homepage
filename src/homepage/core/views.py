from pathlib import Path

from django.http import (
    FileResponse,
    HttpRequest,
    HttpResponseBase,
    HttpResponseNotFound,
)
from django.template.loader import render_to_string
from django.urls import Resolver404
from django.views.generic import TemplateView, View

ASSET_DIR = Path(__file__).parent / "static" / "core" / "assets"


class RobotsView(View):
    def get(self, _request: HttpRequest) -> HttpResponseBase:
        return FileResponse(open(ASSET_DIR / "robots.txt", "rb"))


def not_found_view(request: HttpRequest, exception: Resolver404) -> HttpResponseNotFound:
    if request.accepts("text/html"):
        content = render_to_string("core/views/404.html", context=None, request=request)
        return HttpResponseNotFound(content=content.encode("UTF-8"), content_type="text/html")

    return HttpResponseNotFound(content="Not Found")


class HomeView(TemplateView):
    template_name = "core/views/index.html"


class ProjectsView(TemplateView):
    template_name = "core/views/projects.html"
