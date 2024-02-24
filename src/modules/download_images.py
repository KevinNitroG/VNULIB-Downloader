"""Download book's images"""
import os
from io import BytesIO
import requests
from PIL import Image
from PIL.Image import Image as ImagePIL
from alive_progress import alive_bar
from requests import Response
from .link_parse import LinkFile, Link
from ..utils.utils import create_directory, create_page_link


class DownloadImages:
    """Download book's images

    Args:
        - links (list[Link]): The list of links object
        - download_directory (str): Download directory
    """

    def __init__(self, links: list[Link], download_directory: str) -> None:
        self.links: list[Link] = links
        self.download_directory: str = os.pathsep.join(download_directory.split('/'))

    @staticmethod
    def download_image_from_page(link: str) -> bytes:
        """Dowload image from page

        Args:
            - link (str): the page link

        Return:
            - Bytes : The datas of images
        """
        return requests.get(link, stream=True, timeout=10).content

    def book_download(self, link: LinkFile, folder_path: str) -> None:
        """Download images for book

        Args:
            link (LinkFile): Link object
            folder_path (str): Destination for images to be downloaded
        """
        if create_directory(folder_path, force=True):
            number_of_pages: int = link.num_pages
            with alive_bar(number_of_pages) as bar:  # pylint: disable=disallowed-name
                for page_num in range(1, number_of_pages + 1):
                    sub_link: str = create_page_link(link.page_link, page_num)
                    image_bytes: bytes = self.download_image_from_page(
                        sub_link)
                    image: ImagePIL = Image.open(BytesIO(image_bytes))
                    image_path: str = os.path.join(
                        self.download_directory, f'image_{page_num}.jpg')
                    image.save(image_path)
                    bar()  # pylint: disable=not-callable

    def book_handler(self, links: Link) -> None:
        """Download images from the preview link.

        Args:
            links (Link): The preview link.
        """
        folder_path: str = os.path.join(self.download_directory, links.name)
        if create_directory(folder_path, force=True):
            for link in links.files:
                self.book_download(link=link, folder_path=folder_path)

    # Nguyen Xu lys di nha:))
    def preview_and_page_download(self, link: LinkFile, folder_path: str) -> None:
        if create_directory(folder_path, force=True):
        number_of_pages: int = link.num_pages
        with alive_bar(number_of_pages) as bar:  # pylint: disable=disallowed-name
            for page_num in range(1, number_of_pages + 1):
                sub_link: str = create_page_link(link.page_link, page_num)
                image_bytes: bytes = self.download_image_from_page(
                    sub_link)
                image: ImagePIL = Image.open(BytesIO(image_bytes))
                image_path: str = os.path.join(
                    self.download_directory, f'image_{page_num}.jpg')
                image.save(image_path)
                bar()  # pylint: disable=not-callable

    def preview_and_page_handler(self, link: LinkFile) -> None:
        """Dowload All book's images from page link and previews link

        Args:
            - link (LinkFile): link which that type is page link
        """
        folder_name: str = link.name
        folder_path: str = os.path.join(self.download_directory, folder_name)
        if create_directory(folder_path, force=True):
            self.download_image_from_page(link=link, folder_path=folder_path)

    def dowload_images(self) -> None:
        """Dowload Images from list of Link"""
        for link in self.links:
            match link.original_type:
                case 'book':
                    self.book_handler(link)
                case 'page' | 'preview':
                    self.preview_and_page_handler(link.files[0])
