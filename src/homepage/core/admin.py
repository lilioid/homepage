from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

admin.site.register(models.CustomUser, UserAdmin)
admin.site.login_template = "core/login.html"
