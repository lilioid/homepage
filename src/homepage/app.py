#!/usr/bin/env python3
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from starlette.datastructures import URL

import homepage.blog
import homepage.state
import homepage.views
import homepage.webmention
import homepage.well_known
from homepage import CANONICAL_HOST, STATIC_DIR
from homepage.config import AppConfig
from homepage.templates import templates


def make_app(cfg: AppConfig):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.sql_engine = homepage.state.connect_engine(cfg.db_path, debug=cfg.dev_mode)
        homepage.state.init_state(app.state.sql_engine)
        yield

    app = FastAPI(openapi_url=None, app_config=cfg, lifespan=lifespan, debug=cfg.dev_mode)
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    app.include_router(homepage.views.router)
    app.include_router(homepage.blog.router)
    app.include_router(homepage.well_known.router)
    app.include_router(homepage.webmention.router)

    @app.exception_handler(404)
    async def handle404(request: Request, _exception) -> HTMLResponse:
        return templates.TemplateResponse(request, name="404.html", status_code=404)

    @app.middleware("http")
    async def add_cache_headers(request: Request, call_next) -> Response:
        config = AppConfig.from_request(request)
        response = await call_next(request)  # type: Response

        if config.dev_mode:
            response.headers["Cache-Control"] = "no-cache, no-store"
            return response

        if request.url.path.startswith("/static/assets"):
            FRESH_TIME = 24 * 60 * 60  # 1 day
            STALE_TIME = 30 * 60 * 60 * 24  # 30 days
            response.headers.setdefault(
                "Cache-Control",
                f"max-age={FRESH_TIME}, stale-if-error={STALE_TIME}",
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
            + "frame-src li.lly.sh; "
            + "connect-src wss://li.lly.sh;",
        )
        response.headers.setdefault("X-Xss-Protection", "1; mode=block")
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("Cross-Origin-Opener-Policy", "same-origin")
        return response

    @app.middleware("http")
    async def redirect_to_canonical_host(request: Request, call_next) -> Response:
        config = AppConfig.from_request(request)
        if request.url.hostname != CANONICAL_HOST and not config.dev_mode:
            return RedirectResponse(URL(f"https://{CANONICAL_HOST}{request.url.path}?{request.url.query}"))
        else:
            return await call_next(request)

    return app
