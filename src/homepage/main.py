#!/usr/bin/env python3
import argparse
import asyncio
import logging
import sys

import colorama
from colorama import Back, Fore, Style
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from hypercorn import Config as HypercornConfig
from hypercorn.asyncio import serve as hypercorn_serve
from starlette.datastructures import URL

from homepage import STATIC_DIR, blog, templates, views, well_known

app = FastAPI(openapi_url=None)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(views.router)
app.include_router(blog.router)
app.include_router(well_known.router)


@app.exception_handler(404)
async def handle404(request: Request, _exception) -> HTMLResponse:
    return templates.TemplateResponse(request, name="404.html", status_code=404)


@app.middleware("http")
async def add_cache_headers(request: Request, call_next) -> Response:
    args = request.app.state.args
    response = await call_next(request)  # type: Response

    if args.dev:
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
        "default-src 'self'; "
        + "style-src 'self' 'unsafe-inline'; "
        + "script-src 'self' 'unsafe-inline'; "
        + "frame-src ftsell.de; "
        + "connect-src wss://ftsell.de;",
    )
    response.headers.setdefault("X-Xss-Protection", "1; mode=block")
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Cross-Origin-Opener-Policy", "same-origin")
    return response


@app.middleware("http")
async def redirect_to_canonical_host(request: Request, call_next) -> Response:
    if request.url.hostname in [
        "ftsell.de",
        "www.ftsell.de",
        "www.finn-thorben.me",
        "finn-thorben.me",
        "lly.sh",
    ]:
        return RedirectResponse(URL(f"https://li.lly.sh{request.url.path}?{request.url.query}"))
    else:
        return await call_next(request)


def main() -> int:
    colorama.init()
    argp = argparse.ArgumentParser(prog="homepage", description="Lillys personal homepage")
    argp.add_argument(
        "--dev", default=False, action="store_true", help="Enable development mode (which reduces caching)"
    )
    argp.add_argument("--bind", default="localhost:8000", help="Which address:port to bind to")
    args = argp.parse_args()

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
    logger.setLevel(logging.DEBUG if args.dev else logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        DynFormatter(fmt="%(asctime)s - %(levelname)s (%(name)s): %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    )
    logger.addHandler(handler)

    # run webserver
    app.state.args = args
    asyncio.run(
        hypercorn_serve(
            app,
            HypercornConfig.from_mapping(
                bind=args.bind,
                accesslog=logging.getLogger("http.request"),
                errorlog=logging.getLogger("http.error"),
            ),
        )
    )


if __name__ == "__main__":
    sys.exit(main())
