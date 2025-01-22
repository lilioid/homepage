#!/usr/bin/env python3
import asyncio
import logging
import sys
from argparse import ArgumentParser
from typing import Optional

import colorama
from hypercorn import Config as HypercornConfig
from hypercorn.asyncio import serve as hypercorn_serve
from sqlmodel import Session as DbSession

import homepage.app
import homepage.webmention
from homepage.config import AppConfig

logger = logging.getLogger(__name__)


def configure_logging(log_level: int):
    """
    Configure python logging with desired log level and automatically colored output
    """

    class DynFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:
            colors = {
                logging.DEBUG: colorama.Fore.CYAN,
                logging.INFO: colorama.Fore.BLUE,
                logging.WARNING: colorama.Fore.YELLOW,
                logging.ERROR: colorama.Fore.RED,
                logging.CRITICAL: colorama.Back.RED + colorama.Fore.WHITE,
            }
            return colors[record.levelno] + super().format(record) + colorama.Style.RESET_ALL

    logger = logging.getLogger()
    logger.setLevel(log_level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        DynFormatter(fmt="%(asctime)s - %(levelname)s (%(name)s): %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    )
    logger.addHandler(handler)


def run_webserver(cfg: AppConfig):
    asyncio.run(
        hypercorn_serve(
            homepage.app.make_app(cfg),
            HypercornConfig.from_mapping(
                bind=cfg.bind,
                accesslog=logging.getLogger("http.request"),
                errorlog=logging.getLogger("http.error"),
            ),
        )
    )


def send_webmentions(db_path: str, debug: bool = False, force_resend: bool = False, dry_run: bool = False):
    engine = homepage.state.connect_engine(db_path, debug)
    homepage.state.init_state(engine)
    with DbSession(engine) as session:
        asyncio.run(homepage.webmention.send_all_webmentions(session, force_resend, dry_run))


def main() -> Optional[int]:
    colorama.init()
    argp = ArgumentParser(prog="mooday", description="Daily mood tracker")
    subp = argp.add_subparsers(dest="action")
    argp.add_argument(
        "-v", "--verbose", action="count", default=0, help="Increase program verbosity (can be supplied multiple itmes)"
    )
    argp.add_argument(
        "-q", "--quiet", action="count", default=0, help="Decrease program verbosity (can be specified mutliple times)"
    )
    argp.add_argument("--db", default="./database.sqlite", help="sqlite connection string")

    serve = subp.add_parser("serve")
    serve.add_argument(
        "--bind", "-b", default="localhost:8000", help="Host and port to which the webserver should bind"
    )
    serve.add_argument(
        "--dev", action="store_true", default=False, help="Start in development mode which reduces caching"
    )

    send_webm = subp.add_parser("send-webmentions")
    send_webm.add_argument("--dry-run", action="store_true", default=False, help="Don't actually send webmentions")
    send_webm.add_argument(
        "--force-resend",
        action="store_true",
        default=False,
        help="Force resending all webmentions even if they have been sent before",
    )

    args = argp.parse_args()
    configure_logging(log_level=logging.INFO - (args.verbose * 10) + (args.quiet * 10))

    match args.action:
        case "serve":
            app_config = AppConfig(bind=args.bind, db_path=args.db, dev_mode=args.dev)
            run_webserver(app_config)
        case "send-webmentions":
            send_webmentions(args.db, (args.verbose - args.quiet) > 0, args.force_resend, args.dry_run)
        case _:
            raise Exception(f"Unhandled argument action {args.action}")


if __name__ == "__main__":
    sys.exit(main())
