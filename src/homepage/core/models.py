import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom Mafiasi User Model.
    It is not really used right now but since it is best practice to use one we have it.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Friend(models.Model):
    display_name = models.CharField(max_length=32)
    url = models.URLField(max_length=64)
    is_shown = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_name"]

    def __str__(self):
        return self.display_name
