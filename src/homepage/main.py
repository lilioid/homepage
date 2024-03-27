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
