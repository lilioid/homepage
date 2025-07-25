import logging
import re
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


@dataclass
class WebmentionPayload:
    source: str
    target: str


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


async def send_webmention(http_session: aiohttp.ClientSession, endpoint: str, src_url: str, dst_url: str):
    async with http_session.post(
        endpoint,
        data=aiohttp.FormData(
            {
                "source": src_url,
                "target": dst_url,
            }
        ),
    ) as response:
        if 200 <= response.status < 300:
            logger.debug("Successfully sent webmention from %s to %s", src_url, dst_url)
        else:
            logger.error(
                "Could not send webmention from %s to %s: [%s]: %s",
                src_url,
                dst_url,
                response.status,
                await response.text(),
            )


async def process_mention(
    http_session: aiohttp.ClientSession,
    src_url: str,
    dst_url: str,
    dry_run: bool = False,
):
    logger.debug("Processing mention from %s to %s", src_url, dst_url)

    try:
        webmention_endpoint = await find_webmention_endpoint(http_session, dst_url)
    except Exception as e:
        logger.error("Could not query for webmention endpoint: %s", e)
        return

    if webmention_endpoint is not None:
        if dry_run:
            logger.info("DRY-RUN! Sending webmention from %s to %s", src_url, dst_url)
            return
        else:
            logger.info("Sending webmention from %s to %s", src_url, dst_url)
            await send_webmention(http_session, webmention_endpoint, src_url, dst_url)
