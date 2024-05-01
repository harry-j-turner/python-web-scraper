from crawler.crawl import LinkMap


def format_as_string_report(link_map: LinkMap) -> str:
    """Format the link map as a string report."""

    report = ""
    for url, links in link_map.items():
        report += f"\n\nLinks from {url}:"
        for link in links:
            report += f"\n  - {link}"

    return report
