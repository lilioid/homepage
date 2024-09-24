#!/usr/bin/env python3
import asyncio
import logging
import sys
from contextlib import asynccontextmanager

import colorama
from colorama import Back, Fore, Style
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from hypercorn import Config as HypercornConfig
from hypercorn.asyncio import serve as hypercorn_serve
from starlette.datastructures import URL

from homepage import STATIC_DIR, blog, templates, views, well_known
from homepage.settings import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    if app.state.settings is None:
        app.state.settings = Settings.from_env()
    yield


app = FastAPI(openapi_url=None, lifespan=lifespan)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(views.router)
app.include_router(blog.router)
app.include_router(well_known.router)


@app.exception_handler(404)
async def handle404(request: Request, _exception) -> HTMLResponse:
    return templates.TemplateResponse(request, name="404.html", status_code=404)


@app.middleware("http")
async def add_cache_headers(request: Request, call_next) -> Response:
    settings = Settings.from_request(request)
    response = await call_next(request)  # type: Response

    if settings.DEV_MODE:
        return response

    if request.url.path.startswith("/static/assets"):
        FRESH_TIME = 24 * 60 * 60  # 1 day
        STALE_TIME = 30 * 60 * 60 * 24  # 30 days
        response.headers.setdefault(
            "Cache-Control",
            f"max-age={FRESH_TIME}, stale-while-revalidate={STALE_TIME}, stale-if-error={STALE_TIME}",
        )
    else:
        FRESH_TIME = 10 * 60  # 10 minutes
        STALE_TIME = 30 * 60 * 60 * 24  # 30 days
        response.headers.setdefault(
            "Cache-Control",
            f"max-age={FRESH_TIME}, stale-if-error={STALE_TIME}",
        )
    return response


@app.middleware("http")
async def add_security_headers(request: Request, call_next) -> Response:
    response = await call_next(request)  # type: Response
    response.headers.setdefault(
        "Content-Security-Policy",
        "default-src 'self'; style-src 'self' 'unsafe-inline'; frame-src ftsell.de; connect-src wss://ftsell.de;",
    )
    response.headers.setdefault("X-Xss-Protection", "1; mode=block")
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Cross-Origin-Opener-Policy", "same-origin")
    return response


@app.middleware("http")
async def redirect_to_canonical_host(request: Request, call_next) -> Response:
    if request.url.hostname in [
        "www.ftsell.de",
        "www.finn-thorben.me",
        "finn-thorben.me",
    ]:
        return RedirectResponse(URL(f"https://ftsell.de{request.url.path}?{request.url.query}"))
    else:
        return await call_next(request)


def main() -> int:
    colorama.init()
    settings = Settings.from_argv()

    # configure logging with colored log levels
    class DynFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:
            colors = {
                logging.DEBUG: Fore.CYAN,
                logging.INFO: Fore.BLUE,
                logging.WARNING: Fore.YELLOW,
                logging.ERROR: Fore.RED,
                logging.CRITICAL: Back.RED + Fore.WHITE,
            }
            return colors[record.levelno] + super().format(record) + Style.RESET_ALL

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if settings.DEV_MODE else logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        DynFormatter(fmt="%(asctime)s - %(levelname)s (%(name)s): %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    )
    logger.addHandler(handler)

    # run webserver
    app.state.settings = settings
    asyncio.run(
        hypercorn_serve(
            app,
            HypercornConfig.from_mapping(
                bind=settings.BIND,
                accesslog=logging.getLogger("http.request"),
                errorlog=logging.getLogger("http.error"),
            ),
        )
    )


if __name__ == "__main__":
    sys.exit(main())
