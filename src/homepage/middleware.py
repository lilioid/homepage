from typing import Awaitable, Callable

from asgiref.sync import markcoroutinefunction
from bs4 import BeautifulSoup
from django.http import HttpRequest, HttpResponse


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
            soup = BeautifulSoup(response.content)
            for anchor_elem in soup.find_all("a"):
                if "rel" in anchor_elem.attrs or "href" not in anchor_elem.attrs:
                    continue

                href = anchor_elem.attrs["href"]
                if self.is_external_href(request, href):
                    anchor_elem.attrs["rel"] = "noopener nofollow external"
                if self.is_current_page(request, href):
                    anchor_elem.attrs["aria-current"] = "page"

            response.content = soup.prettify(formatter="html5").encode("UTF-8")

        return response
