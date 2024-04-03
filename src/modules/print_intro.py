"""Print out the banner, authors, version."""

from __future__ import annotations

from print_color import print as printColor

from src.constants import AUTHORS, BANNER, VERSION
from src.utils.prints import TERMINAL_SIZE_COLUMNS


class PrintIntro:
    """Print out the intro."""

    def __init__(self) -> None:
        """Initialise for PrintIntro class."""
        self.banner = BANNER.split("\n")
        self.authors = AUTHORS
        self.version = VERSION
        self.print_intro()

    def print_intro(self) -> None:
        """Print the intro including the banner, authors, version."""
        self._print_banner(lines=self.banner)
        self._print_authors(authors=self.authors)
        self._print_version(version=self.version)

    @staticmethod
    def _print_banner(lines: list[str]) -> None:
        """Print out the banner.

        Args:
            lines (list[str]): List of lines of the banner.
        """
        for line in lines:
            printColor(line.center(TERMINAL_SIZE_COLUMNS), color="yan")

    @staticmethod
    def _print_authors(authors: str) -> None:
        """Print out the authors.

        Args:
            authors (str): Authors.
        """
        to_print_authors: str = f"\033[94m\033[43m {authors} \033[0m"
        print(to_print_authors.rjust(TERMINAL_SIZE_COLUMNS))

    @staticmethod
    def _print_version(version: str) -> None:
        """Print out the version.

        Args:
            version (str): Version.
        """
        to_print_version: str = f"\033[45m\033[44m {version} \033[0m"
        print(to_print_version.rjust(TERMINAL_SIZE_COLUMNS))
