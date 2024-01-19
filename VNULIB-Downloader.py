"""VNULIB Downloader"""


from src.utils.utils import pause
from src.utils.printIntro import printIntro
from src.utils.printColor import printTitle
from src.utils.setupLogger import setupLogger
from src.utils.setupVariables import setupVariables


def main() -> None:
    """Main function to run VNULIB Downloader

    Params:
        - None

    Returns:
        - None
    """
    printIntro()
    printTitle(message='SETUP VARIABLES')
    LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL = setupVariables()
    setupLogger(LOG=LOG, LOG_LEVEL=LOG_LEVEL)


if __name__ == '__main__':
    main()
    pause()
