"""Convert parse links to convert all the links to the page links format"""


from re import compile as re_compile, search as re_search
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from src.bot import Action
from src.utils import logger


class LinkParse:
    """Parse links to get the raw list of link information

    Params:
        - links (list[str]): List of links to parse
    """

    def __init__(self, links: list[str]) -> None:
        self.links: list[str] = links
        self.pattern_book = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/handle/VNUHCM/\d+')
        self.pattern_preview = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/simple_document\.php\?subfolder=.+&doc=\d+&bitsid=.+')
        self.pattern_page = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/services/view\.php\?.+(page=\d+).+')
        self.need_to_convert = False

    def setup(self) -> list[dict]:
        """Setup links to return the list of dictionary contain links' information

        Params:
            - None

        Returns:
        - list[dict]: List of dictionary contain parsed links' information
        """
        parsed_links: list[dict] = []
        for link in self.links:
            dict_link = {}
            dict_link.update({'original_link': link})
            if re_search(self.pattern_page, link):
                dict_link.update({'original_type': 'page'})
                dict_link.update({'link': link})
                dict_link.update({'page_number': -1})
            elif re_search(self.pattern_preview, link):
                dict_link.update({'original_type': 'preview'})
                self.need_to_convert = True
            elif re_search(self.pattern_book, link):
                dict_link.update({'original_type': 'book'})
                self.need_to_convert = True
            else:
                dict_link.update({'original_type': 'unknown'})
                logger.warning(
                    msg=f'Unknown link type: {link}')
            parsed_links.append(dict_link)
        return parsed_links

    @staticmethod
    def convert(driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver, links_dict: list[dict]) -> list[dict]:
        """Convert all links to the page links format

        Returns:
        - list: A list contains converted links to page links format
        """
        converted_links: list[dict] = []
        for link_dict in links_dict:
            match link_dict['original_type']:
                case 'page':
                    converted_links.append(link_dict)
                case 'preview':
                    logger.info(
                        msg=f'Converting {link_dict["original_link"]} to page link')
                    converted_link: str = Action.book_preview_to_page(
                        driver=driver, url=link_dict['original_link'])
                    link_dict.update({'link': converted_link})
                    converted_links.append(link_dict)
                    logger.info(
                        msg=f'Done for {link_dict["original_link"]}')
                case 'book':
                    logger.info(
                        msg=f'Converting {link_dict["original_link"]} to page link')
                    converted_link: str = Action.book_web_to_page(
                        driver=driver, url=link_dict['original_link'])
                    link_dict.update({'link': converted_link})
                    converted_links.append(link_dict)
                    logger.info(
                        msg=f'Done for {link_dict["original_link"]}')
                case _:
                    logger.warning(
                        msg=f'Skip downloading link: {link_dict["original_link"]}')
        return converted_links

    @staticmethod
    def parse_link(link: str) -> str:
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
