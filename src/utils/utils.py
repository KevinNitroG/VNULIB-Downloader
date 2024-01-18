"""Contains utility functions for the project"""


from os import makedirs, path, removedirs


def pause() -> None:
    """Pause the terminal until user hits Enter

    Params:
        - None

    Returns:
        - None
    """
    _: str = input('Press Enter to continue . . .')


def createDirectory(*directories: str) -> None:
    """Create directories if they do not exist

    Params:
        - *directories (str): The directories to create

    Returns:
        - None
    """
    for directory in directories:
        if not path.exists(path=directory):
            makedirs(name=directory)


def reCreateDirectory(*directories: str) -> None:
    """Delete directories and recreate them

    Params:
        - *directories (str): The directories to recreate

    Returns:
        - None
    """
    for directory in directories:
        if path.exists(path=directory):
            removedirs(name=directory)
        makedirs(name=directory)
