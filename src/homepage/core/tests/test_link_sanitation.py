import re

from bs4 import BeautifulSoup
from django.test.client import Client
from django.urls import reverse

STATIC_URLS = [
    "index",
    "projects",
]


def test_static_urls_are_resolvable(client: Client):
    for url_name in STATIC_URLS:
        response = client.get(reverse(url_name), follow=True)
        assert response.status_code == 200
        assert response.headers["Content-Type"].startswith("text/html")


def test_static_urls_internal_links_are_valid(client: Client):
    for url_name in STATIC_URLS:
        response = client.get(reverse(url_name), follow=True)
        soup = BeautifulSoup(response.content, "html.parser")
        for anchor in soup.find_all(name="a"):
            if "external" not in anchor.attrs.get("rel", []):
                href = anchor.attrs["href"]
                response = client.get(href, follow=True)
                assert response.status_code == 200, f"response for {href} was not OK"


def test_static_urls_external_links_are_marked(client: Client):
    for url_name in STATIC_URLS:
        response = client.get(reverse(url_name), follow=True)
        soup = BeautifulSoup(response.content, "html.parser")
        for anchor in soup.find_all(name="a"):
            href = str(anchor.attrs["href"])
            if re.match(r"https?://", href):
                assert "external" in anchor.attrs.get(
                    "rel", []
                ), f"external link to {href} on site {url_name} does not have rel=external attribute"
