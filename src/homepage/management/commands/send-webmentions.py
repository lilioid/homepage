import asyncio
import logging
from argparse import ArgumentParser

import aiohttp
from django.conf import settings
from django.core.management import BaseCommand

from homepage import models, webmention

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Send all pending webmentions"

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("--dry-run", default=False, action="store_true", help="Don't actually send out webmentions")
        parser.add_argument(
            "--resend",
            default=False,
            action="store_true",
            help="Send webmentions even when one has already been sent before",
        )

    def handle(self, *args, **options):
        asyncio.run(self.handle_async(*args, **options))

    async def handle_async(self, *args, **options):
        async with aiohttp.ClientSession() as sess, asyncio.TaskGroup() as tg:
            obj_filter = {}
            if not options["resend"]:
                obj_filter["webmention_sent"] = False

            logger.debug(f"Filtering for webmentions with filter {obj_filter}")
            qs = models.Webmention.objects.filter(**obj_filter)
            logger.info(f"Processing {await qs.acount()} mentions")
            async for i in qs.aiterator():
                tg.create_task(self.handle_webmention(sess, i, options["dry_run"]))

    async def handle_webmention(self, sess: aiohttp.ClientSession, mention: models.Webmention, dry_run: bool = False):
        src_url = f"{settings.BASE_URI.geturl()}{mention.own_path}"
        sent = await webmention.process_mention(sess, src_url, mention.href, dry_run)
        if sent:
            mention.webmention_sent = True
            await mention.asave()
