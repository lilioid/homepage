import logging
import random
from dataclasses import dataclass
from datetime import datetime
from typing import Tuple

from django.templatetags.static import static
from django.urls import reverse
from django.utils import timezone
from jinja2 import Environment, pass_context
from jinja2.runtime import Context

from . import blog, markdown

logger = logging.getLogger(__name__)


@dataclass
class Event:
    name: str
    start: datetime
    end: datetime


EVENTS = [
    Event(
        "why2025",
        datetime(2025, 8, 1),
        datetime(2025, 8, 13),
    ),
    Event(
        "ef29",
        datetime(2025, 8, 31),
        datetime(2025, 9, 7),
    ),
    Event(
        "39c3",
        datetime(2025, 12, 16),
        datetime(2025, 12, 31),
    ),
]


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
    Friend("rhandos", "https://rhandos.xyz/"),
    Friend("tessa", "https://tessa.dog/"),
    Friend("bitwhisker", "https://bitwhisker.de/"),
    Friend("hammi", "https://hammi.jetzt"),
]


def split_cmd(cmd: str) -> Tuple[str, str]:
    arg0 = cmd.split(" ")[0]
    argv = cmd[len(arg0) + 1:]
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


def dateformat(dt: datetime) -> str:
    return dt.strftime("%d.%m.%Y %H:%M")


def get_political_message() -> str:
    MSGS = [
        "Du bist die Brandmauer gegen Rechts",
        "„Unpolitisch“ ist politisch",
        "Die AfD ist die mit Abstand größte Gefahr für unsere Gesellschaft! #AfDVerbotJetzt",
        "Sich an Antifaschismus stören ist so 1933",
        "Diese Website wird nicht von Faschisten betrieben",
        "Menschenrechte statt rechte Menschen",
        "Kein Mensch ist illegal",
        "„Nie wieder“ ist immer, nicht nur alle 4 Jahre beim Kreuzchen machen",
        "Kein Platz für Rassismus",
        "Trans rights are human rights",
        "Trans rights or riot nights",
        "AfDler verpisst euch – keiner vermisst euch",
        "Seenotrettung ist kein Verbrechen",
    ]

    return random.choice(MSGS)


def get_active_festival() -> str | None:
    now = timezone.now()
    for i in EVENTS:
        if timezone.make_aware(i.start) <= now <= timezone.make_aware(i.end):
            return i.name

    return None


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "homepage": {
                "festival_mode": get_active_festival(),
                "split_cmd": split_cmd,
                "friends": sorted(FRIENDS, key=lambda i: i.name),
                "render_blog_post": render_blog_post,
                "get_political_message": get_political_message,
            },
        }
    )
    env.filters.update(
        {
            "urlsafe_title": urlsafe_title,
            "dateformat": dateformat,
        }
    )
    return env
