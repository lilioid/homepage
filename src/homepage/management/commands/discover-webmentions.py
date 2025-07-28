import asyncio
import logging
from argparse import ArgumentParser
from typing import Set

from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from django.test import AsyncClient, override_settings
from django.urls import reverse

from homepage import models

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Scrape the current site for mentions of external pages and store them for later sending"

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument(
            "--start-with",
            action="append",
            default=[reverse("home"), reverse("webmention-test")],
            help="Add an additional starting URL for crawling",
        )

    @override_settings(ALLOWED_HOSTS=["testserver"])
    def handle(self, *args, **options):
        asyncio.run(self.handle_async(*args, **options))

    async def handle_async(self, *args, **options):
        initial_list = options["start_with"]
        done_list = set()

        logger.info(f"Crawling django site starting with {' & '.join(initial_list)}")
        client = AsyncClient()
        async with asyncio.TaskGroup() as tg:
            for i in initial_list:
                tg.create_task(self.crawl_path(tg, client, i, done_list))

    async def crawl_path(self, tg: asyncio.TaskGroup, client: AsyncClient, path: str, done_list: Set[str]):
        path = path.rsplit("#", maxsplit=1)[0].rsplit("?", maxsplit=1)[0]
        if path in done_list:
            return
        else:
            done_list.add(path)

        logger.debug(f"Checking {path} for webmentions")
        response = await client.get(path, follow=True, secure=True)

        if not response.headers.get("Content-Type", default="text/plain").startswith("text/html"):
            return

        soup = BeautifulSoup(response.content, features="html.parser")
        mentions = set()
        for anchor_elem in soup.find_all("a"):
            href = anchor_elem.attrs["href"]
            href = href.split("?", maxsplit=1)[0].split("#", maxsplit=1)[0]
            if "external" not in anchor_elem.attrs.get("rel", ""):
                if href == "":
                    continue

                logger.debug(f"Found internal href to {href}")
                tg.create_task(self.crawl_path(tg, client, href, done_list))
                continue

            if href.startswith("http://") or href.startswith("https://"):
                logger.info(f"Found webmention to external site from {path} to {href}")
                mentions.add(href)

        await self.record_webmention(path, mentions)

    async def record_webmention(self, own_path: str, mentions: Set[str]):
        await models.OutboundWebmention.objects.abulk_create(
            [
                models.OutboundWebmention(
                    own_path=own_path,
                    href=i,
                )
                for i in mentions
            ],
            ignore_conflicts=True,
        )
