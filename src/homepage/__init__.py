__version__ = "2.0.0"
__author__ = "Finn Sell (ftsell)"

from pathlib import Path

from fastapi.templating import Jinja2Templates

from . import friends

BASE_DIR = Path(__file__).parent.parent.parent
SRC_DIR = BASE_DIR / "src" / "homepage"
STATIC_DIR = SRC_DIR / "static"
TEMPLATE_DIR = SRC_DIR / "templates"

templates = Jinja2Templates(directory=TEMPLATE_DIR, context_processors=[friends.context_processor])
