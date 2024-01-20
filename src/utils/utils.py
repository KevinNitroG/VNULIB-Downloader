"""Contains utility functions for the project"""


from os import makedirs, path, os
from shutil import rmtree, shutil

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


def deleteAllBooks(path: str) -> None:
    """Delete All The Book's Folders

    Args:
        - path (str): The path include all Book's Folders

    Returns:
        - None
    """
    subdirectories = [os.path.join(path, d) for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]

    for subdirectory in subdirectories:
        shutil.rmtree(subdirectory)


def deleteAllJPGFile(path: str) -> None:
    """Delete All JPG File

        Args:
            -path(str): The path include Images and PDF file

        Returns:
            -None
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg'):
                os.remove(os.path.join(root, file))
