"""Delete the images in folder."""

from __future__ import annotations

import os
from logging import getLogger
from .link_parse import Link


logger = getLogger(__name__)


class CleanIMG:
    """Clean images. Suitable to use for after creating PDF."""

    def __init__(self, links: list[Link], download_directory: str) -> None:
        """Initialise for CleanIMG class.

        Args:
            - links (list[Link]): The list of links object.
            - download_directory (str): The download directory.
        """
        self._links: list[Link] = links
        self._download_directory: str = download_directory

    @staticmethod
    def _process(page_directory: str) -> None:
        """Delete images file in directory.

        Args:
            directory (str): The directory containing the images.
        """
        logger.info('Deleting images: "%s"', page_directory)
        jpg_files: list[str] = [os.path.join(page_directory, f) for f in os.listdir(page_directory) if f.endswith(".jpg")]
        for jpg_file in jpg_files:
            os.remove(jpg_file)
        logger.info('Deleted images: "%s"', page_directory)

    @staticmethod
    def _book_handler(book_directory: str, link: Link) -> None:
        """Book link hanlder to clean images

        Args:
            directory (str): The directory containing the subdirectories.
            link (Link): The book's link.
        """
        for link_page in link.files:
            CleanIMG._process(os.path.join(book_directory, link_page.name))

    def clean_img(self) -> None:
        """Clean images"""
        for link in self._links:
            match link.original_type:
                case "book":
                    self._book_handler(os.path.join(self._download_directory, link.name), link)
                case "page" | "preview":
                    self._process(os.path.join(self._download_directory, link.files[0].name))
                case _:
                    pass
