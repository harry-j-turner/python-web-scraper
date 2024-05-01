import pytest

from bs4 import BeautifulSoup

from crawler.crawl import extract_domain_urls_from_soup


@pytest.mark.parametrize(
    "html_content, base_url, expected_urls",
    [
        # Only matching domain URLs are extracted
        (
            '<a href="http://example.com/page1">Page 1</a>'
            '<a href="http://example.com/page2">Page 2</a>'
            '<a href="http://notexample.com">External</a>',
            "http://example.com",
            ["http://example.com/page1", "http://example.com/page2"],
        ),
        # Relative URLs
        (
            '<a href="/page1">Page 1</a><a href="/page2">Page 2</a>',
            "http://example.com",
            ["http://example.com/page1", "http://example.com/page2"],
        ),
        # No href attributes
        (
            '<a>Missing href</a><a href="http://example.com/page1">Page 1</a>',
            "http://example.com",
            ["http://example.com/page1"],
        ),
    ],
)
def test_extract_urls_from_soup(html_content: str, base_url: str, expected_urls: list[str]) -> None:
    """Function extracts URLs from a HTML page that are within the same domain."""
    soup = BeautifulSoup(html_content, "html.parser")
    extracted_urls = extract_domain_urls_from_soup(soup, base_url)
    assert extracted_urls == expected_urls
