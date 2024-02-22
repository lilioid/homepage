from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

admin.site.register(models.Category)
admin.site.register(models.MarkdownPost)
admin.site.register(models.TemplatePost)
