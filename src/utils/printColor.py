"""Print out with tag, color, format, background"""

from os import get_terminal_size

from print_color.print_color import print as printColor


TERMINAL_SIZE_COLUMNS: int = get_terminal_size().columns


def printTitle(message: str) -> None:
    """Print out title with center align

    Args:
        - Message (str): Message of Title

    Returns:
        - None
    """
    printColor(message.center(int(TERMINAL_SIZE_COLUMNS)),
               color='magenta', format='bold', background='blue', end='\n\n')


def printSuccess(message: str) -> None:
    """Print out success message with green color

    Args:
        - Message (str): Message of Success

    Returns:
        - None
    """
    printColor(message, tag='Success', color='green')


def printError(message: str) -> None:
    """Print out error message with red color

    Args:
        - Message (str): Message of Error

    Returns:
        - None
    """
    printColor(message, tag='Error', color='red')


def printWarning(message: str) -> None:
    """Print out warning message with yellow color

    Args:
        - Message (str): Message of Warning

    Returns:
        - None
    """
    printColor(message, tag='Warning', color='yellow')


def printRetry(message: str) -> None:
    """Print out retry message with blue color

    Args:
        - Message (str): Message of Retry

    Returns:
        - None
    """
    printColor(message, tag='Retry', color='blue')


def printInfo(message: str) -> None:
    """Print out info message with yan color

    Args:
        - Message (str): Message of Info

    Returns:
        - None
    """
    printColor(message, tag='Info', color='yan')
