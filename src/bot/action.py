"""Contains Bot actions.
Book website -> Book preview -> Book page link.
"""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse
from logging import getLogger
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .utils import wait_element_visible
from ..modules import Link, LinkFile
from ..utils import datetime_name, slugify


logger = getLogger(__name__)


class Action:
    """Bot actions to process links.

    Args:
        - driver (WebDriver): Selenium WebDriver.
        - links (list[Link]): List of links object.
        - timeout (int): Time to wait for element to be visible.
    """

    def __init__(self, driver: WebDriver, links: list[Link], timeout: int) -> None:
        self.driver: WebDriver = driver
        self.links: list[Link] = links
        self.timeout: int = timeout

    @staticmethod
    def __book_preview_to_page(link: str) -> str:
        """Book preview link to book page link.

        Args:
            - link (str): Book preview link.

        Returns:
            - str: Book page link without "page" query.
        """
        parser = urlparse(link)
        query = parse_qs(parser.query)
        subfolder_value: str = query.get("subfolder", "")[0]
        doc_value: str = query.get("doc", "")[0]
        page_link: str = f"https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc={doc_value}&format=jpg&subfolder={subfolder_value}"  # nopep8
        return page_link

    def __get_num_pages(self, driver: WebDriver) -> int:
        """Get number of pages from book preview link.
        Already in book preview link in Selenium.

        Args:
            - driver (WebDriver): Selenium WebDriver.

        Returns:
            - int: Number of pages.
        """
        pages: str = wait_element_visible(driver=driver, css_selector=".flowpaper_lblTotalPages", timeout=self.timeout).text.strip(" /")
        return int(pages)

    def preview_to_page_and_num_pages(self, link: str) -> tuple[str, int]:
        """Book preview link to book page link and get number of pages.

        Args:
            - link (str): Book preview link.

        Returns:
            - tuple[str, int]: Book page link and number of pages.
        """
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(link)
        wait_element_visible(
            driver=self.driver,
            css_selector="#pageContainer_0_documentViewer_textLayer",
            timeout=self.timeout,
        )
        preview_link: str = self.driver.current_url
        page_link: str = self.__book_preview_to_page(link=preview_link)
        pages: int = self.__get_num_pages(driver=self.driver)
        return page_link, pages

    def book_to_preview(self, link: str) -> list[str]:
        """Book website link to book preview link.

        Args:
            - link (str): Book website link.

        Returns:
            - list[str]: List of book preview link(s).
        """
        self.driver.get(link)
        view_online_button: list[WebElement] = self.driver.find_elements(By.CSS_SELECTOR, ".pdf-view.viewonline")
        preview_links: list[str] = []
        for preview_link_element in view_online_button:
            preview_link: str | None = preview_link_element.get_attribute("href")
            if preview_link is not None:
                preview_links.append(preview_link)
        logger.info('"%s": Found "%s" preview link(s)', link, len(preview_links))
        return preview_links

    def get_book_files_name(self) -> list[str]:
        """Get book's files' name from the book website.
        Already in book website in Selenium.

        Returns:
            - list[str]: List of book's files' name.
        """
        name_elements: list[WebElement] = self.driver.find_elements(By.CSS_SELECTOR, ".standard.title-bit.break-all > a")
        file_names: list[str] = [name_element.text.replace(".pdf", "") for name_element in name_elements]
        return file_names

    def book_handler(self, link: Link) -> Link:
        """Process book link handler.

        Args:
            - link (Link): Current link object.

        Returns:
            - Link: Processed link object.
        """
        preview_links: list[str] = self.book_to_preview(link=link.original_link)
        book_files_name: list[str] = self.get_book_files_name()
        link.name = slugify(self.driver.find_element(by=By.CSS_SELECTOR, value=".ds-div-head").text)
        processed_files: list[LinkFile] = []
        for i, preview_link in enumerate(preview_links):
            page_link, num_pages = self.preview_to_page_and_num_pages(link=preview_link)
            processed_files.append(LinkFile(page_link=page_link, num_pages=num_pages, name=book_files_name[i]))
        link.files = processed_files
        return link

    def preview_handler(self, link: Link) -> Link:
        """Process preview link handler.

        Args:
            - link (Link): Current link object.

        Returns:
            - Link: Processed link object.
        """
        page_link, num_pages = self.preview_to_page_and_num_pages(link=link.original_link)
        link.files = [LinkFile(page_link=page_link, num_pages=num_pages, name=datetime_name())]
        return link

    def action(self) -> list[Link]:
        """Convert all links to the page links format.

        Returns:
        - list[Link]: A list processed links object.
        """
        converted_links: list[Link] = []
        for link in self.links:
            match link.original_type:
                case "book":
                    logger.info('"%s": "%s"', link.original_link, link.original_type)
                    converted_links.append(self.book_handler(link=link))
                case "preview":
                    logger.info('"%s": "%s"', link.original_link, link.original_type)
                    converted_links.append(self.preview_handler(link=link))
                case "page":
                    converted_links.append(link)
        return converted_links
