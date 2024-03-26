from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from homepage import STATIC_DIR, templates
from homepage.views import router

app = FastAPI(openapi_url=None)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/", router)


@app.exception_handler(404)
def handle404(request: Request, _exception) -> HTMLResponse:
    return templates.TemplateResponse(request, name="404.html")
