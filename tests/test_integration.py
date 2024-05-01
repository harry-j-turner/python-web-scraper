import pytest

from crawler.crawl import crawl_site
from crawler.formatters import format_as_string_report

FAKE_WEBSITE_REPORT = """

Links from http://localhost:8000:
  - http://localhost:8000/A.html
  - http://localhost:8000/B.html
  - http://localhost:8000/C.html

Links from http://localhost:8000/A.html:
  - http://localhost:8000/B.html
  - http://localhost:8000/D.html

Links from http://localhost:8000/B.html:
  - http://localhost:8000/C.html
  - http://localhost:8000/E.html

Links from http://localhost:8000/C.html:
  - http://localhost:8000/G.html

Links from http://localhost:8000/D.html:

Links from http://localhost:8000/E.html:
  - http://localhost:8000/F.html
  - http://localhost:8000/G.html

Links from http://localhost:8000/F.html:
  - http://localhost:8000/A.html

Links from http://localhost:8000/G.html:
  - http://localhost:8000/index.html

Links from http://localhost:8000/index.html:
  - http://localhost:8000/A.html
  - http://localhost:8000/B.html
  - http://localhost:8000/C.html"""


@pytest.mark.integration
def test_integration() -> None:
    """Test the entire crawl process on a local test website."""

    # Given - A local test website running on localhost:8000

    # When - We crawl the website
    link_map = crawl_site("http://localhost:8000")

    # And - We format the link_map as a string report (ordering by key for testability)
    sorted_keys = sorted(link_map.keys())
    ordered_link_map = {key: link_map[key] for key in sorted_keys}
    string_report = format_as_string_report(ordered_link_map)

    # Then - We should see the following links in the report
    assert string_report == FAKE_WEBSITE_REPORT
