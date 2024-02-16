"""Convert parse links to convert all the links to the page links format"""


from re import compile as re_compile, search as re_search
from .user_options import LinkFile, Link
from ..utils import logger
from ..utils.utils import datetime_name


PATTERN_BOOK = re_compile(
    r'^https?:\/\/ir\.vnulib\.edu\.vn\/handle\/VNUHCM\/\d+$')
PATTERN_PREVIEW = re_compile(
    r'^https?:\/\/ir\.vnulib\.edu\.vn\/flowpaper\/simple_document\.php\?(?=.*\bsubfolder=[^&]+\b)(?=.*\bbitsid=[^&]+\b)(?=.*\bdoc=\d*\b).*$')
PATTERN_PAGE = re_compile(
    r'https?:\/\/ir\.vnulib\.edu\.vn\/flowpaper\/services\/view\.php\?(?=.*\bdoc=\d*\b)(?=.*\bformat=jpg&\b)(?=.*\bsubfolder=[^&]+\b).*$')


class LinkParse:
    """Parse links to get the links' information

    Params:
        - links (list[Links]): List of links to parse
    """

    def __init__(self, links: list[Link]) -> None:
        self.links: list[Link] = links
        self.need_to_convert = False

    @staticmethod
    def categorise(link: str) -> str:
        """Categorise the links to the type of links

        Params:
            - link (str): Link to categorise

        Returns:
            - str: 'book', 'preview', 'page' or 'unknown'
        """
        if re_search(PATTERN_BOOK, link):
            return 'book'
        if re_search(PATTERN_PREVIEW, link):
            return 'preview'
        if re_search(PATTERN_PAGE, link):
            return 'page'
        return 'unknown'

    def parse(self) -> list[Link]:
        """Categorise links into types. With 'page' type, the book atrribute will be set

        Params:
            - None

        Returns:
        - list[Links]: List of categorised links
        """
        modified_links: list[Link] = []
        for link in self.links:
            link_type: str = self.categorise(link.original_link)
            match link_type:
                case 'book':
                    self.need_to_convert = True
                    link.original_type = 'book'
                    modified_links.append(link)
                case 'preview':
                    self.need_to_convert = True
                    link.original_type = 'preview'
                    modified_links.append(link)
                case 'page':
                    link.original_type = 'page'
                    link.files = [
                        LinkFile(page_link=link.original_link, num_pages=-1, name=datetime_name())]
                    modified_links.append(link)
                case _:
                    logger.warning(
                        msg=f'Unknown link type for: {link.original_link}')
        return modified_links
