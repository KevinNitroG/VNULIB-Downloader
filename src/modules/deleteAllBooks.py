# Delete All Books When Overwrite is True
import os


def deleteAllBooks(path: str) -> None:
    """Delete All The Book's Folders

        Args:
            - path (str):The path include all Book's Folders

        Returns:
            - None
    """
    subdirectories = [os.path.join(path, d) for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]

    for subdirectory in subdirectories:
        for root, dirs, files in os.walk(subdirectory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(subdirectory)
