"""Delete the images in folder"""

from __future__ import annotations

import os

from .link_parse import Link

from ..utils import logger


class DeleteIMG:
    """Merge the images of books into PDF files

    Args:
        - links (list[Link]): The list of links object
    """

    def __init__(self, links: list[Link], download_directory: str) -> None:
        self.links: list[Link] = links
        self.download_directory: str = download_directory

    @staticmethod
    def process(page_directory: str) -> None:
        """Delete JPG file in directory

        Args:
            directory (str): The directory containing the JPG images.
        """
        jpg_files: list[str] = [
            os.path.join(page_directory, f)
            for f in os.listdir(page_directory)
            if f.endswith(".jpg")
        ]
        for jpg_file in jpg_files:
            os.remove(jpg_file)
        logger.info(msg=f'Deleted images in: "{page_directory}"')

    @staticmethod
    def book_handler(book_directory: str, link: Link) -> None:
        """For each subdirectory in a directory, merge all JPG images into a single PDF.
        The PDF is saved in the same subdirectory with the name of the subdirectory.

        Args:
            directory (str): The directory containing the subdirectories.
            link (Link): The book's link
        """
        for link_page in link.files:
            DeleteIMG.process(os.path.join(book_directory, link_page.name))

    def delete_img(self) -> None:
        """Delete images"""
        for link in self.links:
            match link.original_type:
                case "book":
                    self.book_handler(
                        os.path.join(self.download_directory, link.name), link
                    )
                case "page" | "preview":
                    self.process(
                        os.path.join(self.download_directory, link.files[0].name)
                    )
