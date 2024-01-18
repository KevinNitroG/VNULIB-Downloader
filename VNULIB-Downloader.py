"""VNULIB Downloader"""


from src.utils.utils import pause
from src.utils.printIntro import printIntro
from src.utils.setupVariables import (
    setupVariables, LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL)
from src.utils.setupLogger import setupLogger


def main() -> None:
    """Main function to run VNULIB Downloader

    Params:
        - None

    Returns:
        - None
    """
    printIntro()
    setupVariables()
    setupLogger()

    pause()


if __name__ == '__main__':
    main()
