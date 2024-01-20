"""Contains utility functions for the project"""


from os import makedirs, path
from shutil import rmtree

from src.utils.printColor import printInfo, printSuccess


def pause() -> None:
    """Pause the terminal until user hits Enter

    Params:
        - None

    Returns:
        - None
    """
    _: str = input('Press Enter to continue . . .')


def createDirectory(*directories: str, force: bool = False) -> None:
    """Remove (if force=True) and create a directory

    Params:
        - *directories (str): The directory to create
        - force (bool): Whether to remove the directory if it exists

    Returns:
        - None
    """
    for directory in directories:
        if path.exists(path=directory):
            if force:
                rmtree(path=directory)
                printSuccess(message=f'{directory} was removed recursively!')
            else:
                printInfo(
                    message=f'{directory} was already created. Skip creating it')
                return None
        makedirs(name=directory)
