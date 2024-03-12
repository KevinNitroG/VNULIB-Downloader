"""Download book's images"""

from __future__ import annotations

import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from itertools import count
from typing import Any, override
import requests
from requests.sessions import Session
from requests import Response
import urllib3
from logging import getLogger
from alive_progress import alive_bar
from .link_parse import Link, LinkFile
from ..constants import ERROR_PAGE_IMAGE_PATH
from ..utils import create_directory


logger = getLogger("vnulib_downloader")


def get_error_page_bytes() -> bytes:
    """Get the error image bytes from local.

    Returns:
        bytes: The error image bytes.
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        error_page_path = os.path.join(sys._MEIPASS, ERROR_PAGE_IMAGE_PATH)  # type: ignore # skipcq: PYL-W0212 # pylint: disable=protected-access # nopep8
    else:
        error_page_path = ERROR_PAGE_IMAGE_PATH
    with open(error_page_path, "rb") as file:
        content = file.read()
    return content


ERROR_PAGE_IMAGE: bytes = get_error_page_bytes()
OUT_PAGE_ERROR_TEXT: str = "Error:Error converting document"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DownloadCore:  # pylint: disable=too-few-public-methods
    """Download Core class for being inherited.

    Args:
        - link (LinkFile): Link object.
        - download_path (str): Path for images to be downloaded.
        - timeout (int): Timeout for Request.
    """

    def __init__(self, link: LinkFile, download_path: str, timeout: int) -> None:
        self.link: LinkFile = link
        self.download_path: str = download_path
        self.timeout: int = timeout
        self.session: Any

    def get_images_bytes(self, link: str, page: str) -> bytes:
        """Get images bytes.

        Args:
            - link (str): the page link.
            - page (str): The current page number to download.

        Return:
            - Bytes: The datas of images.
        """
        try:
            with self.session.get(link, stream=True, timeout=self.timeout, verify=False) as reponse:
                return reponse.content  # skipcq: BAN-B501, PTC-W6001
        except requests.exceptions.ReadTimeout:
            logger.error(msg=f'"{link}": Page "{page}" - Timeout')
            return ERROR_PAGE_IMAGE


class SingleThreadDownload(DownloadCore):
    """Single Thread download for unkown num pages.

    Args:
        - link (LinkFile): Link object.
        - download_path (str): Path for images to be downloaded.
        - timeout (int): Timeout for Request.
    """

    def __init__(self, link: LinkFile, download_path: str, timeout: int) -> None:
        super().__init__(link=link, download_path=download_path, timeout=timeout)
        self.session: Session = self.get_session()
        self.count = count(start=1, step=1)

    @staticmethod
    def get_session() -> Session:
        """Get session.

        Returns:
            - Session: Session.
        """
        return requests.Session()

    @override
    def get_images_bytes(self, link: str, page: str) -> bytes:
        """Get image's bytes, check valid page first.

        Args:
            - link (str): Link.
            - page (str): The current page number to download.

        Returns:
            - str: Text content of link.
        """
        try:
            response: Response = self.session.get(link, stream=True, timeout=self.timeout, verify=False)  # skipcq: BAN-B501, PTC-W6001
            return b"" if OUT_PAGE_ERROR_TEXT in response.text else response.content
        except requests.exceptions.ReadTimeout:
            logger.error(msg=f'"{link}": Page "{page}" - Timeout')
            return ERROR_PAGE_IMAGE

    def download(self) -> None:
        """Download."""
        self.session = requests.Session()  # pylint: disable=attribute-defined-outside-init
        with alive_bar() as bar:  # pylint: disable=disallowed-name
            while True:
                current_page: str = str(next(self.count))  # skipcq: PTC-W0063
                image_link: str = f"{self.link.page_link}&page={current_page}"
                image_path: str = os.path.join(self.download_path, f"image_{current_page}.jpg")
                if image_bytes := self.get_images_bytes(link=image_link, page=current_page):
                    with open(image_path, "wb") as file:  # skipcq: PTC-W6004
                        file.write(image_bytes)
                else:
                    break
                bar()  # pylint: disable=not-callable
        self.session.close()


class MultiThreadingDownload(DownloadCore):
    """Multi Threading download, only for known page.

    Args:
        - link (LinkFile): Link object.
        - download_path (str): Path for images to be downloaded.
        - timeout (int): Timeout for Request.
    """

    def __init__(self, link: LinkFile, download_path: str, timeout: int) -> None:
        super().__init__(link=link, download_path=download_path, timeout=timeout)
        self.thread_local = threading.local()
        self.session: Session = self.get_session()

    def get_session(self) -> Session:
        """Get session for thread.

        Returns:
            - Session: Session for thread.
        """
        if not hasattr(self.thread_local, "session"):
            self.thread_local.session = requests.Session()
        return self.thread_local.session

    def download_to_file(self, image_link: str, image_path: str, page: str) -> None:  # pylint: disable=disallowed-name
        """Multithreading download function for known page link (book | preview).

        Args:
            - image_link (str): Image link.
            - image_path (str): Image path.
            - page (str): The current page number to download.
        """
        with open(image_path, "wb") as file:  # skipcq: PTC-W6004
            file.write(self.get_images_bytes(link=image_link, page=page))
        self.bar()  # pylint: disable=not-callable

    def download(self) -> None:
        """Download images."""
        with alive_bar(total=self.link.num_pages) as self.bar, ThreadPoolExecutor() as executor:  # pylint: disable=[disallowed-name, attribute-defined-outside-init]
            for page_num in range(1, self.link.num_pages + 1):
                sub_link: str = f"{self.link.page_link}&page={page_num}"
                image_path: str = os.path.join(self.download_path, f"image_{page_num}.jpg")
                executor.submit(self.download_to_file, sub_link, image_path, str(page_num))


class DownloadIMG:
    """Download book's images.

    Args:
        - links (list[Link]): The list of links object.
        - download_directory (str): Download directory.
        - timeout (int): Timeout (s) for Request to fetch each image.
    """

    def __init__(self, links: list[Link], download_directory: str, timeout: int) -> None:
        self.links: list[Link] = links
        self.download_directory: str = download_directory
        self.timeout: int = timeout

    def book_handler(self, links: Link) -> None:
        """Download images from the book link.

        Args:
            links (Link): Book link.
        """
        folder_path: str = os.path.join(self.download_directory, links.name)
        if create_directory(folder_path):
            for link in links.files:
                sub_path: str = os.path.join(folder_path, link.name)
                if create_directory(sub_path):
                    MultiThreadingDownload(link=link, download_path=sub_path, timeout=self.timeout).download()

    def preview_handler(self, link: LinkFile) -> None:
        """Download images from the preview & page link (known num pages).

        Args:
            link (LinkFile): LinkFile of Preview link.
        """
        folder_path: str = os.path.join(self.download_directory, link.name)
        if create_directory(folder_path):
            MultiThreadingDownload(link=link, download_path=folder_path, timeout=self.timeout).download()

    def page_handler(self, link: LinkFile) -> None:
        """Dowload All book's images from page link (for unkown num pages).

        Args:
            - link (LinkFile): LinkFile of Page link.
        """
        folder_path: str = os.path.join(self.download_directory, link.name)
        if create_directory(folder_path, force=True):
            SingleThreadDownload(link=link, download_path=folder_path, timeout=self.timeout).download()

    def dowload(self) -> None:
        """Dowload Images from list of Link."""
        for link in self.links:
            logger.info(msg=f'Downloading: "{link.original_link}"')
            match link.original_type:
                case "book":
                    self.book_handler(link)
                case "preview":
                    self.preview_handler(link.files[0])
                case "page":
                    if link.files[0].num_pages > 1:
                        self.preview_handler(link.files[0])
                    else:
                        self.page_handler(link.files[0])
                case _:
                    pass
            logger.info(msg=f'Done: "{link.original_link}"')
