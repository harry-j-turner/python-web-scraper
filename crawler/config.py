from argparse import ArgumentParser
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    url: str
    workers: int
    limit: Optional[int]
    log_level: str


def config_from_args() -> Config:
    parser = ArgumentParser(description="Crawl a website and output a map of links.")
    parser.add_argument("--url", help="The URL to crawl.", required=True)
    parser.add_argument(
        "--workers",
        help="The number of workers to use for crawling.",
        type=int,
        default=1,
    )
    parser.add_argument(
        "--limit",
        help="The maximum number of pages to crawl. If not provided, all pages will be crawled.",
        type=int,
        default=None,
    )
    parser.add_argument(
        "--log-level",
        help="The logging level to use.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
    )
    args = parser.parse_args()
    return Config(url=args.url, log_level=args.log_level, workers=args.workers, limit=args.limit)
