from django.contrib import admin

from . import models

admin.site.register(models.Category)


@admin.register(models.TemplatePost)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ["title", "category", "published", "created_at"]
    list_filter = ["category"]
    radio_fields = {"category": admin.VERTICAL}
    search_fields = ["title"]
    search_help_text = "Search for post by title"


@admin.register(models.MarkdownPost)
class MarkdownPostAdmin(PostAdmin):
    search_fields = ["title", "text"]
    search_help_text = "Search for post by title or content"
