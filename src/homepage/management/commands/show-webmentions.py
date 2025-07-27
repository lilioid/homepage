import logging
from argparse import ArgumentParser

from django.core.management import BaseCommand
from terminaltables import AsciiTable

from homepage import models

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Show status of current webmentions"

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument(
            "--only-unsent", default=False, action="store_true", help="For outgoing webmentions, only show unsent ones"
        )

    def handle(self, *args, **options):
        filter = {}
        if options["only_unsent"]:
            filter["webmention_sent"] = False

        mentions = models.Webmention.objects.filter(**filter).order_by("webmention_sent", "href").all()
        table = AsciiTable(
            [["href", "Local Path", "Is Sent?"]]
            + [[i_mention.href, i_mention.own_path, i_mention.webmention_sent] for i_mention in mentions.iterator()]
        )
        table.title = f"Outgoing Webmentions ({len(mentions)})"
        print(table.table)
