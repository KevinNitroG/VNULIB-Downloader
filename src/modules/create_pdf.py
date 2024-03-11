"""Create PDF for books.
Reference logging for multiprocessing: https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes
Reference modern logging: https://www.youtube.com/watch?v=9L77QExPmI0
"""

from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor
from logging import Logger
import img2pdf
from .link_parse import Link
from ..utils import ToolLogger, QueueHandlerRun


logger: Logger = ToolLogger().get_logger("vnulib_downloader_queue")


class CreatePDF:
    """Create PDF for books.

    Args:
        - links (list[Link]): The list of links object.
    """

    def __init__(self, links: list[Link], download_directory: str) -> None:
        self.links: list[Link] = links
        self.download_directory: str = download_directory
        self.executor = ProcessPoolExecutor()
        self.queue_handler: QueueHandlerRun = QueueHandlerRun("queue")
        self.queue_handler.start()

    @staticmethod
    def check_already_has_pdf(files: list[str]) -> bool:
        """Check if a list of files contains a pdf file.

        Args:
            files (list[str]): List of files.

        Returns:
            bool: True if yes, otherwise False.
        """
        for file in files:
            if file.endswith(".pdf"):
                return True
        return False

    @staticmethod
    def process(directory: str, name: str) -> None:
        """Merge all images in a directory into a single PDF.

        Args:
            directory (str): The directory containing the images.
            name (str): Name of pdf file.
        """
        print("Da vao")
        logger: Logger = ToolLogger().get_logger("vnulib_downloader_queue")
        logger.warning("Heyyy")
        pdf_file_name: str = os.path.join(directory, f"{name}.pdf")
        logger.info('Creating PDF: "%s"', pdf_file_name)
        files: list[str] = [os.path.join(directory, item) for item in os.listdir(directory)]
        if CreatePDF.check_already_has_pdf(files):
            return
        pdf_file: bytes | None = img2pdf.convert(files)
        if pdf_file is not None:
            with open(pdf_file_name, "wb") as f:
                f.write(pdf_file)
            logger.info('Created PDF: "%s"', pdf_file_name)

    def book_handler(self, book_directory: str, link: Link) -> None:
        """Book handler, create PDF for Book's files.

        Args:
            directory (str): The directory containing the subdirectories.
            link (Link): The book's Link.
        """
        for file in link.files:
            self.executor.submit(
                CreatePDF.process,
                os.path.join(book_directory, file.name),
                file.name,
            )

    def preview_and_page_handler(self, download_directory: str, name: str) -> None:
        """Preview and page handler, create PDF for only one file.

        Args:
            download_directory (str): The directory to download the file.
            name (str): The file's name.
        """
        self.executor.submit(
            CreatePDF.process,
            download_directory,
            name,
        )

    def create_pdf(self) -> None:
        """Create PDF."""
        for link in self.links:
            match link.original_type:
                case "book":
                    self.book_handler(
                        book_directory=os.path.join(self.download_directory, link.name),
                        link=link,
                    )
                case "preview" | "page":
                    self.preview_and_page_handler(
                        download_directory=os.path.join(self.download_directory, link.files[0].name),
                        name=link.files[0].name,
                    )
                case _:
                    pass
        self.executor.shutdown()
        self.queue_handler.stop()
