import pytest

from crawler.crawl import get_unseen_links


@pytest.mark.parametrize(
    "links, link_map, limit, expected",
    [
        (
            ["http://a.com/1", "http://a.com/2", "http://a.com/3"],
            {},
            None,
            ["http://a.com/1", "http://a.com/2", "http://a.com/3"],
        ),
        (
            ["http://a.com/1", "http://a.com/2", "http://a.com/3"],
            {},
            2,
            ["http://a.com/1", "http://a.com/2"],
        ),
        (
            ["http://a.com/1", "http://a.com/2", "http://a.com/3"],
            {"http://a.com/1": [], "http://a.com/2": []},
            None,
            ["http://a.com/3"],
        ),
        (
            ["http://a.com/1", "http://a.com/2", "http://a.com/3"],
            {"http://a.com/1": [], "http://a.com/2": []},
            2,
            [],
        ),
    ],
)
def test_get_unseen_links(
    links: list[str], link_map: dict[str, list[str]], limit: int, expected: list[str]
) -> None:
    """Function returns correct number of links for processing given existing set and limit."""
    returned_set = set(get_unseen_links(links, link_map, limit))
    expected_set = set(expected)
    assert returned_set == expected_set
