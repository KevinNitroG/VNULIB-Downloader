"""Convert parse links to convert all the links to the page links format"""


from selenium.webdriver.chrome.webdriver import WebDriver
from src.bot import Action

from src.utils import logger


class ConvertParseLink:
    """Convert parse links to convert all the links to the page links format

    Params:
        - driver (WebDriver): Selenium WebDriver
        - links (list[dict]): List of links information
    """

    def __init__(self, driver: WebDriver, links) -> None:
        self.driver: WebDriver = driver
        self.links: list[dict] = links

    def convert(self) -> list[dict]:
        """Convert all links to the page links format

        Returns:
        - list: A list contains converted links to page links format
        """
        converted_links: list[dict] = []
        for link in self.links:
            match link['original_type']:
                case 'preview':
                    logger.info(
                        msg=f'Converting {link["original_link"]} to page link')
                    converted_link: str = Action.book_preview_to_page(
                        driver=self.driver, url=link['original_link'])
                    link.update({'link': converted_link})
                    converted_links.append(link)
                    logger.info(
                        msg=f'Done for {link["original_link"]}')
                case 'book':
                    logger.info(
                        msg=f'Converting {link["original_link"]} to page link')
                    converted_link: str = Action.book_web_to_page(
                        driver=self.driver, url=link['original_link'])
                    link.update({'link': converted_link})
                    converted_links.append(link)
                    logger.info(
                        msg=f'Done for {link["original_link"]}')
                case _:
                    converted_links.append(link)
        return converted_links
