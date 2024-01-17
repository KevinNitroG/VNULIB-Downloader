"""Print out the banner, authors, version"""


from print_color.print_color import print as printColor
from ..utils import TERMINAL_SIZE_COLUMNS
from ..CONSTANTS import BANNER, AUTHORS, VERSION


def printBanner(lines: list[str]) -> None:
    """Print out the banner

    Params:
        - lines (list[str]): List of lines of the banner

    Returns:
        - None
    """
    for line in lines:
        printColor(line.center(TERMINAL_SIZE_COLUMNS),
                   color='purple')


def printAuthors(authors: str) -> None:
    """Print out the authors

    Params:
        - authors (str): Authors

    Returns:
        - None
    """
    to_print_authors: str = f'\033[94m\033[43m {authors} \033[0m'
    print(to_print_authors.rjust(TERMINAL_SIZE_COLUMNS))


def printVersion(version: str) -> None:
    """Print out the version

    Params:
        - version (str): Version

    Returns:
        - None
    """
    to_print_version: str = f'\033[45m\033[44m {version} \033[0m'
    print(to_print_version.rjust(TERMINAL_SIZE_COLUMNS))


def printIntro() -> None:
    """Print out the banner, authors, version

    Params:
        - None

    Returns:
        - None
    """
    printBanner(lines=BANNER.split('\n'))
    printAuthors(authors=AUTHORS)
    printVersion(version=VERSION)
    print()
