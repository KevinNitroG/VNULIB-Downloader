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
    def merge_jpg_to_pdf(directory, book_name) -> None:
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
            pdf_bytes = img2pdf.convert(jpg_files)
            if pdf_bytes is not None:
                with open(book_name, 'wb') as f:
                    f.write(pdf_bytes)
        else:
            print("No JPG images found in the directory.")
