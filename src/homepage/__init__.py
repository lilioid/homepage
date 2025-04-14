"""
Personal homepage server of Lilly (li@lly.sh)
"""

from pathlib import Path

CANONICAL_HOST = "li.lly.sh"
SRC_DIR = Path(__file__).parent
PROJECT_DIR = SRC_DIR.parent.parent
STATIC_DIR = SRC_DIR / "static"
TEMPLATE_DIR = SRC_DIR / "templates"
