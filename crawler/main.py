import logging

from crawler.crawl import crawl_site, LinkMap
from crawler.config import config_from_args
from crawler.formatters import format_as_string_report


def main() -> None:
    config = config_from_args()
    logging.basicConfig(level=config.log_level)

    link_map: LinkMap = crawl_site(config.url, workers=config.workers, limit=config.limit)

    string_report: str = format_as_string_report(link_map)
    print(string_report)


if __name__ == "__main__":
    main()
