"""Download book's images"""


import os
import sys
from itertools import count
import threading
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


class DownloadIMG:
    """Download book's images

    Args:
        - links (list[Link]): The list of links object
        - download_directory (str): Download directory
    """

    def __init__(self, links: list[Link], download_directory: str) -> None:
        self.links: list[Link] = links
        self.download_directory: str = os.sep.join(download_directory.split('/'))

    @staticmethod
    def get_images_bytes(link: str) -> bytes:
        """Get images bytes

        Args:
            - link (str): the page link

        Return:
            - Bytes: The datas of images
        """
        try:
            return requests.get(link, stream=True, timeout=20, verify=False).content
        except requests.exceptions.ReadTimeout:
            logger.error(msg=f'Error page for {link}')
            return ERROR_PAGE_IMAGE

    @staticmethod
    def get_content_pages(link: str) -> str:
        """Get text from page

        Args:
            - link (str): Link

        Returns:
            - str: Text content of link
        """
        return requests.get(link, stream=True, timeout=20, verify=False).text

    @staticmethod
    def multithreading_for_known_page(image_link: str, image_path: str, bar) -> None:  # pylint: disable=disallowed-name
        """Multithreading download function for known page link (book | preview)

        Args:
            image_link (str): Image link
            image_path (str): Image path
            bar: The alivebar
        """
        with open(image_path, 'wb') as file:
            file.write(DownloadIMG.get_images_bytes(image_link))
        bar()

    @staticmethod
    def multithreading_for_unknown_page(image_link: str, image_path: str, bar) -> None:   # pylint: disable=disallowed-name
        """Multithreading download function for unkown page link (page)

        Args:
            image_link (str): Image link
            image_path (str): Image path
            bar: The alivebar
        """
        if OUT_PAGE_ERROR_TEXT in DownloadIMG.get_content_pages(image_link):
            raise IndexError
        with open(image_path, 'wb') as file:
            file.write(DownloadIMG.get_images_bytes(image_link))
        bar()

    def download_with_known_page(self, link: LinkFile, download_path: str) -> None:
        """Download images for link with known page nums (each link of book | preview)

        Args:
            link (LinkFile): Link object
            download_path (str): Path for images to be downloaded
        """
        number_of_pages: int = link.num_pages
        with alive_bar(number_of_pages) as bar:  # pylint: disable=disallowed-name
            for page_num in range(1, number_of_pages + 1):
                sub_link: str = f'{link.page_link}&page={page_num}'
                image_path = os.path.join(download_path, f'image_{page_num}.jpg')
                thread = threading.Thread(target=self.multithreading_for_known_page, args=(sub_link, image_path, bar))
                thread.start()
                thread.join()

    def download_with_unknown_page(self, link: LinkFile, download_path: str) -> None:
        """Download images from the preview and page link.

        Args:
            links (LinkFile): The preview and page link
        """
        page_num = count(start=1)
        with alive_bar() as bar:  # pylint: disable=disallowed-name
            try:
                while True:
                    current_page: str = str(next(page_num))
                    image_link: str = f'{link.page_link}&page={current_page}'
                    image_path: str = os.path.join(download_path, f'image_{current_page}.jpg')
                    thread = threading.Thread(target=self.multithreading_for_unknown_page, args=(image_link, image_path, bar))
                    thread.start()
                    thread.join()
            except IndexError:
                pass

    def book_handler(self, links: Link) -> None:
        """Download images from the book link

        Args:
            links (Link): Book link
        """
        folder_path: str = os.path.join(self.download_directory, links.name)
        if create_directory(folder_path, force=True):
            for link in links.files:
                sub_path: str = os.path.join(folder_path, link.name)
                create_directory(sub_path, force=True)
                self.download_with_known_page(link=link, download_path=sub_path)

    def preview_handler(self, link: LinkFile) -> None:
        """Download images from the preview link

        Args:
            link (LinkFile): LinkFile of Preview link
        """
        folder_path: str = os.path.join(self.download_directory, link.name)
        create_directory(folder_path, force=True)
        self.download_with_known_page(link=link, download_path=folder_path)

    def page_handler(self, link: LinkFile) -> None:
        """Dowload All book's images from page link and previews link

        Args:
            - link (LinkFile): LinkFile of Page link
        """
        folder_name: str = link.name
        folder_path: str = os.path.join(self.download_directory, folder_name)
        if create_directory(folder_path, force=True):
            self.download_with_unknown_page(link=link, download_path=folder_path)

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
                    self.page_handler(link.files[0])
            logger.info(msg=f'Done: \'{link.original_link}\'')
            print()
