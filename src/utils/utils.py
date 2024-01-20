"""Contains utility functions for the project"""


import os
import shutil


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
