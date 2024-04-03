"""Contains Bot actions.
Book website -> Book preview -> Book page link.
"""

from __future__ import annotations

from logging import getLogger
from urllib.parse import parse_qs, urlparse

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from ..modules import Link, LinkFile
from ..utils import datetime_name, slugify
from .utils import wait_element_visible

logger = getLogger(__name__)


class Action:
    """Bot actions to process links."""

    def __init__(self, driver: WebDriver, links: list[Link], timeout: int) -> None:
        """Initialise Action class.

        Args:
            driver (WebDriver): Selenium WebDriver.
            links (list[Link]): List of links object.
            timeout (int): Time to wait for element to be visible.
        """
        self._driver: WebDriver = driver
        self.links: list[Link] = links
        self._timeout: int = timeout

    @staticmethod
    def _book_preview_to_page(link: str) -> str:
        """Book preview link to book page link.

        Args:
            link (str): Book preview link.

        Returns:
            str: Book page link without "page" query.
        """
        parser = urlparse(link)
        query = parse_qs(parser.query)
        subfolder_value: str = query.get("subfolder", "")[0]
        doc_value: str = query.get("doc", "")[0]
        page_link: str = f"https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc={doc_value}&format=jpg&subfolder={subfolder_value}"  # nopep8
        return page_link

    def _get_num_pages(self, driver: WebDriver) -> int:
        """Get number of pages from book preview link.
        Already in book preview link in Selenium.

        Args:
            driver (WebDriver): Selenium WebDriver.

        Returns:
            int: Number of pages.
        """
        pages: str = wait_element_visible(driver=driver, css_selector=".flowpaper_lblTotalPages", timeout=self._timeout).text.strip(" /")
        return int(pages)

    def _preview_to_page_and_num_pages(self, link: str) -> tuple[str, int]:
        """Book preview link to book page link and get number of pages.

        Args:
            link (str): Book preview link.

        Returns:
            tuple[str, int]: Book page link and number of pages.
        """
        self._driver.switch_to.window(self._driver.window_handles[0])
        self._driver.get(link)
        wait_element_visible(
            driver=self._driver,
            css_selector="#pageContainer_0_documentViewer_textLayer",
            timeout=self._timeout,
        )
        preview_link: str = self._driver.current_url
        page_link: str = self._book_preview_to_page(link=preview_link)
        pages: int = self._get_num_pages(driver=self._driver)
        return page_link, pages

    def _book_to_preview(self, link: str) -> list[str]:
        """Book website link to book preview link.

        Args:
            link (str): Book website link.

        Returns:
            list[str]: List of book preview link(s).
        """
        self._driver.get(link)
        view_online_button: list[WebElement] = self._driver.find_elements(By.CSS_SELECTOR, ".pdf-view.viewonline")
        preview_links: list[str] = []
        for preview_link_element in view_online_button:
            preview_link: str | None = preview_link_element.get_attribute("href")
            if preview_link is not None:
                preview_links.append(preview_link)
        logger.info('"%s": Found "%s" preview link(s)', link, len(preview_links))
        return preview_links

    def _get_book_files_name(self) -> list[str]:
        """Get book's files' name from the book website.
        Already in book website in Selenium.

        Returns:
            list[str]: List of book's files' name.
        """
        name_elements: list[WebElement] = self._driver.find_elements(By.CSS_SELECTOR, ".standard.title-bit.break-all > a")
        file_names: list[str] = [name_element.text.replace(".pdf", "") for name_element in name_elements]
        return file_names

    def _book_handler(self, link: Link) -> Link:
        """Process book link handler.

        Args:
            link (Link): Current link object.

        Returns:
            Link: Processed link object.
        """
        preview_links: list[str] = self._book_to_preview(link=link.original_link)
        book_files_name: list[str] = self._get_book_files_name()
        link.name = slugify(self._driver.find_element(by=By.CSS_SELECTOR, value=".ds-div-head").text)
        processed_files: list[LinkFile] = []
        for i, preview_link in enumerate(preview_links):
            page_link, num_pages = self._preview_to_page_and_num_pages(link=preview_link)
            processed_files.append(LinkFile(page_link=page_link, num_pages=num_pages, name=slugify(book_files_name[i])))
        link.files = processed_files
        return link

    def _preview_handler(self, link: Link) -> Link:
        """Process preview link handler.

        Args:
            link (Link): Current link object.

        Returns:
            Link: Processed link object.
        """
        page_link, num_pages = self._preview_to_page_and_num_pages(link=link.original_link)
        link.files = [LinkFile(page_link=page_link, num_pages=num_pages, name=datetime_name())]
        return link

    def run(self) -> None:
        """Convert all links to the page links format.
        Then replace links attribute of object.
        """
        converted_links: list[Link] = []
        for link in self.links:
            match link.original_type:
                case "book":
                    logger.info('"%s": "%s"', link.original_link, link.original_type)
                    converted_links.append(self._book_handler(link=link))
                case "preview":
                    logger.info('"%s": "%s"', link.original_link, link.original_type)
                    converted_links.append(self._preview_handler(link=link))
                case "page":
                    converted_links.append(link)
        self.links = converted_links
