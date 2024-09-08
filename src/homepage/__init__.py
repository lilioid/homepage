"""
Personal homepage server of Finn Sell (dev@ftsell.de)
"""

from pathlib import Path

from fastapi.templating import Jinja2Templates

from . import friends

SRC_DIR = Path(__file__).parent
STATIC_DIR = SRC_DIR / "static"
TEMPLATE_DIR = SRC_DIR / "templates"

templates = Jinja2Templates(
    directory=TEMPLATE_DIR,
    context_processors=[friends.context_processor],
)
