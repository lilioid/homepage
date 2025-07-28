import uuid

from django.db import models


class OutboundWebmention(models.Model):
    pk = models.CompositePrimaryKey("own_path", "href")
    own_path = models.CharField(max_length=256)
    href = models.CharField(max_length=256)
    first_seen_at = models.DateTimeField(auto_now_add=True)
    webmention_sent = models.BooleanField(default=False)


class InboundWebmention(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    own_path = models.CharField(max_length=256)
    source = models.CharField(max_length=256)
    received_at = models.DateTimeField(auto_now_add=True)
    content = models.ForeignKey("InboundWebmentionContent", on_delete=models.CASCADE, null=True, default=None)


class InboundWebmentionContent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
