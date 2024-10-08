import logging
import re
import xml.etree.ElementTree as etree
from dataclasses import dataclass
from datetime import datetime
from hashlib import sha1
from pathlib import Path as FsPath
from typing import Annotated, Dict, List, Optional

import frontmatter
import markdown
from fastapi import APIRouter, HTTPException, Path, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from markdown.treeprocessors import Treeprocessor

from . import SRC_DIR, templates

router = APIRouter()
logger = logging.getLogger(__name__)


class WrapSectionProcessor(Treeprocessor):
    """A markdown processor that automatically wraps content in <section> tags based on <h2> headings"""

    def run(self, root: etree.Element) -> Optional[etree.Element]:
        try:
            new_root = etree.Element(root.tag, root.attrib)
            cur_section = etree.Element("section")
            new_root.append(cur_section)

            for child in root:
                if child.tag == "h2":
                    cur_section = etree.Element("section")
                    cur_section.append(child)
                    new_root.append(cur_section)
                else:
                    cur_section.append(child)

            return new_root
        except Exception:
            logger.exception("Could not process element tree with %s", type(self))


class SectionIdLinker(Treeprocessor):
    """
    A markdown processor that assigns id= attributes to sections based on the contained <h2> tag
    as well as creating links to the section with a # character after the heading.
    """

    def run(self, root: etree.Element) -> Optional[etree.Element]:
        try:
            for section in root.findall("section[h2]"):
                heading = section.find("h2")
                sec_id = heading.text.lower().replace(" ", "-").replace("/", "-").replace("&", "")
                logger.debug("Linking section with heading %s as id=%s", heading.text, sec_id)

                # add id to section itself
                section.attrib["id"] = sec_id

                # add span containing the actual title
                elem = etree.Element("span")
                elem.text = heading.text + " "
                heading.clear()
                heading.append(elem)

                # add anchor containing a link to the section
                elem = etree.Element("a", {"href": f"#{sec_id}", "title": "Link to this section"})
                elem.text = "#"
                heading.append(elem)

        except Exception:
            logger.exception("Could not process element tree with %s", type(self))


class FootnotesAsideTransformer(Treeprocessor):
    """A markdown processor that converts the footnotes <div> container into an <aside>"""

    def run(self, root: etree.Element) -> Optional[etree.Element]:
        try:
            container = root.find("div[@class='footnote']")
            container.tag = "aside"
        except Exception:
            logger.exception("Could not process element tree with %s", type(self))


class BlogMdExt(markdown.Extension):
    """Custom markdown extension which registers the processors defined above"""

    def extendMarkdown(self, md: markdown.Markdown):
        logger.debug("Registering custom markdown processors for blog")
        try:
            md.treeprocessors.register(WrapSectionProcessor(), "wrap-sections", 75)
            md.treeprocessors.register(SectionIdLinker(), "link-sections", 70)
            md.treeprocessors.register(FootnotesAsideTransformer(), "footnote-aside-transformer", 40)
        except Exception:
            logger.exception("Could not register processors for extension %s", type(self))


@dataclass
class Article:
    """Metadata and content for each article"""

    id: int
    source: FsPath
    title: str
    short_desc: str
    tags: List[str]
    created_at: datetime
    edited_at: Optional[datetime]
    body: str
    author: str
    is_draft: bool

    @property
    def ref(self) -> str:
        name = self.title.lower().replace(" ", "-").replace("/", "-").replace("&", "and")
        return f"{self.id:03}-{name}"

    @property
    def body_html(self) -> str:
        return markdown.markdown(
            text=self.body,
            extensions=["fenced_code", "footnotes", "tables", "sane_lists", "smarty", "codehilite", BlogMdExt()],
        )

    @property
    def last_modified(self) -> datetime:
        if self.edited_at is not None:
            return self.edited_at
        return self.created_at


def parse_article(path: FsPath) -> Article:
    """Read the given files content and extract article metadata + content from it"""
    with path.open("r", encoding="utf-8") as f:
        fm = frontmatter.load(f)

    return Article(
        id=extract_article_id(path.name),
        source=path,
        title=fm["title"],
        short_desc=fm["short_desc"],
        tags=fm["tags"],
        created_at=datetime.fromisoformat(fm["created_at"]),
        edited_at=datetime.fromisoformat(fm["edited_at"]) if "edited_at" in fm else None,
        author=fm["author"],
        is_draft="draft" in fm and fm["draft"] is True,
        body=fm.content,
    )


def make_article_index() -> Dict[str, Article]:
    """Search the `blog` directories content for markdown files and parse articles from all of them"""
    return {
        extract_article_id(file_path): parse_article(dir_path / file_path)
        for (dir_path, _dir_names, file_names) in (SRC_DIR / "blog").walk()
        for file_path in file_names
        if file_path.endswith(".md")
    }


def extract_article_id(article_ref) -> int:
    """Extract an articles numeric ID from a given reference"""
    return int(re.match(r"(\d+)(-.*)?", article_ref).group(1))


@router.get("/blog/")
async def index_redirect() -> RedirectResponse:
    return RedirectResponse("/blog/index.html")


@router.get("/blog/index.html", tags=["blog"])
async def index(request: Request, tag: Optional[str] = None, with_drafts: bool = False) -> HTMLResponse:
    # generate article index
    idx = make_article_index()
    article_list = sorted(
        (i for i in idx.values()),
        key=lambda i: i.created_at,
        reverse=True,
    )

    # filter articles if requested
    if not with_drafts:
        logger.debug("Filtering blog posts to exclude drafts")
        article_list = (i for i in article_list if not i.is_draft)
    if tag is not None:
        logger.debug("Filtering blog posts for tag %s", tag)
        article_list = (i for i in article_list if tag in i.tags)

    # render index template and return it
    return templates.TemplateResponse(
        request,
        name="blog/index.html",
        context={
            "articles": list(article_list),
            "tag_filter": tag,
        },
    )


@router.get("/blog/feed.rss")
async def rss_feed(request: Request) -> Response:
    # generate article index
    idx = make_article_index()
    article_list = sorted(
        (i for i in idx.values() if not i.is_draft),
        key=lambda i: i.created_at,
        reverse=True,
    )

    # render feed template and return it
    return templates.TemplateResponse(
        request,
        name="blog/feed.rss",
        headers={
            "Content-Type": "application/rss+xml",
        },
        context={
            "base_url": request.base_url,
            "articles": list(article_list),
            "last_edit_date": sorted((i.last_modified for i in article_list))[0],
        },
    )


@router.get("/blog/feed.atom")
async def atom_feed(request: Request) -> Response:
    # generate article index
    idx = make_article_index()
    article_list = sorted(
        (i for i in idx.values() if not i.is_draft),
        key=lambda i: i.created_at,
        reverse=True,
    )

    # render feed template and return it
    return templates.TemplateResponse(
        request,
        name="blog/feed.atom",
        headers={
            "Content-Type": "application/atom+xml",
        },
        context={
            "base_url": request.base_url,
            "articles": list(article_list),
            "last_edit_date": sorted((i.last_modified for i in article_list))[0],
        },
    )


@router.get("/blog/{article_ref}.html", tags=["blog"], response_model=None)
async def article(
    request: Request, article_ref: Annotated[str, Path(pattern=r"(\d+)(-.*)?")]
) -> HTMLResponse | Response:
    idx = make_article_index()
    article_id = extract_article_id(article_ref)

    # send 404 if the article does not exist
    if article_id not in idx:
        raise HTTPException(status_code=404, detail=f"Blog article with id {article_id} does not exist")

    # redirect to the canonical article url
    article = idx[article_id]
    if article_ref != article.ref:
        return RedirectResponse(url=f"{article.ref}.html", status_code=302)

    # handle requests containing ETag by indicating Not-Modified
    etag = 'W/"' + sha1(article.body.encode("UTF-8")).hexdigest() + '"'
    if "if-none-match" in request.headers and request.headers["if-none-match"] == etag:
        return Response(status_code=304)

    # render the blog post and return it
    return templates.TemplateResponse(
        request,
        name="blog/[article].html",
        context={"article": article},
        headers={
            "ETag": etag,
        },
    )
