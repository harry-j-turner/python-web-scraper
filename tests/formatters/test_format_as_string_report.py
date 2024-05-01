from crawler.formatters import format_as_string_report


def test_format_as_string_report() -> None:
    """Function correctly formats a link map as a string report."""
    link_map = {
        "https://www.example.com": [
            "https://www.example.com/page1",
            "https://www.example.com/page2",
        ],
        "https://www.example.com/page1": ["https://www.example.com/page2"],
        "https://www.example.com/page2": ["https://www.example.com/page1"],
    }

    expected = """

Links from https://www.example.com:
  - https://www.example.com/page1
  - https://www.example.com/page2

Links from https://www.example.com/page1:
  - https://www.example.com/page2

Links from https://www.example.com/page2:
  - https://www.example.com/page1"""

    assert format_as_string_report(link_map) == expected
