from django.db import models


class Webmention(models.Model):
    pk = models.CompositePrimaryKey("own_path", "href", "page_hash")
    own_path = models.CharField(max_length=256)
    href = models.CharField(max_length=256)
    page_hash = models.BinaryField()
    first_seen_at = models.DateTimeField(auto_now_add=True)
    webmention_sent = models.BooleanField(default=False)
