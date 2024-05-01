import pytest

from crawler.crawl import extract_domain_from_url


@pytest.mark.parametrize(
    "url, domain",
    [
        ("https://example.com", "example.com"),  # Basic URL
        ("example.com", "example.com"),  # Missing protocol
        ("https://blog.example.com", "blog.example.com"),  # Subdomain
        ("https://example.co.uk", "example.co.uk"),  # TLD with multiple parts
        ("https://example.com?query=param", "example.com"),  # Query parameter
        ("https://example.com/path", "example.com"),  # With path
        (
            "https://www.example.com",
            "example.com",
        ),  # www redirects to root domain
        ("https://example.com:8080", "example.com"),  # URL with port
        ("localhost:8080", "localhost"),  # Localhost
        ("invalidurl", None),  # Invalid URL
        ("", None),  # Empty URL
        ("   ", None),  # Whitespace
        ("/just/a/path", None),  # No domain present
        ("tel:+442077414100", None),  # Telephone link
    ],
)
def test_extract_domain_from_url(url: str, domain: str) -> None:
    """Function extracts the domain from the URL and handles edge cases."""
    first_level_domain = extract_domain_from_url(url)
    assert first_level_domain == domain
