import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path as FsPath
from typing import Annotated, Dict, List, Optional

import markdown
from fastapi import APIRouter, HTTPException, Path, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from frontmatter import Frontmatter

from . import SRC_DIR, templates

router = APIRouter()


@dataclass
class Article:
    id: int
    source: FsPath
    title: str
    short_desc: str
    tags: List[str]
    created_at: datetime
    body: str
    author: str
    is_draft: bool

    @property
    def ref(self) -> str:
        name = self.title.lower().replace(" ", "-").replace("/", "-")
        return f"{self.id:03}-{name}"

    @property
    def body_html(self) -> str:
        return markdown.markdown(
            text=self.body,
            extensions=[],
        )


def read_article(path: FsPath) -> Article:
    fm = Frontmatter.read_file(path)
    return Article(
        id=canonicalize_article_ref(path.name),
        source=path,
        title=fm["attributes"]["title"],
        short_desc=fm["attributes"]["short_desc"],
        tags=fm["attributes"]["tags"],
        created_at=datetime.fromisoformat(fm["attributes"]["created_at"]),
        author=fm["attributes"]["author"],
        is_draft="draft" in fm["attributes"] and fm["attributes"]["draft"] is True,
        body=fm["body"],
    )


# @cache
def calc_article_index() -> Dict[str, Article]:
    return {
        canonicalize_article_ref(file_path): read_article(dir_path / file_path)
        for (dir_path, _dir_names, file_names) in (SRC_DIR / "blog").walk()
        for file_path in file_names
    }


def canonicalize_article_ref(article_ref) -> int:
    return int(re.match(r"(\d+)(-.*)?", article_ref).group(1))


@router.get("/blog/")
async def index_redirect() -> RedirectResponse:
    return RedirectResponse("/blog/index.html")


@router.get("/blog/index.html", tags=["blog"])
async def index(request: Request, tags: Optional[str] = None) -> HTMLResponse:
    idx = calc_article_index()
    article_list = sorted(
        (i for i in idx.values() if not i.is_draft),
        key=lambda i: i.created_at,
        reverse=True,
    )
    return templates.TemplateResponse(
        request,
        name="blog/index.html",
        context={
            "articles": article_list,
        },
    )


@router.get("/blog/{article_ref}.html", tags=["blog"])
async def article(request: Request, article_ref: Annotated[str, Path(pattern=r"(\d+)(-.*)?")]) -> HTMLResponse:
    idx = calc_article_index()
    article_id = canonicalize_article_ref(article_ref)

    if article_id not in idx:
        raise HTTPException(status_code=404, detail=f"Blog article with id {article_id} does not exist")

    article = idx[article_id]
    if article_ref != article.ref:
        return RedirectResponse(url=f"{article.ref}.html", status_code=302)

    return templates.TemplateResponse(request, name="blog/[article].html", context={"article": article})
