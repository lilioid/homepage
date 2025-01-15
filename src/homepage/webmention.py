import asyncio
import logging
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup
from fastapi import APIRouter

import homepage.blog

logger = logging.getLogger(__name__)
router = APIRouter()


async def find_webmention_endpoint(session: aiohttp.ClientSession, url: str) -> Optional[str]:
    logger.debug("Probing %s for its webmention endpoint", url)
    async with session.get(url) as response:
        if response.status != 200:
            logger.debug(
                "URL %s does not have a webmention endpoint as the request to it returned status code %s",
                url,
                response.status,
            )
            return None

        # TODO: Add support for LINK HTTP headers

        if response.content_type != "text/html":
            logger.debug(
                "URL %s does not have a webmention endpoint as the request to it returned non-html content-type %s",
                url,
                response.content_type,
            )
            return None

        soup = BeautifulSoup(await response.text(), features="html.parser")
        endpoint = soup.find(["link", "a"], attrs={"rel": "webmention"})
        if endpoint is None:
            return None

        endpoint = urljoin(url, endpoint["href"])
        logger.debug("Found webmention endpoint for %s at %s", url, endpoint)
        return endpoint


async def process_mention(tg: asyncio.TaskGroup, session: aiohttp.ClientSession, src_url: str, dst_url: str):
    logger.debug("Processing mention from %s to %s", src_url, dst_url)
    webmention_endpoint = await find_webmention_endpoint(session, dst_url)
    if webmention_endpoint is not None:
        pass


async def process_webpage(tg: asyncio.TaskGroup, session: aiohttp.ClientSession, page_url: str, html: str):
    logger.info("Processing webmentions of %s", page_url)
    soup = BeautifulSoup(html, features="html.parser")
    for i_anchor in soup.find_all("a", attrs={"rel": "external"}):
        tg.create_task(process_mention(tg, session, page_url, i_anchor["href"]))


async def send_webmentions(dry_run: bool):
    articles = homepage.blog.make_article_index()
    logger.info("Processing Webmentions of %s articles", len(articles))
    session = aiohttp.ClientSession(headers={"User-Agent": "li.lly.sh Homepage (Webmention)"})
    async with session, asyncio.TaskGroup() as tg:
        tg.create_task(
            process_webpage(
                tg, session, "https://localhost:8000", "<a rel='external' href='https://webmention.rocks/test/3'>"
            )
        )
        # for i_article in articles.values():
        #    # skip drafts
        #    if i_article.is_draft:
        #        logger.info("Skipping article %s because it is a draft", i_article.ref)
        #        continue

        #    # schedule processing
        #    tg.create_task(process_webpage(i_article.body_html))
