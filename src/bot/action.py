"""Contains Bot actions: Book website -> Book preview -> Book page link"""


from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import urllib3
from .utils import wait_element_visible
from ..utils import logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Action:
    """Bot actions for the bot to perform"""

    @staticmethod
    def __remove_page_query(link: str) -> str:
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
            (parser.scheme, parser.netloc, parser.path,
             parser.params, parsed_query, parser.fragment))
        return parsed_url

    @staticmethod
    def book_preview_to_page_and_num_page(driver: WebDriver, link: str) -> tuple[str, int]:
        """Book preview link to book page link and return number of pages

        Params:
            - driver (WebDriver): Selenium WebDriver
            - link (str): Book preview link

        Returns:
            - list[str]: Page link from book preview link
            - int: Number of pages
        """
        driver.get(link)
        wait_element_visible(
            driver=driver, css_selector='#pageContainer_0_documentViewer')
        driver.execute_script('window.scrollTo(0, 5000)')
        sleep(1)
        driver.refresh()
        page_0_image: WebElement = wait_element_visible(
            driver=driver, css_selector='#page_0_documentViewer')
        page_0_image_link: str | None = driver.execute_script(
            "return arguments[0].getAttribute('src');", page_0_image)
        pages: str | None = wait_element_visible(
            driver=driver, css_selector='.flowpaper_lblTotalPages.flowpaper_tblabel').get_attribute('innerHTML')
        if page_0_image_link is not None and pages is not None:
            converted_link: str = Action.__remove_page_query(
                link=page_0_image_link)
            return converted_link, int(pages.strip(' /'))
        return '', -1

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
