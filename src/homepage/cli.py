#!/usr/bin/env python3
import asyncio
import logging
import sys
from argparse import ArgumentParser
from typing import Optional

import colorama
from hypercorn import Config as HypercornConfig
from hypercorn.asyncio import serve as hypercorn_serve

import homepage.app
from homepage.config import AppConfig


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


def main() -> Optional[int]:
    colorama.init()
    argp = ArgumentParser(prog="mooday", description="Daily mood tracker")
    argp.add_argument(
        "-v", "--verbose", action="count", default=0, help="Increase program verbosity (can be supplied multiple itmes)"
    )
    argp.add_argument(
        "-q", "--quiet", action="count", default=0, help="Decrease program verbosity (can be specified mutliple times)"
    )
    argp.add_argument("--bind", "-b", default="localhost:8000", help="Host and port to which the webserver should bind")
    argp.add_argument("--db", default="database.sqlite", help="Path to a file in which webmention logs are persisted")
    argp.add_argument(
        "--dev", action="store_true", default=False, help="Start in development mode which reduces caching"
    )
    args = argp.parse_args()

    configure_logging(log_level=logging.INFO - (args.verbose * 10) + (args.quiet * 10))
    app_config = AppConfig(bind=args.bind, db_path=args.db, dev_mode=args.dev)
    run_webserver(app_config)


if __name__ == "__main__":
    sys.exit(main())
