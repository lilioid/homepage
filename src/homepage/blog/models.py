from django.db import models


class Category(models.Model):
    """
    A category into which posts can be organized
    """

    name = models.CharField(max_length=32)
    tag = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Basic post data

    Not valid on its own since it does not contain any content.
    The content is held by one of the derived models instead.
    """

    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    category = models.ForeignKey(to="Category", on_delete=models.SET_NULL, related_name="posts", null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class MarkdownPost(Post):
    """
    A post that has its content stored as markdown in the database.
    """

    text = models.TextField()


class TemplatePost(Post):
    """
    A post that renders a django template as its content.
    """

    template_name = models.CharField(max_length=128)
