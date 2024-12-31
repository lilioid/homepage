from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get("/robots.txt")
async def robots_txt() -> PlainTextResponse:
    return PlainTextResponse(
        content="""User-Agent: *
Allow: /
Disallow: /verysecretriddles
"""
    )


@router.get("/.well-known/security.txt")
@router.get("/security.txt")
async def security_txt() -> PlainTextResponse:
    return PlainTextResponse(
        content="""Contact: mailto:security@lly.sh
Preferred-Languages: en, de
Canonical: https://lly.sh/.well-known/security.txt
"""
    )
