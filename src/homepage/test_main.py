import logging
import re

from bs4 import BeautifulSoup
from fastapi.routing import APIRoute
from fastapi.testclient import TestClient

from .main import app

logger = logging.getLogger(__name__)
client = TestClient(app)

SITE_ROUTES = [route.path for route in app.routes if isinstance(route, APIRoute) and "site" in route.tags]


def test_internal_links():
    """Validate that internal links are actually resolvable and don't generate 404s"""
    for url in SITE_ROUTES:
        logger.info(f"Testing site {url}")
        response = client.get(url)
        soup = BeautifulSoup(response.content, features="html.parser")
        for anchor in soup.find_all(name="a"):
            if "external" not in anchor.attrs.get("rel", []):
                href = anchor.attrs["href"]
                logger.info(f"Validating internal link to {href}")
                response = client.get(href, follow_redirects=True)
                assert response.status_code == 200, f"response for {href} was not OK"


def test_external_links():
    """Validate that all links starting with https:// are also marked as external"""
    for url in SITE_ROUTES:
        logger.info(f"Testing site {url}")
        response = client.get(url)
        soup = BeautifulSoup(response.content, features="html.parser")
        for anchor in soup.find_all(name="a"):
            href = str(anchor.attrs["href"])
            if re.match(r"https?://", href):
                logger.info(f"Validating link to {href}")
                assert "external" in anchor.attrs.get(
                    "rel", []
                ), f"external link to {href} on site {url} does not have rel=external attribute"
