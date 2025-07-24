from django.apps import AppConfig
from django.conf import settings
from django.utils import autoreload


class HomepageConfig(AppConfig):
    name = "homepage"

    def ready(self):
        super().ready()
        autoreload.autoreload_started.connect(self.on_autoreload_ready)

    def on_autoreload_ready(self, sender: autoreload.BaseReloader, **kwargs):
        blog_dir = settings.BASE_DIR / "src" / "homepage" / "blog"
        sender.watch_dir(blog_dir, "*.md")
