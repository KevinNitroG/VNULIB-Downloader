"""Merge the images of books into PDF files"""

import os
import img2pdf
from .link_parse import Link, LinkFile


class CreatePDF:
    """Merge the images of books into PDF files

    Args:
        - links (list[Link]): The list of links object
    """

    def __init__(self, links: list[Link]) -> None:
        self.links: list[Link] = links

    @staticmethod
    def merge_jpg_to_pdf_page_link_or_preview_link(page_directory: str, link_page: LinkFile) -> None:
        """Merge all JPG images in a directory into a single PDF.

        Args:
            directory (str): The directory containing the JPG images.
            link (LinkFile): The link of the which use to download JPG use to merge to PDF
        """
        jpg_files: list[str] = [os.path.join(page_directory, f) for f in os.listdir(page_directory) if f.endswith('.jpg')]
        converted_pdf: bytes | None = img2pdf.convert([i for i in jpg_files if i.endswith('.jpg')])
        if converted_pdf is not None:
            with open(f'{link_page.name}.pdf', 'wb') as f:
                f.write(converted_pdf)

    @staticmethod
    def merge_jpg_to_pdf_book_link(book_directory: str, link: Link) -> None:
        """
        For each subdirectory in a directory, merge all JPG images into a single PDF.
        The PDF is saved in the same subdirectory with the name of the subdirectory.

        Args:
            directory (str): The directory containing the subdirectories.

        """
        for link_page in link.files:
            CreatePDF.merge_jpg_to_pdf_page_link_or_preview_link(os.path.join(book_directory, link_page.name), link_page)

    @staticmethod
    def create_pdf(dowload_directory: str, links: list[Link]) -> None:
        """
        For each subdirectory in a directory, if there are JPG images, merge them into a single PDF.
        If there are no JPG images, use the merge_jpg_to_pdf_book_link function.

        Ars:
            directory (str): The directory containing the subdirectories.
        """
        for link in links:
            if link.original_type == 'book':
                CreatePDF.merge_jpg_to_pdf_book_link(os.path.join(dowload_directory, link.name), link)
            else:
                CreatePDF.merge_jpg_to_pdf_page_link_or_preview_link(os.path.join(dowload_directory, link.name), link.files[0])
