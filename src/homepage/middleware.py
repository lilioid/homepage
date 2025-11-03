import logging
from typing import Awaitable, Callable

from asgiref.sync import markcoroutinefunction
from bs4 import BeautifulSoup
from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

logger = logging.getLogger(__name__)


class FixHtmlMiddleware:
    sync_capable = False
    async_capable = True

    def __init__(self, get_response: Callable[[HttpRequest], Awaitable[HttpResponse]]):
        self.get_response = get_response
        markcoroutinefunction(self)

    def is_external_href(self, request: HttpRequest, href: str) -> bool:
        is_internal = (
            href.startswith("/")
            or href.startswith("./")
            or href.startswith("#")
            or href.startswith("?")
            or href.startswith(f"{request.scheme}://{request.get_host()}/")
            or href == ""
        )
        return not is_internal

    def is_current_page(self, request: HttpRequest, href: str) -> bool:
        return request.path == href

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        response = await self.get_response(request)

        if response.headers.get("Content-Type", default="text/plain").startswith("text/html"):
            soup = BeautifulSoup(response.content, features="html.parser")
            for anchor_elem in soup.find_all("a"):
                if "rel" in anchor_elem.attrs or "href" not in anchor_elem.attrs:
                    continue

                href = anchor_elem.attrs["href"]
                if self.is_external_href(request, href):
                    anchor_elem.attrs["rel"] = "noopener nofollow external"
                if self.is_current_page(request, href):
                    anchor_elem.attrs["aria-current"] = "page"

            response.content = soup.encode(formatter="html5")

        return response


class CanonicalHostMiddleware:
    sync_capable = False
    async_capable = True

    def __init__(self, get_response: Callable[[HttpRequest], Awaitable[HttpResponse]]):
        self.get_response = get_response
        markcoroutinefunction(self)

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        if request.get_host() != settings.BASE_URI.netloc:
            target = f"//{settings.BASE_URI.netloc}{request.get_full_path()}"
            logger.info(f"Redirecting request from {request.get_host()} to canonical host {settings.BASE_URI.netloc}")
            return HttpResponseRedirect(redirect_to=target)

        return await self.get_response(request)
