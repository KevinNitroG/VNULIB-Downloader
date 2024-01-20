# Delete All Images if KEEPIMG is false
import os


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
