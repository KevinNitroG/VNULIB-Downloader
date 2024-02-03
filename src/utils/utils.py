"""Contains utility functions for the project"""


from os import makedirs, path
from shutil import rmtree
from src.modules.logger import logger


def pause() -> None:
    """Pause the terminal until user hits Enter

    Params:
        - None

    Returns:
        - None
    """
    _: str = input('Press Enter to continue . . .')


def create_directory(*directories: str, force: bool = False) -> None:
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
                try:
                    rmtree(path=directory)
                except PermissionError as e:
                    logger.error(
                        msg=f'Error occurred while removing {directory}: {e}')
                    raise
                logger.info(msg=f'{directory} was removed recursively!')
            else:
                logger.info(
                    msg=f'{directory} was already created. Skip creating it')
                return
        makedirs(name=directory)
        logger.info(msg=f'{directory} was created!')
    return


def remove_directory(*directories: str) -> None:
    """Remove a directory

    Params:
        - *directories (str): The directory to remove

    Returns:
        - None
    """
    for directory in directories:
        if path.exists(path=directory):
            try:
                rmtree(path=directory)
            except PermissionError as e:
                logger.error(
                    msg=f'Error occurred while removing {directory}: {e}')
                raise
            logger.info(msg=f'{directory} was removed recursively!')
        else:
            logger.info(
                msg=f'{directory} was not found. Skip removing it')
