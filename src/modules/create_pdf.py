"""Create PDF for books.
Reference logging for multiprocessing: https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes
"""

from __future__ import annotations

import os
import multiprocessing
from logging.handlers import QueueHandler
import img2pdf
from .link_parse import Link
from ..utils import logger


class CreatePDF:
    """Create PDF for books.

    Args:
        - links (list[Link]): The list of links object.
    """

    def __init__(self, links: list[Link], download_directory: str) -> None:
        self.links: list[Link] = links
        self.download_directory: str = download_directory
        self.all_processes_stop: bool = False
        self.queue = multiprocessing.Queue(maxsize=-1)
        self.logger = logger
        self.logger.addHandler(QueueHandler(queue=self.queue))
        self.workers: list = []

    def logging_process(self) -> None:
        """Take a separate process for logging."""
        while True:
            try:
                record = self.queue.get()
                if record is None:
                    break
                self.logger.handle(record)
            except Exception:
                import sys, traceback

                print("Whoops! Problem:", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)

    def process(self, directory: str, name: str) -> None:
        """Merge all images in a directory into a single PDF.

        Args:
            directory (str): The directory containing the images.
            name (str): Name of pdf file.
        """
        pdf_file_name: str = os.path.join(directory, f"{name}.pdf")
        self.logger.info(msg=f'Creating PDF: "{pdf_file_name}"')
        list_files: list[str] = [os.path.join(directory, item) for item in os.listdir(directory)]
        if any(map(lambda file: file.endswith(".pdf"), list_files)):
            return
        pdf_file: bytes | None = img2pdf.convert(list_files)
        if pdf_file is not None:
            with open(pdf_file_name, "wb") as f:
                f.write(pdf_file)
            self.logger.info(msg=f'Created PDF: "{pdf_file_name}"')

    def book_handler(self, book_directory: str, link: Link) -> None:
        """Book handler, create PDF for Book's files.

        Args:
            directory (str): The directory containing the subdirectories.
            link (Link): The book's Link.
        """
        for file in link.files:
            worker = multiprocessing.Process(
                target=self.process,
                args=(
                    os.path.join(book_directory, file.name),
                    file.name,
                ),
            )
            worker.start()
            self.workers.append(worker)

    def create_pdf(self) -> None:
        """Create PDF."""
        logger_listener = multiprocessing.Process(target=self.logging_process)
        logger_listener.start()
        for link in self.links:
            match link.original_type:
                case "book":
                    self.book_handler(os.path.join(self.download_directory, link.name), link)
                case "preview" | "page":
                    worker = multiprocessing.Process(
                        target=self.process,
                        args=(
                            os.path.join(self.download_directory, link.files[0].name),
                            link.files[0].name,
                        ),
                    )
                    worker.start()
                    self.workers.append(worker)
                case _:
                    pass
        for worker in self.workers:
            worker.join()
        self.queue.put_nowait(None)
        logger_listener.join()
