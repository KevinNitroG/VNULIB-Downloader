"""Delete the images in folder"""

from __future__ import annotations

import os

from .link_parse import Link


class DeleteIMG:
    """Merge the images of books into PDF files

    Args:
        - links (list[Link]): The list of links object
    """

    def __init__(self, links: list[Link]) -> None:
        self.links: list[Link] = links

    @staticmethod
    def delete_jpg_page_link_or_preview_link(page_directory: str) -> None:
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

    @staticmethod
    def delete_jpg_book_link(book_directory: str, link: Link) -> None:
        """
        For each subdirectory in a directory, merge all JPG images into a single PDF.
        The PDF is saved in the same subdirectory with the name of the subdirectory.

        Args:
            directory (str): The directory containing the subdirectories.
            link (Link): The book's link
        """
        for link_page in link.files:
            DeleteIMG.delete_jpg_page_link_or_preview_link(
                os.path.join(book_directory, link_page.name)
            )

    @staticmethod
    def delete_jpg(dowload_directory: str, links: list[Link]) -> None:
        """
        For each subdirectory in a directory, if there are JPG images, delete it

        Ars:
            directory (str): The directory containing the subdirectories.
            links(list[Link]): The list of Link
        """
        for link in links:
            if link.original_type == "book":
                DeleteIMG.delete_jpg_book_link(
                    os.path.join(dowload_directory, link.name), link
                )
            else:
                DeleteIMG.delete_jpg_page_link_or_preview_link(
                    os.path.join(dowload_directory, link.name)
                )
