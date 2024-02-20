"""Merge the images of books into PDF files"""

import os
import img2pdf
from .link_parse import LinkFile, Link


class CreatePDF:
    """Merge the images of books into PDF files

    Args:
        - links (list[Link]): The list of links object
    """

    def __init__(self, links: list[Link]) -> None:
        self.links = links

    @staticmethod
    def merge_jpg_to_pdf(directory: str, book_name: str) -> None:
        """Merge all JPG images in a directory into a single PDF.

        Args:
            directory (str): The directory containing the JPG images.
            output_filename (str): The filename of the output PDF.

        Returns:
            None
        """
        jpg_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
        jpg_files.sort()
        jpg_files = [os.path.join(directory, f) for f in jpg_files]
        if jpg_files:
            pdf_bytes: bytes | None = img2pdf.convert(jpg_files)
            if pdf_bytes is not None:
                with open(book_name, 'wb') as f:
                    f.write(pdf_bytes)
        else:
            print("No JPG images found in the directory.")

    @staticmethod
    def merge_jpg_to_pdf_previewlink(directory: str) -> None:
        """
        For each subdirectory in a directory, merge all JPG images into a single PDF.
        The PDF is saved in the same subdirectory with the name of the subdirectory.

        Args:
            directory (str): The directory containing the subdirectories.

        """
        for subdir in os.scandir(directory):
            if subdir.is_dir():
                CreatePDF.merge_jpg_to_pdf(os.path.join(
                    directory, subdir.path), os.path.basename(subdir.path))
