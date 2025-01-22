import asyncio
import logging
import re
from datetime import UTC, datetime
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup
from fastapi import APIRouter
from sqlmodel import Session as DbSession
from sqlmodel import select

import homepage.blog
from homepage.state import WebmentionSentEvent

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

        # extract HTTP Link header with rel=webmention if present
        # TODO: Fix https://webmention.rocks/test/19
        for i_link in response.headers.getall("link", []):
            match = re.match(r"^<(.+)>; rel=\"?(.+)\"?$", i_link)
            if "webmention" in match.group(2):
                endpoint = urljoin(url, match.group(1))
                logger.debug("Found webmention endpoint for %s at %s", url, endpoint)
                return endpoint

        if response.content_type != "text/html":
            logger.debug(
                "URL %s does not have a webmention endpoint as the request to it returned non-html content-type %s",
                url,
                response.content_type,
            )
            return None

        soup = BeautifulSoup(await response.text(), features="html.parser")
        for endpoint in soup.find_all(["link", "a"], attrs={"rel": "webmention"}):
            if "href" not in endpoint.attrs:
                continue

            endpoint = urljoin(url, endpoint["href"])
            logger.debug("Found webmention endpoint for %s at %s", url, endpoint)
            return endpoint

        # no webmention endpoint found
        return None


async def send_webmention(
    http_session: aiohttp.ClientSession, db_session: DbSession, endpoint: str, src_url: str, dst_url: str
):
    async with http_session.post(
        endpoint,
        data=aiohttp.FormData(
            {
                "source": src_url,
                "target": dst_url,
            }
        ),
    ) as response:
        if response.status >= 200 and response.status < 300:
            logger.info("Successfully sent webmention from %s to %s", src_url, dst_url)
        else:
            logger.error(
                "Could not send webmention from %s to %s: [%s]: %s",
                src_url,
                dst_url,
                response.status,
                await response.text(),
            )


async def process_mention(
    tg: asyncio.TaskGroup,
    http_session: aiohttp.ClientSession,
    db_session: DbSession,
    src_url: str,
    dst_url: str,
    content_date: datetime,
    dry_run: bool = False,
    force_resend: bool = False,
):
    logger.debug("Processing mention from %s to %s", src_url, dst_url)
    webmention_endpoint = await find_webmention_endpoint(http_session, dst_url)
    if webmention_endpoint is not None and not dry_run:
        if force_resend or not is_webmention_already_sent(db_session, src_url, dst_url, content_date):
            logger.info("Sending webmention from %s to %s%s", src_url, dst_url, " (dry-run)" if dry_run else "")
            # await send_webmention(http_session, db_session, webmention_endpoint, src_url, dst_url)
            persist_webmention(db_session, src_url, dst_url)
        else:
            logger.info(
                "Skipping sending webmention from %s to %s because one has already been sent for that content version",
                src_url,
                dst_url,
            )


def persist_webmention(db: DbSession, src_url: str, dst_url: str):
    logger.debug("Persisting sent webmention from %s to %s in database", src_url, dst_url)
    event = WebmentionSentEvent(
        src_uri=src_url,
        target_uri=dst_url,
        date=datetime.now(UTC),
    )
    db.add(event)
    db.commit()


def is_webmention_already_sent(db: DbSession, src_url, dst_url: str, content_date: datetime) -> bool:
    logger.debug(
        "Looking up whether a webmention was already sent from %s to %s after %s", src_url, dst_url, content_date
    )
    stmt = (
        select(WebmentionSentEvent)
        .where(WebmentionSentEvent.src_uri == src_url)
        .where(WebmentionSentEvent.target_uri == dst_url)
        .where(WebmentionSentEvent.date >= content_date)
    )
    return db.exec(stmt).first() is not None


async def process_webpage(
    tg: asyncio.TaskGroup,
    http_session: aiohttp.ClientSession,
    db_session: DbSession,
    page_url: str,
    html: str,
    content_date: datetime,
    dry_run: bool = False,
    force_resend: bool = False,
):
    logger.info("Processing webmentions of %s", page_url)
    soup = BeautifulSoup(html, features="html.parser")
    for i_anchor in soup.find_all("a", attrs={"rel": "external"}):
        tg.create_task(
            process_mention(
                tg, http_session, db_session, page_url, i_anchor["href"], content_date, dry_run, force_resend
            )
        )


async def send_all_webmentions(db_session: DbSession, force_resend: bool, dry_run: bool):
    """
    Process the internal blog and send out all pending webmentions
    """
    articles = homepage.blog.make_article_index()
    logger.info("Processing Webmentions of %s articles", len(articles))
    http_session = aiohttp.ClientSession(headers={"User-Agent": "li.lly.sh Homepage (Webmention)"})
    async with http_session, asyncio.TaskGroup() as tg:
        for i_article in articles.values():
            # skip drafts
            if i_article.is_draft:
                logger.info("Skipping article %s because it is a draft", i_article.ref)
                continue

            # schedule processing
            tg.create_task(
                process_webpage(
                    tg,
                    http_session,
                    db_session,
                    i_article.absolute_url,
                    i_article.body_html,
                    i_article.last_modified,
                    dry_run,
                    force_resend,
                )
            )
