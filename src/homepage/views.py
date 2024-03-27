from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from . import templates

router = APIRouter()


@router.get("/", tags=["site"])
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, name="views/index.html")


@router.get("/projects", tags=["site"])
async def projects(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, name="views/projects.html")


@router.get("/pixelflut", tags=["site"])
async def pixelflut(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, name="views/pixelflut.html")
