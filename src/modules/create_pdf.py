"""Create PDF for books.
Reference logging for multiprocessing: https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes
Reference modern logging: https://www.youtube.com/watch?v=9L77QExPmI0
"""

from __future__ import annotations

import os
from multiprocessing import Queue, Process
from logging import Logger
import img2pdf
from .link_parse import Link
from ..utils import get_queue_logger, logger_listener


class CreatePDF:
    """Create PDF for books.

    Args:
        - links (list[Link]): The list of links object.
    """

    def __init__(self, links: list[Link], download_directory: str) -> None:
        self.links: list[Link] = links
        self.download_directory: str = download_directory
        self.queue: Queue = Queue(-1)
        self.workers: list[Process] = []

    @staticmethod
    def check_already_has_pdf(files: list[str]) -> bool:
        """Check if a list of files contains a pdf file.

        This method now also provides a foundation for checking other file types in the future,
        enhancing its utility and adaptability.

        Args:
            files (list[str]): List of files.

        Returns:
            bool: True if a PDF file is found, otherwise False.
        """
        return any(file.endswith(".pdf") for file in files)

    @staticmethod
    def process(directory: str, name: str, queue: Queue) -> None:
        """Merge all images in a directory into a single PDF.

        Args:
            directory (str): The directory containing the images.
            name (str): Name of pdf file.
        """
        logger: Logger = get_queue_logger(queue)
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

    def _create_pdf_worker(self, download_directory: str, name: str) -> None:
        """Creates a worker process to generate a PDF.

        Args:
            download_directory (str): The directory to download the file.
            name (str): The file's name.
        """
        worker = Process(
            target=CreatePDF.process,
            args=(
                download_directory,
                name,
                self.queue,
            ),
        )
        worker.start()
        self.workers.append(worker)

    def book_handler(self, book_directory: str, link: Link) -> None:
        """Book handler, create PDF for Book's files.

        Args:
            directory (str): The directory containing the subdirectories.
            link (Link): The book's Link.
        """
        for file in link.files:
            worker = Process(
                target=CreatePDF.process,
                args=(
                    os.path.join(book_directory, file.name),
                    file.name,
                    self.queue,
                ),
            )
            worker.start()
            self.workers.append(worker)

    def preview_and_page_handler(self, download_directory: str, name: str) -> None:
        """Preview and Page handler, create PDF files.

        Args:
            download_directory (str): The directory to download the file.
            name (str): The file's name.
        """
        self._create_pdf_worker(download_directory, name)

    def create_pdf(self) -> None:
        """Create PDF."""
        listener = Process(target=logger_listener, args=("vnulib_downloader", self.queue))
        listener.start()
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
        for worker in self.workers:
            worker.join()
        self.queue.put_nowait(None)
        listener.join()
