from typing import Any, Dict

from fastapi import Request
from fastapi.templating import Jinja2Templates

from . import CANONICAL_HOST, TEMPLATE_DIR, antinazi, friends


def app_context(request: Request) -> Dict[str, Any]:
    return {
        "canonical_host": CANONICAL_HOST,
    }


templates = Jinja2Templates(
    directory=TEMPLATE_DIR,
    context_processors=[app_context, friends.context_processor, antinazi.context_processor],
)
