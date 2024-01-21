"""VNULIB Downloader"""


from logging import Logger

from src.utils import pause
from src.utils.toolArgparse import argParse
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


if __name__ == '__main__':
    if argParse().update:
        pass  # implement later
    else:
        main()
        pause()
