import logging
from dataclasses import dataclass
from typing import Tuple

from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment, pass_context
from jinja2.runtime import Context

from . import blog, markdown

logger = logging.getLogger(__name__)


@dataclass
class Friend:
    name: str
    homepage: str


FRIENDS = [
    Friend("bonsaibeef.de", "https://bonsaibeef.de"),
    Friend("Freddy", "https://frederico.info/"),
    Friend("Helena", "https://helena.place/"),
    Friend("kritzl", "https://kritzl.dev/"),
    Friend("Noah Fust", "https://noahfuhst.de/"),
    Friend("olebit", "https://oleb.it/"),
    Friend("traumweh", "https://traumweh.dev/"),
    Friend("Vic Wrobel", "https://www.vicwrobel.de/"),
    Friend("Markus", "https://weboverflow.de/"),
]


def split_cmd(cmd: str) -> Tuple[str, str]:
    arg0 = cmd.split(" ")[0]
    argv = cmd[len(arg0) + 1 :]
    return arg0, argv


def urlsafe_title(value: str) -> str:
    return (
        value.lower()
        .replace("_", "-")
        .replace(" ", "-")
        .replace("?", "")
        .replace("&", "")
        .replace("/", "-")
        .replace("(", "")
        .replace(")", "")
        .replace("!", "")
    )


@pass_context
def render_blog_post(ctx: Context, post: blog.Post) -> str:
    logger.info("Rendering blog post %s", post.ref)
    content_template = ctx.environment.from_string(post.raw_body)
    rendered_content = content_template.render()
    rendered_content = markdown.render(rendered_content)
    return rendered_content


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "homepage": {
                "split_cmd": split_cmd,
                "friends": sorted(FRIENDS, key=lambda i: i.name),
                "render_blog_post": render_blog_post,
            },
        }
    )
    env.filters.update({"urlsafe_title": urlsafe_title})
    return env
