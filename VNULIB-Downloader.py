"""VNULIB Downloader"""


import os

from logging import Logger

from src.utils.utils import (
    pause, createDirectory, deleteAllBooks, deleteAllJPGFile)
from src.modules.downloadImages import (dowloadAllImagesFromAllLinks)
from src.utils.printIntro import printIntro
from src.utils.printColor import printTitle
from src.utils.setupVariables import setupVariables
from src.utils.setupLogger import setupLogger

from src.CONSTANTS import CONFIG_FILE


def main() -> None:
    """Main function to run VNULIB Downloader

    Params:
        - None

    Returns:
        - None
    """
    printIntro()
    printTitle(message='SETUP VARIABLES')
    LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG = setupVariables(
        config_file=CONFIG_FILE)
    LOGGER: Logger | None = setupLogger(LOG=LOG)
    print(LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOGGER)
    createDirectory('dowloaded_books')
    if OVERWRITE_BOOK:
        deleteAllBooks(os.getcwd())
    dowloadAllImagesFromAllLinks(LINKS)
    if not KEEP_IMGS:
        deleteAllJPGFile(os.getcwd())


if __name__ == '__main__':
    main()
    pause()
