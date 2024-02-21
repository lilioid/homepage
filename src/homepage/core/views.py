from pathlib import Path

from django.http import FileResponse, HttpRequest, HttpResponseBase
from django.views.generic import TemplateView, View

ASSET_DIR = Path(__file__).parent / "static" / "core" / "assets"


class RobotsView(View):
    def get(self, _request: HttpRequest) -> HttpResponseBase:
        return FileResponse(open(ASSET_DIR / "robots.txt", "rb"))


class HomeView(TemplateView):
    template_name = "core/views/index.html"


class ProjectsView(TemplateView):
    template_name = "core/views/projects.html"
