from crawler.crawl import deduplicate_links


def test_deduplicate_links() -> None:
    """Function removes anchor links from a list of URLs."""
    links = [
        "https://www.abc.com#section1",
        "https://www.abc.com#section2",
        "https://www.def.com#section1",
        "https://www.def.com#section2",
        "https://www.ghi.com/path#section1",
        "https://www.ghi.com/path#section2",
        "https://www.jkl.com",
        "https://www.jkl.com#section1",
    ]

    expected = [
        "https://www.abc.com",
        "https://www.def.com",
        "https://www.ghi.com/path",
        "https://www.jkl.com",
    ]

    assert set(deduplicate_links(links)) == set(expected)


def test_deduplicate_links_end_slash() -> None:
    """Function removes end slashes links from a list of URLs."""
    links = [
        "https://www.abc.com/",
        "https://www.abc.com",
    ]

    expected = [
        "https://www.abc.com",
    ]

    assert set(deduplicate_links(links)) == set(expected)
