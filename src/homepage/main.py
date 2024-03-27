from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles

from homepage import STATIC_DIR, templates, views, well_known

app = FastAPI(openapi_url=None)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(views.router)
app.include_router(well_known.router)


@app.exception_handler(404)
async def handle404(request: Request, _exception) -> HTMLResponse:
    return templates.TemplateResponse(request, name="404.html")


@app.middleware("http")
async def add_cache_headers(request: Request, call_next) -> Response:
    response = await call_next(request)  # type: Response
    if request.url.path.startswith("/static"):
        FRESH_TIME = 1 * 60 * 60  # 1 hour
        STALE_TIME = 30 * 60 * 60 * 24  # 30 days
        response.headers.setdefault(
            "Cache-Control",
            f"max-age={FRESH_TIME}, stale-while-revalidate={STALE_TIME}, stale-if-error={STALE_TIME}",
        )
    else:
        FRESH_TIME = 1 * 60  # 1 minute
        STALE_TIME = 30 * 60 * 60 * 24  # 30 days
        response.headers.setdefault(
            "Cache-Control",
            f"max-age={FRESH_TIME}, stale-while-revalidate={STALE_TIME}, stale-if-error={STALE_TIME}",
        )
    return response


@app.middleware("http")
async def add_security_headers(request: Request, call_next) -> Response:
    response = await call_next(request)  # type: Response
    response.headers.setdefault(
        "Content-Security-Policy",
        f"default-src 'self' 'unsafe-inline'; frame-src ftsell.de; connect-src wss://ftsell.de;",
    )
    response.headers.setdefault("X-Xss-Protection", "1; mode=block")
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    return response
