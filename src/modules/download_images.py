"""Download book's images"""
import os
import re
from io import BytesIO
import requests

from PIL import Image

from alive_progress import alive_bar
from requests import Response
from .link_parse import LinkFile, Link
from ..utils.utils import create_directory, create_page_link


class DownloadImages:
    """Download book's images

    Args:
        - links (list[Link]): The list of links object
    """

    def __init__(self, links: list[Link]) -> None:
        self.links: list[Link] = links

    @staticmethod
    def download_image_from_page(link: str) -> bytes:
        """Dowload image from page

        Args:
            - link (str): the page link

        Return:
            - Bytes : The datas of images
        """
        response: Response = requests.get(
            link, stream=True, timeout=10)
        return response.content

    @staticmethod
    def download_images_from_page_link(link: LinkFile, download_directory: str) -> None:
        """Dowload All book's images from page link

        Args:
            - link (str): link which that type is page link

        Return:
            - None
        """
        folder_name: str = link.name
        folder_path: str = os.path.join(download_directory, folder_name)
        create_directory(folder_path)
        number_of_pages: int = link.num_pages
        with alive_bar(number_of_pages) as bar:  # pylint: disable=disallowed-name
            for page_num in range(number_of_pages):
                sub_link = create_page_link(link.page_link)
                sub_link: str = re.sub(
                    r'page=\d+', f'page={page_num}', link.page_link)
                image_bytes: bytes = DownloadImages.download_image_from_page(
                    sub_link)
                image = Image.open(BytesIO(image_bytes))
                image_path: str = os.path.join(
                    download_directory, f"image_{page_num}.jpg")
                image.save(image_path)
                bar()  # pylint: disable=not-callable

    @staticmethod
    def download_images_from_preview_link(links: Link, download_directory: str) -> None:
        """
        Download images from the preview link.

        Args:
            links (Link): The preview link.
            download_directory (str): The directory to save the downloaded images.

        Returns:
            None
        """
        folder_book_name: str = links.name
        folder_path: str = os.path.join(download_directory, folder_book_name)
        create_directory(folder_path)
        for link in links.files:
            DownloadImages.download_images_from_page_link(link, folder_path)
