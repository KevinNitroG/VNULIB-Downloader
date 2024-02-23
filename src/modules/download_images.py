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
    def download_images_from_page_link_or_preview_link(link: LinkFile, download_directory: str) -> None:
        """Dowload All book's images from page link and previews link

        Args:
            - link (LinkFile): link which that type is page link
        """
        folder_name: str = link.name
        folder_path: str = os.path.join(download_directory, folder_name)
        if create_directory(folder_path):
            number_of_pages: int = link.num_pages
            with alive_bar(number_of_pages) as bar:  # pylint: disable=disallowed-name
                for page_num in range(1, number_of_pages + 1):
                    sub_link: str = create_page_link(link.page_link, page_num)
                    image_bytes: bytes = DownloadImages.download_image_from_page(
                        sub_link)
                    image: ImagePIL = Image.open(BytesIO(image_bytes))
                    image_path: str = os.path.join(
                        download_directory, f'image_{page_num}.jpg')
                    image.save(image_path)
                    bar()  # pylint: disable=not-callable

    @staticmethod
    def download_images_from_book_link(links: Link, download_directory: str) -> None:
        """Download images from the preview link.

        Args:
            links (Link): The preview link.
            download_directory (str): The directory to save the downloaded images.
        """
        folder_book_name: str = links.name
        folder_path: str = os.path.join(download_directory, folder_book_name)
        if create_directory(folder_path):
            for link in links.files:
                DownloadImages.download_images_from_page_link_or_preview_link(
                    link, folder_path)

    @staticmethod
    def dowload_images(links: list[Link], download_directory: str) -> None:
        """Dowload Images from list of Link

            Args:
                -links (list[Link]):List of Link
                -download_directory(str):the directory save dowloads folder
        """
        for link in links:
            if link.original_type == 'page' or link.original_type == 'preview':
                DownloadImages.download_images_from_page_link_or_preview_link(
                    link.files[0], download_directory)
            if link.original_type == 'book':
                DownloadImages.download_images_from_book_link(
                    link, download_directory)
