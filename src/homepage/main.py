from environs import Env
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from starlette.datastructures import URL

from homepage import STATIC_DIR, templates, views, well_known

env = Env()
DEV_MODE = env.bool("DEV_MODE", default=False)

app = FastAPI(openapi_url=None)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(views.router)
app.include_router(well_known.router)


@app.exception_handler(404)
async def handle404(request: Request, _exception) -> HTMLResponse:
    return templates.TemplateResponse(request, name="404.html", status_code=404)


@app.middleware("http")
async def add_cache_headers(request: Request, call_next) -> Response:
    response = await call_next(request)  # type: Response

    if DEV_MODE:
        return response

    if request.url.path.startswith("/static"):
        FRESH_TIME = 1 * 60 * 60  # 1 hour
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
