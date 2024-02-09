"""Contains Bot actions: Book website -> Book preview -> Book page link"""


from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import urllib3
from .utils import wait_element_visible
from ..utils import logger


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Action:
    """Bot actions for the bot to perform"""

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
        parsed_query: str = urlencode(query, doseq=True)
        parsed_url: str = urlunparse(
            (parser.scheme, parser.netloc, parser.path,
             parser.params, parsed_query, parser.fragment))
        return parsed_url

    @staticmethod
    def get_num_pages(driver: WebDriver) -> int:
        """Get number of pages from book preview link

        Params:
            - driver (WebDriver): Selenium WebDriver

        Returns:
            - int: Number of pages
        """
        pages: str = wait_element_visible(
            driver=driver, css_selector='.flowpaper_lblTotalPages').text.strip(' /')
        return int(pages)

    @staticmethod
    def book_preview_to_page(link: str) -> str:
        """Book preview link to book page link and return number of pages

        Params:
            - link (str): Book preview link

        Returns:
            - list[str]: Book page link
        """
        parser = urlparse(link)
        query = parse_qs(parser.query)
        subfolder_value: str = query.get('subfolder', '')[0]
        doc_value: str = query.get('doc', '')[0]
        page_link: str = f'https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc={
            doc_value}&format=jpg&subfolder={subfolder_value}'
        return page_link

    @staticmethod
    def book_preview_to_page_and_pages(driver: WebDriver, link: str) -> tuple[str, int]:
        """Book preview link to book page link and return number of pages

        Params:
            - driver (WebDriver): Selenium WebDriver
            - link (str): Book preview link

        Returns:
            - tuple[str, int]: Book page link and number of pages
        """
        driver.switch_to.window(driver.window_handles[0])
        driver.get(link)
        wait_element_visible(
            driver=driver, css_selector='#pageContainer_0_documentViewer_textLayer')
        preview_link: str = driver.current_url
        page_link: str = Action.book_preview_to_page(link=preview_link)
        pages: int = Action.get_num_pages(driver=driver)
        return page_link, pages

    # @staticmethod
    # def book_preview_to_page(link: str) -> str:
    #     """Book preview link to book page link

    #     Params:
    #         - link (str): Book preview link

    #     Returns:
    #         - str: Converted link to book page link
    #     """
    #     parser = urlparse(link)
    #     query = parse_qs(parser.query)
    #     doc_value: str = query.get('doc', '')[0]
    #     subfolder_value: str = query.get('subfolder', '')[0]
    #     converted_link: str = f'https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc={
    #         doc_value}&format=jpg&subfolder={subfolder_value}'
    #     return converted_link

    @staticmethod
    def book_web_to_preview(driver: WebDriver, link: str) -> list[str]:
        """Book website link to book preview link

        Params:
            - driver (WebDriver): Selenium WebDriver
            - link (str): Book website link

        Returns:
            - list[str]: List of book preview link(s)
        """
        driver.get(link)
        view_online_button: list[WebElement] = driver.find_elements(
            By.CSS_SELECTOR, '.pdf-view.viewonline')
        preview_links: list[str] = []
        for preview_link_element in view_online_button:
            preview_link: str | None = preview_link_element.get_attribute(
                'href')
            if preview_link is not None:
                preview_links.append(preview_link)
        logger.info(msg=f'Found {len(preview_links)} '
                    f'preview link(s) for {link}')
        return preview_links
