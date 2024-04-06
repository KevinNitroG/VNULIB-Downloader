"""Categorise links, remove invalid links."""

from __future__ import annotations

from logging import getLogger
from re import compile as re_compile
from re import search as re_search
from time import sleep
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from ..utils.utils import datetime_name
from .user_options import Link, LinkFile

logger = getLogger(__name__)


class LinkParse:
    """Parse links to categorise and remove invalid links."""

    _PATTERN_BOOK = re_compile(r"^https?:\/\/ir\.vnulib\.edu\.vn\/handle\/VNUHCM\/\d+$")
    _PATTERN_PREVIEW = re_compile(r"^https?:\/\/ir\.vnulib\.edu\.vn\/flowpaper\/(simple_document\.php)?\?(?=.*\bbitsid=[^&]+\b).*$")
    _PATTERN_PAGE = re_compile(r"https?:\/\/ir\.vnulib\.edu\.vn\/flowpaper\/services\/view\.php\?(?=.*\bdoc=\d*\b)(?=.*\bformat=jpg&\b)(?=.*\bsubfolder=[^&]+\b).*$")

    def __init__(self, links: list[Link]) -> None:
        """Initialise for LinkParse class.

        Args:
            links (list[Links]): List of links to parse.
        """
        self.links: list[Link] = links
        self.need_to_process: bool = False

    def _categorise(self, link: str) -> str:
        """Categorise the links using regex.

        Args:
            link (str): Link to categorise.

        Returns:
            str: ``book``, ``preview``, ``page`` or empty string.
        """
        if re_search(self._PATTERN_BOOK, link):
            return "book"
        if re_search(self._PATTERN_PREVIEW, link):
            return "preview"
        return "page" if re_search(self._PATTERN_PAGE, link) else ""

    @staticmethod
    def _get_page_num_from_page_query(link: str) -> int:
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
    def _remove_page_query(link: str) -> str:
        """Parse the link to remove ``page`` query.

        Args:
            link (str): Link to parse.

        Returns:
            str: Parsed link without ``page`` query.
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
    def _page_handler(link: Link) -> Link:
        """Process ``page`` link handler.

        Args:
            link (Link): Current link page object.

        Returns:
            Link: Processed link page object.
        """
        link.original_type = "page"
        page_link: str = LinkParse._remove_page_query(link=link.original_link)
        num_pages: int = LinkParse._get_page_num_from_page_query(link=link.original_link)
        link.files = [LinkFile(page_link=page_link, num_pages=num_pages, name=datetime_name())]
        return link

    def parse(self) -> None:
        """Categorise links, remove invalid links, pre-set for ``page`` type links.
        Then it will replace the link in object.
        """
        modified_links: list[Link] = []
        for link in self.links:
            link_type: str = self._categorise(link.original_link)
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
                    link = self._page_handler(link)
                    modified_links.append(link)
                    num_pages: str = f'"{link.files[0].num_pages}" page(s)' if link.files[0].num_pages != -1 else "no limit"
                    logger.info('"%s": "page" - %s', link.original_link, num_pages)
                    sleep(0.1)  # Sleep to avoid same folder name in any case
                case _:
                    logger.warning('"%s": Unknown link type', link.original_link)
        self.links = modified_links
