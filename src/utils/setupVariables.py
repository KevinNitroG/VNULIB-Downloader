"""Setup variables, priority: argparse > .env > user input"""


from os import getenv
from typing import Any
from dotenv import load_dotenv
from argparse import Namespace
import src.utils.argparse
from printColor import printInfo, printWarning


def setupVariablesFromArgsAndDotenv(args: Namespace) -> None:
    """Function to be called by setupVariables()

    Params:
        - args (Namespace): Arguments parsed by argparse

    Returns:
        - None
    """
    global LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL

    dotenv_links: str | None = getenv(key='LINKS')
    if args.links:
        LINKS: list[Any] | None = args.links
        printInfo(message=f'LINKS is set by argparse')
    elif dotenv_links:
        LINKS: list[Any] | None = dotenv_links.split(sep=',')
        printInfo(message=f'LINKS is set by config.env')
    else:
        LINKS: list[Any] | None = None
        printWarning(message='LINKS is not set. Will retrieve from user input')

    if args.overwrite_book:
        OVERWRITE_BOOK: bool | None = args.overwrite_book
        printInfo(message=f'OVERWRITE_BOOK is set by argparse')
    elif getenv(key='OVERWRITE_BOOK'):
        OVERWRITE_BOOK: bool | None = (getenv(key='OVERWRITE_BOOK') == 'True')
        printInfo(message=f'OVERWRITE_BOOK is set by config.env')
    else:
        OVERWRITE_BOOK: bool | None = None
        printWarning(
            message='OVERWRITE_BOOK is not set. Will retrieve from user input')

    if args.create_pdf:
        CREATE_PDF: bool | None = args.create_pdf
        printInfo(message=f'CREATE_PDF is set by argparse')
    elif getenv(key='CREATE_PDF'):
        CREATE_PDF: bool | None = (getenv(key='CREATE_PDF') == 'True')
        printInfo(message=f'CREATE_PDF is set by config.env')
    else:
        CREATE_PDF: bool | None = None
        printWarning(
            message='CREATE_PDF is not set. Will retrieve from user input')

    if args.keep_imgs:
        KEEP_IMGS: bool | None = args.keep_imgs
        printInfo(message=f'KEEP_IMGS is set by argparse')
    elif getenv(key='KEEP_IMGS'):
        KEEP_IMGS: bool | None = (getenv(key='KEEP_IMGS') == 'True')
        printInfo(message=f'KEEP_IMGS is set by config.env')
    else:
        KEEP_IMGS: bool | None = None
        printWarning(
            message='KEEP_IMGS is not set. Will retrieve from user input')

    if args.log:
        LOG: bool | None = args.log
        printInfo(message=f'LOG is set by argparse')
    elif getenv(key='LOG'):
        LOG: bool | None = (getenv(key='LOG') == 'True')
        printInfo(message=f'LOG is set by config.env')
    else:
        LOG: bool | None = False

    if args.log_level:
        LOG_LEVEL: str | None = args.log_level
        printInfo(message=f'LOG_LEVEL is set by argparse to ${LOG_LEVEL}')
    elif getenv(key='LOG_LEVEL'):
        LOG_LEVEL: str | None = getenv(key='LOG_LEVEL')
        printInfo(message=f'LOG_LEVEL is set by config.env to ${LOG_LEVEL}')
    else:
        LOG_LEVEL: str | None = None


def userInputVariables() -> None:
    """Get user input for variables

    Params:
        - None

    Returns:
        - None
    """
    global LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL

    LINKS: list[Any] | None = LINKS or input(
        'Enter the links of the book(s) to be downloaded (separated by space): ').split(sep=' ')
    OVERWRITE_BOOK: bool | None = OVERWRITE_BOOK or input(
        'If the folder of images / PDF file of the book is already exist, then overwrite it (Y/n): ').upper() == 'Y'
    CREATE_PDF: bool | None = CREATE_PDF or input(
        'Merge images to a PDF (Y/n): ').upper == 'Y'
    KEEP_IMGS: bool | None = KEEP_IMGS or input(
        'Keep images after merging to PDF (Y/n): ').upper() == 'Y'
    # LOG: bool | None = LOG or input('Log the process (y/N): ').upper() == 'N'
    # LOG_LEVEL: str | None = LOG_LEVEL or input(
    #     'Log level:\n\tOptions: DEBUG, INFO, WARNING, ERROR, CRITICAL\n\tDefault: INFO\nLog level: ').upper()


def setupVariables() -> None:
    """Setup variables, priority: argparse > .env > user input

    Params:
        - None

    Returns:
        - None
    """
    load_dotenv(dotenv_path='config.env')
    args: Namespace = src.utils.argparse.argParse()
    setupVariablesFromArgsAndDotenv(args=args)
    userInputVariables()
