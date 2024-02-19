"""Categorise links, remove invalid links"""


from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from re import compile as re_compile, search as re_search
from .user_options import LinkFile, Link
from ..utils import logger
from ..utils.utils import datetime_name


PATTERN_BOOK = re_compile(
    r'^https?:\/\/ir\.vnulib\.edu\.vn\/handle\/VNUHCM\/\d+$')
PATTERN_PREVIEW = re_compile(
    r'^https?:\/\/ir\.vnulib\.edu\.vn\/flowpaper\/simple_document\.php\?(?=.*\bsubfolder=[^&]+\b)(?=.*\bbitsid=[^&]+\b)(?=.*\bdoc=\d*\b).*$')  # pylint: disable=line-too-long
PATTERN_PAGE = re_compile(
    r'https?:\/\/ir\.vnulib\.edu\.vn\/flowpaper\/services\/view\.php\?(?=.*\bdoc=\d*\b)(?=.*\bformat=jpg&\b)(?=.*\bsubfolder=[^&]+\b).*$')  # pylint: disable=line-too-long


class LinkParse:
    """Parse links to categorise and remove invalid links

    Args:
        - links (list[Links]): List of links to parse
    """

    def __init__(self, links: list[Link]) -> None:
        self.links: list[Link] = links
        self.need_to_process: bool = False

    @staticmethod
    def categorise(link: str) -> str:
        """Categorise the links using regex

        Args:
            - link (str): Link to categorise

        Returns:
            - str: 'book', 'preview', 'page' or ''
        """
        if re_search(PATTERN_BOOK, link):
            return 'book'
        if re_search(PATTERN_PREVIEW, link):
            return 'preview'
        if re_search(PATTERN_PAGE, link):
            return 'page'
        return ''

    @staticmethod
    def remove_page_query(link: str) -> str:
        """Parse the link to remove "page" query

        Args:
            - link (str): Link to parse

        Returns:
            - str: Parsed link without "page" query
        """
        parser = urlparse(link)
        query = parse_qs(parser.query)
        query.pop('page', None)
        parsed_query: str = urlencode(query, doseq=True)
        parsed_url: str = urlunparse(
            (parser.scheme, parser.netloc, parser.path,
             parser.params, parsed_query, parser.fragment))
        return parsed_url

    @staticmethod
    def process_page(link: Link) -> Link:
        """Process page link handler

        Args:
            - link (Link): Current link object

        Returns:
            - Link: Processed link object
        """
        link.original_type = 'page'
        page_link: str = LinkParse.remove_page_query(link=link.original_link)
        link.files = [LinkFile(
            page_link=page_link, num_pages=-1, name=datetime_name())]
        return link

    def parse(self) -> list[Link]:
        """Categorise links, remvoe invalid links, pre-set for 'page' type links

        Returns:
        - list[Links]: List of parsed links object
        """
        modified_links: list[Link] = []
        for link in self.links:
            link_type: str = self.categorise(link.original_link)
            match link_type:
                case 'book':
                    self.need_to_process = True
                    link.original_type = 'book'
                    modified_links.append(link)
                case 'preview':
                    self.need_to_process = True
                    link.original_type = 'preview'
                    modified_links.append(link)
                case 'page':
                    link = self.process_page(link)
                    modified_links.append(link)
                case _:
                    logger.warning(
                        msg='Unknown link type for: '
                        f'\'{link.original_link}\'')
        return modified_links
