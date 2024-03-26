import re

import pytest
from bs4 import BeautifulSoup
from fastapi import APIRouter
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

SITE_ROUTES = [
    route.path
    for mount in app.routes
    if isinstance(mount.app, APIRouter)
    for route in mount.routes
    if "site" in route.tags
]


def test_internal_links():
    for url in SITE_ROUTES:
        response = client.get(url)
        soup = BeautifulSoup(response.content, features="html.parser")
        for anchor in soup.find_all(name="a"):
            if "external" not in anchor.attrs.get("rel", []):
                href = anchor.attrs["href"]
                response = client.get(href, follow_redirects=True)
                assert response.status_code == 200, f"response for {href} was not OK"


def test_external_links():
    for url in SITE_ROUTES:
        response = client.get(url)
        soup = BeautifulSoup(response.content, features="html.parser")
        for anchor in soup.find_all(name="a"):
            href = str(anchor.attrs["href"])
            if re.match(r"https?://", href):
                assert "external" in anchor.attrs.get(
                    "rel", []
                ), f"external link to {href} on site {url} does not have rel=external attribute"
