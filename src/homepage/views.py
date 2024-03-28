from http import HTTPStatus

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from . import templates

router = APIRouter()


@router.get("/")
async def index_redirect() -> RedirectResponse:
    return RedirectResponse("/index.html")


@router.get("/index.html", tags=["site"])
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, name="views/index.html")


@router.get("/projects.html", tags=["site"])
async def projects(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, name="views/projects.html")


@router.get("/pixelflut.html", tags=["site"])
async def pixelflut(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, name="views/pixelflut.html")
