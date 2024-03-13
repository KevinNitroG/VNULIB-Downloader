"""Categorise links, remove invalid links."""

from __future__ import annotations

from re import compile as re_compile
from re import search as re_search
from time import sleep
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse
from logging import getLogger
from .user_options import Link, LinkFile
from ..utils.utils import datetime_name


logger = getLogger(__name__)


PATTERN_BOOK = re_compile(r"^https?:\/\/ir\.vnulib\.edu\.vn\/handle\/VNUHCM\/\d+$")
PATTERN_PREVIEW = re_compile(r"^https?:\/\/ir\.vnulib\.edu\.vn\/flowpaper\/(simple_document\.php)?\?(?=.*\bbitsid=[^&]+\b).*$")
PATTERN_PAGE = re_compile(r"https?:\/\/ir\.vnulib\.edu\.vn\/flowpaper\/services\/view\.php\?(?=.*\bdoc=\d*\b)(?=.*\bformat=jpg&\b)(?=.*\bsubfolder=[^&]+\b).*$")


class LinkParse:
    """Parse links to categorise and remove invalid links.

    Args:
        - links (list[Links]): List of links to parse.
    """

    def __init__(self, links: list[Link]) -> None:
        self.links: list[Link] = links
        self.need_to_process: bool = False

    @staticmethod
    def categorise(link: str) -> str:
        """Categorise the links using regex.

        Args:
            - link (str): Link to categorise.

        Returns:
            - str: ``book``, ``preview``, ``page`` or empty string.
        """
        if re_search(PATTERN_BOOK, link):
            return "book"
        if re_search(PATTERN_PREVIEW, link):
            return "preview"
        return "page" if re_search(PATTERN_PAGE, link) else ""

    @staticmethod
    def __get_page_num_from_page_query(link: str) -> int:
        """Get limit number of pages from page query (use for ``page`` link).

        Args:
            link (str): ``page`` link.

        Returns:
            int: Number of pages.
        """
        query: dict[str, list[str]] = parse_qs(urlparse(link).query)
        current_num_pages: list[str] | None = query.get("page")
        if current_num_pages is not None:
            int_current_num_pages: int = int(current_num_pages[0])
            return int_current_num_pages if int_current_num_pages > 1 else -1
        return -1

    @staticmethod
    def remove_page_query(link: str) -> str:
        """Parse the link to remove ``page`` query.

        Args:
            - link (str): Link to parse.

        Returns:
            - str: Parsed link without ``page`` query.
        """
        parser = urlparse(link)
        query = parse_qs(parser.query)
        query.pop("page", None)
        parsed_query: str = urlencode(query, doseq=True)
        parsed_url: str = urlunparse(
            (
                parser.scheme,
                parser.netloc,
                parser.path,
                parser.params,
                parsed_query,
                parser.fragment,
            )
        )
        return parsed_url

    @staticmethod
    def process_page(link: Link) -> Link:
        """Process ``page`` link handler.

        Args:
            - link (Link): Current link page object.

        Returns:
            - Link: Processed link page object.
        """
        link.original_type = "page"
        page_link: str = LinkParse.remove_page_query(link=link.original_link)
        num_pages: int = LinkParse.__get_page_num_from_page_query(link=link.original_link)
        link.files = [LinkFile(page_link=page_link, num_pages=num_pages, name=datetime_name())]
        return link

    def parse(self) -> list[Link]:
        """Categorise links, remvoe invalid links, pre-set for ``page`` type links.

        Returns:
        - list[Links]: List of parsed links object.
        """
        modified_links: list[Link] = []
        for link in self.links:
            link_type: str = self.categorise(link.original_link)
            match link_type:
                case "book":
                    self.need_to_process = True
                    link.original_type = "book"
                    modified_links.append(link)
                case "preview":
                    self.need_to_process = True
                    link.original_type = "preview"
                    modified_links.append(link)
                case "page":
                    link = self.process_page(link)
                    modified_links.append(link)
                    logger.info(msg=f'"{link.original_link}": "page" - "{link.files[0].num_pages}" page(s)')
                    sleep(0.1)  # Sleep to avoid same folder name in any case
                case _:
                    logger.warning(msg=f'"{link.original_link}": Unknown link type')
        return modified_links
