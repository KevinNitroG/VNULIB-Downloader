"""Print functions with tag, color, format, background."""

from __future__ import annotations

from os import get_terminal_size
from print_color.print_color import print as print_color


def print_title(message: str) -> None:
    """Print out title with center align.

    Args:
        - Message (str): Message of Title.
    """
    print()
    print_color(
        message.center(int(TERMINAL_SIZE_COLUMNS)),
        color="magenta",
        format="bold",
        background="blue",
        end="\n\n",
    )


def print_success(message: str) -> None:
    """Print out success message with green color.

    Args:
        - Message (str): Message of Success.
    """
    print_color(message, tag="Success", color="green")


def print_error(message: str) -> None:
    """Print out error message with red color.

    Args:
        - Message (str): Message of Error
    """
    print_color(message, tag="Error", color="red")


def print_warning(message: str) -> None:
    """Print out warning message with yellow color.

    Args:
        - Message (str): Message of Warning
    """
    print_color(message, tag="Warning", color="yellow")


def print_retry(message: str) -> None:
    """Print out retry message with blue color.

    Args:
        - Message (str): Message of Retry
    """
    print_color(message, tag="Retry", color="blue")


def print_info(message: str) -> None:
    """Print out info message with yan color.

    Args:
        - Message (str): Message of Info
    """
    print_color(message, tag="Info", color="yan")


def terminal_size() -> int:
    """Get current terminal's size in columns.

    Returns:
        - int: Terminal's size in columns.
    """
    try:
        size: int = get_terminal_size().columns
    except OSError:
        size = 100
    return size


TERMINAL_SIZE_COLUMNS = terminal_size()
