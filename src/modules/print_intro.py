"""Print out the banner, authors, version"""


from print_color import print as printColor
from src.utils.prints import TERMINAL_SIZE_COLUMNS
from src.constants import BANNER, AUTHORS, VERSION


class PrintIntro:
    """Print out the intro"""

    def __init__(self) -> None:
        self.banner = BANNER.split('\n')
        self.authors = AUTHORS
        self.version = VERSION

    def print_intro(self) -> None:
        """Print the intro

        Params:
            - None

        Retuns:
            - None
        """
        self.print_banner(lines=self.banner)
        self.print_authors(authors=self.authors)
        self.print_version(version=self.version)
        print()

    @staticmethod
    def print_banner(lines: list[str]) -> None:
        """Print out the banner

        Params:
            - lines (list[str]): List of lines of the banner

        Returns:
            - None
        """
        for line in lines:
            printColor(line.center(TERMINAL_SIZE_COLUMNS),
                       color='yan')

    @staticmethod
    def print_authors(authors: str) -> None:
        """Print out the authors

        Params:
            - authors (str): Authors

        Returns:
            - None
        """
        to_print_authors: str = f'\033[94m\033[43m {authors} \033[0m'
        print(to_print_authors.rjust(TERMINAL_SIZE_COLUMNS))

    @staticmethod
    def print_version(version: str) -> None:
        """Print out the version

        Params:
            - version (str): Version

        Returns:
            - None
        """
        to_print_version: str = f'\033[45m\033[44m {version} \033[0m'
        print(to_print_version.rjust(TERMINAL_SIZE_COLUMNS))
