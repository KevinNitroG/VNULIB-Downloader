"""Download book's images"""


import os
import sys
from itertools import count
from concurrent.futures import ThreadPoolExecutor
import threading
from typing import override
import requests
import urllib3
from alive_progress import alive_bar
from .link_parse import LinkFile, Link
from ..utils.utils import create_directory
from ..utils import logger
from ..constants import ERROR_PAGE_IMAGE_PATH


def get_error_page_bytes() -> bytes:
    """Get the error image bytes from local

    Returns:
        bytes: The error image bytes
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        error_page_path = os.path.join(sys._MEIPASS, ERROR_PAGE_IMAGE_PATH)  # type: ignore # skipcq: PYL-W0212 # pylint: disable=protected-access # nopep8
    else:
        error_page_path = ERROR_PAGE_IMAGE_PATH
    with open(error_page_path, 'rb') as file:
        content = file.read()
    return content


ERROR_PAGE_IMAGE: bytes = get_error_page_bytes()
OUT_PAGE_ERROR_TEXT: str = 'Error:Error converting document'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SingleThreadDownload:
    """Single Thread download for unkown num pages

    Args:
        - link (LinkFile): Link object
        - download_path (str): Path for images to be downloaded
        - timeout (int): Timeout for Request
    """

    def __init__(self, link: LinkFile, download_path: str, timeout: int) -> None:
        self.link: LinkFile = link
        self.download_path: str = download_path
        self.timeout: int = timeout

    def get_images_bytes(self, link: str) -> bytes:
        """Get images bytes

        Args:
            - link (str): the page link

        Return:
            - Bytes: The datas of images
        """
        try:
            with self.session.get(link, stream=True, timeout=self.timeout, verify=False) as reponse:
                return reponse.content  # skipcq: BAN-B501, PTC-W6001
        except requests.exceptions.ReadTimeout:
            logger.error(msg=f'Error page for {link}')
            return ERROR_PAGE_IMAGE

    def get_content_pages(self, link: str) -> str:
        """Get text from page

        Args:
            - link (str): Link

        Returns:
            - str: Text content of link
        """
        return requests.get(link, stream=True, timeout=self.timeout, verify=False).text  # skipcq: BAN-B501, PTC-W6001

    def download(self) -> None:
        """Download"""
        self.session = requests.Session()  # pylint: disable=attribute-defined-outside-init
        page_num = count(start=1)
        with alive_bar() as bar:  # pylint: disable=disallowed-name
            while True:
                current_page: str = str(next(page_num))
                image_link: str = f'{self.link.page_link}&page={current_page}'
                image_path: str = os.path.join(self.download_path, f'image_{current_page}.jpg')
                if OUT_PAGE_ERROR_TEXT in self.get_content_pages(image_link):
                    break
                with open(image_path, 'wb') as file:  # skipcq: PTC-W6004
                    file.write(self.get_images_bytes(image_link))
                bar()  # pylint: disable=not-callable


class MultiThreadingDownload(SingleThreadDownload):
    """Multi Threading download, only for known page

    Args:
        - link (LinkFile): Link object
        - download_path (str): Path for images to be downloaded
        - timeout (int): Timeout for Request
    """

    def __init__(self, link: LinkFile, download_path: str, timeout: int) -> None:
        super().__init__(link=link, download_path=download_path, timeout=timeout)
        self.thread_local = threading.local()
        self.session = self.get_session()

    def get_session(self):
        """Get session for thread

        Returns:
            - Session: Session for thread
        """
        if not hasattr(self.thread_local, "session"):
            self.thread_local.session = requests.Session()
        return self.thread_local.session

    def download_to_file(self, image_link: str, image_path: str) -> None:  # pylint: disable=disallowed-name
        """Multithreading download function for known page link (book | preview)

        Args:
            - image_link (str): Image link
            - image_path (str): Image path
        """
        with open(image_path, 'wb') as file:  # skipcq: PTC-W6004
            file.write(self.get_images_bytes(image_link))
        self.bar()  # pylint: disable=not-callable

    @override
    def download(self) -> None:
        """Download images"""
        with alive_bar(self.link.num_pages) as self.bar:  # pylint: disable=[disallowed-name, attribute-defined-outside-init]
            with ThreadPoolExecutor() as executor:
                for page_num in range(1, self.link.num_pages + 1):
                    sub_link: str = f'{self.link.page_link}&page={page_num}'
                    image_path: str = os.path.join(self.download_path, f'image_{page_num}.jpg')
                    executor.submit(self.download_to_file, sub_link, image_path)


class DownloadIMG:
    """Download book's images

    Args:
        - links (list[Link]): The list of links object
        - download_directory (str): Download directory
    """

    def __init__(self, links: list[Link], download_directory: str, timeout: int) -> None:
        self.links: list[Link] = links
        self.download_directory: str = os.sep.join(download_directory.split('/'))
        self.timeout: int = timeout

    def book_handler(self, links: Link) -> None:
        """Download images from the book link

        Args:
            links (Link): Book link
        """
        folder_path: str = os.path.join(self.download_directory, links.name)
        if create_directory(folder_path):
            for link in links.files:
                sub_path: str = os.path.join(folder_path, link.name)
                if create_directory(sub_path):
                    MultiThreadingDownload(link=link, download_path=sub_path, timeout=self.timeout).download()

    def preview_handler(self, link: LinkFile) -> None:
        """Download images from the preview & page link (known num pages)

        Args:
            link (LinkFile): LinkFile of Preview link
        """
        folder_path: str = os.path.join(self.download_directory, link.name)
        if create_directory(folder_path):
            MultiThreadingDownload(link=link, download_path=folder_path, timeout=self.timeout).download()

    def page_handler(self, link: LinkFile) -> None:
        """Dowload All book's images from page link (for unkown num pages)

        Args:
            - link (LinkFile): LinkFile of Page link
        """
        folder_path: str = os.path.join(self.download_directory, link.name)
        if create_directory(folder_path, force=True):
            SingleThreadDownload(link=link, download_path=folder_path, timeout=self.timeout).download()

    def dowload_images(self) -> None:
        """Dowload Images from list of Link"""
        for link in self.links:
            logger.info(msg=f'Downloading: \'{link.original_link}\'')
            match link.original_type:
                case 'book':
                    self.book_handler(link)
                case 'preview':
                    self.preview_handler(link.files[0])
                case 'page':
                    if link.files[0].num_pages > 1:
                        self.preview_handler(link.files[0])
                    else:
                        self.page_handler(link.files[0])
            logger.info(msg=f'Done: \'{link.original_link}\'')
            print()
