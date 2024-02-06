"""Convert parse links to convert all the links to the page links format"""


from re import compile as re_compile, search as re_search
from selenium.webdriver.chrome.webdriver import WebDriver
from .user_options import Links
from ..bot.action import Action
from ..utils import logger


PATTERN_BOOK = re_compile(
    r'http[s]?://ir\.vnulib\.edu\.vn/handle/VNUHCM/\d+')
PATTERN_PREVIEW = re_compile(
    r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/simple_document\.php\?subfolder=.+&doc=\d+&bitsid=.+')
PATTERN_PAGE = re_compile(
    r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/services/view\.php\?.+(page=\d+).+')


class LinkParse:
    """Parse links to get the links' information

    Params:
        - links (list[Links]): List of links to parse
    """

    def __init__(self, links: list[Links]) -> None:
        self.links: list[Links] = links
        self.links_list: list[str] = [link.original_link for link in links]
        self.need_to_convert = False

    @staticmethod
    def convert(driver: WebDriver, links: list[Links]) -> list[Links]:
        """Convert all links to the page links format

        Params:
            - driver (WebDriver): The WebDriver
            - links (list[Links]): List of links to convert

        Returns:
        - list: A list contains converted links to page links format
        """
        converted_links: list[Links] = []
        for (i, _) in enumerate(links):
            match links[i].original_type:
                case 'book':
                    converted_link: str = Action.book_web_to_preview(
                        driver=driver, link=links[i].original_link)
                    converted_link, pages = Action.book_preview_to_page(
                        driver=driver, link=converted_link)
                    links[i].link = converted_link
                    links[i].pages = pages
                    converted_links.append(links[i])
                    logger.debug(msg=f'Converted {links[i].original_link} '
                                 f'to {converted_link}')
                case 'preview':
                    converted_link, pages = Action.book_preview_to_page(
                        driver=driver, link=links[i].original_link)
                    links[i].link = converted_link
                    links[i].pages = pages
                    converted_links.append(links[i])
                    logger.debug(msg=f'Converted {links[i].original_link} '
                                 f'to {converted_link}')
                case 'page':
                    logger.debug(msg='Not need to convert '
                                 f'{links[i].original_link}')
                    continue
                case _:
                    logger.warning(
                        msg=f'Skip downloading link: {links[i].original_link}')
        logger.debug(msg=f'Converted links: {converted_links}')
        return converted_links

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

    def parse(self) -> list[Links]:
        """Setup links to return the list of dictionary contain links' information

        Params:
            - None

        Returns:
        - list[Links]: List of parsed links' information
        """
        for (i, _) in enumerate(self.links):
            link_type: str = self.categorise(self.links[i].original_link)
            match link_type:
                case 'book':
                    self.links[i].original_type = 'book'
                    self.need_to_convert = True
                case 'preview':
                    self.links[i].original_type = 'preview'
                    self.need_to_convert = True
                case 'page':
                    self.links[i].original_type = 'page'
                    self.links[i].link = self.links[i].original_link
                case _:
                    self.links[i].original_type = 'unknown'
                    logger.warning(
                        msg=f'Unknown link type: {self.links[i].original_link}')
        return self.links
