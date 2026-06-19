from django.contrib import admin

from homepage import models


class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(*args, **kwargs):
        return False

    def has_delete_permission(*args, **kwargs):
        return False

    def has_change_permission(*args, **kwargs):
        return False

admin.site.register(models.GuestbookEntry)
admin.site.register(models.InboundWebmention, ReadOnlyAdmin)
admin.site.register(models.InboundWebmentionContent, ReadOnlyAdmin)
