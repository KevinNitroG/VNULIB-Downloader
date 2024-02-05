"""Convert parse links to convert all the links to the page links format"""


from re import compile as re_compile, search as re_search
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from .user_options import Links
from ..bot import Action
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
    def convert(driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver, links: list[Links]) -> list[Links]:
        """Convert all links to the page links format

        Params:
            - driver (ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver): The WebDriver
            - links (list[Links]): List of links to convert

        Returns:
        - list: A list contains converted links to page links format
        """
        converted_links: list[Links] = []
        for (i, _) in enumerate(links):
            match links[i].original_type:
                case 'book':
                    logger.info(
                        msg=f'Converting {links[i].original_link} to page link')
                    converted_link: str = Action.book_web_to_page(
                        driver=driver, link=links[i].original_link)
                    links[i].link = converted_link
                    converted_links.append(links[i])
                    logger.info(
                        msg=f'Done for {links[i].original_link}')
                case 'preview':
                    logger.info(
                        msg=f'Converting {links[i].original_link} to page link')
                    converted_link: str = Action.book_preview_to_page(
                        driver=driver, link=links[i].original_link)
                    links[i].link = converted_link
                    converted_links.append(links[i])
                    logger.info(
                        msg=f'Done for {links[i].original_link}')
                case 'page':
                    converted_links.append(links[i])
                case _:
                    logger.warning(
                        msg=f'Skip downloading link: {links[i].original_link}')
            logger.debug(msg=f'Converted links: {converted_links}')
        return converted_links

    @staticmethod
    def remove_page_query(link: str) -> str:
        """Parse the link to remove "page" query

        Params:
            - link (str): Link to parse

        Returns:
            - str: Parsed link without "page" query
        """
        parser = urlparse(link)
        query = parse_qs(parser.query)
        query.pop('page', None)
        parsed_query = urlencode(query, doseq=True)
        parsed_url = urlunparse(
            (parser.scheme, parser.netloc, parser.path, parser.params, parsed_query, parser.fragment))
        return parsed_url

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
                case _:
                    self.links[i].original_type = 'unknown'
                    logger.warning(
                        msg=f'Unknown link type: {self.links[i].original_link}')
        return self.links
