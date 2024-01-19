"""Setup variables, priority: argparse > config file > user input"""


from re import compile as reCompile, search as reSearch

from yaml import safe_load
from argparse import Namespace

import src.utils.argparse
from .printColor import printError, printInfo
from .setupyYAMLConfig import prepareYAMLConfigFile

from ..CONSTANTS import USER_INPUT_YES


LINKS: list[str] | None = None
OVERWRITE_BOOK: bool | None = None
CREATE_PDF: bool | None = None
KEEP_IMGS: bool | None = None
LOG: bool | None = None
LOG_LEVEL: str | None = None


def strSetByArgparse(var: str) -> str:
    """Return a template string for variables set by argparse

    Params:
        - var (str): Variable name

    Returns:
        - str: Set by argparse message
    """
    return f'{var.ljust(20)} Set by argparse'


def strSetByConfigFile(var: str) -> str:
    """Return a template string for variables set by config file

    Params:
        - var (str): Variable name

    Returns:
        - str: Set by config file message
    """
    return f'{var.ljust(20)} Set by config file (config.yml)'


def strRetreiveFromUserInput(var: str) -> str:
    """Return a template string for variables retrieved from user input

    Params:
        - var (str): Variable name

    Returns:
        - str: Retrieve from user input message
    """
    return f'{var.ljust(20)} Retrieve from user input'


def setupVariablesFromArgsAndConfigFile(args: Namespace, config_file: str = 'config.yml') -> None:
    """Function to be called by setupVariables() to setup variables from argparse and config file

    Params:
        - args (Namespace): The argparse.Namespace object
        - config_file (str): The name of the config file (Default: config.yml)

    Returns:
        - None
    """
    global LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL
    with open(file='config.yml', mode='r', encoding='utf-8') as file:
        config = safe_load(stream=file)
    # Links
    if args.links:
        LINKS = args.links
        printInfo(strSetByArgparse(var='LINKS'))
    elif config['BASIC_CONFIG']['LINKS'] != [] and config['BASIC_CONFIG']['LINKS'] != ['']:
        printInfo(message=strSetByConfigFile(var='LINKS'))
    else:
        LINKS = None
        printInfo(message=strRetreiveFromUserInput(var='LINKS'))
    # Overwrite book
    if args.overwrite_book:
        OVERWRITE_BOOK = args.overwrite_book
        printInfo(message=strSetByArgparse(var='OVERWRITE_BOOK'))
    elif config['BASIC_CONFIG']['OVERWRITE_BOOK']:
        OVERWRITE_BOOK = config['BASIC_CONFIG']['OVERWRITE_BOOK']
        printInfo(message=strSetByConfigFile(var='OVERWRITE_BOOK'))
    else:
        OVERWRITE_BOOK = None
        printInfo(
            message=strRetreiveFromUserInput(var='OVERWRITE_BOOK'))
    # Create PDF
    if args.create_pdf:
        CREATE_PDF = args.create_pdf
        printInfo(message=strSetByArgparse(var='CREATE_PDF'))
    elif config['BASIC_CONFIG']['CREATE_PDF']:
        CREATE_PDF = config['BASIC_CONFIG']['CREATE_PDF']
        printInfo(message=strSetByConfigFile(var='CREATE_PDF'))
    else:
        CREATE_PDF = None
        printInfo(
            message=strRetreiveFromUserInput(var='CREATE_PDF'))
    # Keep images
    if args.keep_imgs:
        KEEP_IMGS = args.keep_imgs
        printInfo(message=strSetByArgparse(var='KEEP_IMGS'))
    elif config['BASIC_CONFIG']['KEEP_IMGS']:
        KEEP_IMGS = config['BASIC_CONFIG']['KEEP_IMGS']
        printInfo(message=strSetByConfigFile(var='KEEP_IMGS'))
    else:
        KEEP_IMGS = None
        printInfo(
            message=strRetreiveFromUserInput(var='KEEP_IMGS'))
    # Log
    if args.log:
        LOG = args.log
        printInfo(message=strSetByArgparse(var='LOG'))
    elif config['ADVANCED_CONFIG']['LOG']:
        LOG = config['ADVANCED_CONFIG']['LOG']
        printInfo(message=strSetByConfigFile(var='LOG'))
    else:
        LOG = False
    # Log level
    if args.log_level:
        LOG_LEVEL = args.log_level
        printInfo(message=f'{'LOG_LEVEL'.ljust(
            20)} Set by argparse to ${LOG_LEVEL}')
    elif config['ADVANCED_CONFIG']['LOG_LEVEL']:
        LOG_LEVEL = config['ADVANCED_CONFIG']['LOG_LEVEL']
        printInfo(message=f'{'LOG_LEVEL'.ljust(
            20)} Set by config file to ${LOG_LEVEL}')
    else:
        LOG_LEVEL = None


def userInputVariables() -> None:
    """Get user input for variables

    Params:
        - None

    Returns:
        - None
    """
    global LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL
    LINKS = LINKS or list(input(
        'Enter the links of the book(s) to be downloaded (separated by space): ').strip().split(sep=' '))
    OVERWRITE_BOOK = OVERWRITE_BOOK or input(
        'Overwrite downloaded books (Y/n): ').upper().strip() in USER_INPUT_YES
    CREATE_PDF = CREATE_PDF or input(
        'Merge images to a PDF (Y/n): ').upper().strip() in USER_INPUT_YES
    KEEP_IMGS = KEEP_IMGS or input(
        'Keep images after merging to PDF (Y/n): ').upper().strip() in USER_INPUT_YES


def checkValidLinks(links: list[str] | None) -> None:
    """Check if the links are valid, otherwise raise ValueError

    Params:
        - links (list[str] | None): The list of links

    Returns:
        - None
    """
    true_pattern = reCompile(
        r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/services/view\.php\?.+page=\d+.+')
    preview_book_pattern = reCompile(
        r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/simple_document\.php\?subfolder=.+&doc=\d+&bitsid=.+')
    book_link_pattern = reCompile(
        r'http[s]?://ir\.vnulib\.edu\.vn/handle/VNUHCM/\d+')
    if links == None or links == [] or links == ['']:
        printError(message='LINKS is None')
        raise ValueError('LINKS is None')
    for link in links:
        if reSearch(pattern=true_pattern, string=link):
            continue
        if reSearch(pattern=preview_book_pattern, string=link):
            printError(
                message=f'Not support preview link of the book: {link}')
            raise ValueError(
                'Not support preview link of the book')
        if reSearch(pattern=book_link_pattern, string=link):
            printError(
                message=f'Not support book link at VNULIB page: {link}')
            raise ValueError('Not support book link at VNULIB page')


def setupVariables():
    """Setup variables, priority: argparse > .env > user input

    Params:
        - None

    Returns:
        - LINKS (list[str] | None): The list of links
        - OVERWRITE_BOOK (bool | None): Overwrite downloaded books
        - CREATE_PDF (bool | None): Merge images to a PDF
        - KEEP_IMGS (bool | None): Keep images after merging to PDF
        - LOG (bool | None): Log
        - LOG_LEVEL (str | None): Log level
    """
    global LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL
    prepareYAMLConfigFile()
    args: Namespace = src.utils.argparse.argParse()
    setupVariablesFromArgsAndConfigFile(args=args, config_file='config.yml')
    print()
    userInputVariables()
    checkValidLinks(links=LINKS)
    return LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL
