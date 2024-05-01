import logging
from typing import Optional
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait
import requests
from bs4 import BeautifulSoup
from furl import furl


LinkMap = dict[str, list[str]]
Domain = str

logger = logging.getLogger(__name__)


def crawl_site(url: str, workers: int = 1, limit: Optional[int] = None) -> LinkMap:
    """Crawl the domain of the provided URL and return a map of pages and their links."""

    link_map: LinkMap = {}
    active_futures = set()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future = executor.submit(crawl_one_url, url)
        active_futures.add(future)
        link_map[url] = []

        while active_futures:
            completed_futures, _ = wait(active_futures, return_when=FIRST_COMPLETED)

            for future in completed_futures:
                active_futures.remove(future)
                url, links = future.result()
                link_map[url] = links

                for link in get_unseen_links(links, link_map, limit=limit):
                    future = executor.submit(crawl_one_url, link)
                    active_futures.add(future)
                    link_map[link] = []

    return link_map


def crawl_one_url(url: str) -> tuple[str, list[str]]:
    """Fetch and parse a single URL and return a list of urls contained on that page."""

    try:
        logger.info(f"Crawling {url}")
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")
        found_urls = extract_domain_urls_from_soup(soup, url_being_crawled=url)

    except ValueError as e:
        logger.error(f"Error crawling {url}: {e}")
        return url, []

    return url, found_urls


def get_unseen_links(links: list[str], link_map: LinkMap, limit: Optional[int] = None) -> list[str]:
    """Process a set of links and return the links that need processing."""

    deduplicated_links = deduplicate_links(links)
    unseen_links = [link for link in deduplicated_links if link not in link_map]

    budget = limit - len(link_map) if limit else None

    return unseen_links[:budget]


def extract_domain_urls_from_soup(soup: BeautifulSoup, url_being_crawled: str) -> list[str]:
    """Find all valid URLS from the same domain within the processed soup."""

    raw_urls = [el.get("href") for el in soup.find_all("a") if el.get("href")]
    well_formed_urls = [urljoin(url_being_crawled, link) for link in raw_urls]

    target_domain = extract_domain_from_url(url_being_crawled)
    valid_urls = [url for url in well_formed_urls if extract_domain_from_url(url) == target_domain]

    return valid_urls


def deduplicate_links(links: list[str]) -> list[str]:
    """Deduplicate links that differ only by their anchor."""

    unique_links = set()
    for link in links:
        f = furl(link)
        f.fragment = None
        normalised_link = str(f).removesuffix("/")
        unique_links.add(normalised_link)
    return sorted(list(unique_links))


def extract_domain_from_url(url: str) -> Domain:
    """Extract full domain from URL and return it in a standard format."""

    url = url.strip()

    if not url.startswith("http"):
        url = f"https://{url}"

    try:
        parsed_url = furl(url)
    except ValueError as e:
        logger.warning(f"Skipping URL {url}: {e}")
        return None

    domain = parsed_url.host

    if domain.startswith("www."):
        domain = domain[4:]

    if "." not in domain and domain != "localhost":
        return None

    return domain
