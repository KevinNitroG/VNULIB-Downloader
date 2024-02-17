"""Contains utility functions for the project
"""


from os import makedirs, path
from shutil import rmtree
from datetime import datetime
import unicodedata
import re
from .logger import logger
from ..constants import USER_INPUT_YES


def pause() -> None:
    """Pause the terminal until user hits Enter
    """
    _: str = input('Press Enter to continue . . .')


def create_directory(*directories: str, force: bool | None = None) -> None:
    """Remove (if force=True) and create a directory

    Args:
        - *directories (str): The directory to create
        - force (bool): Whether to remove the directory if it exists
    """
    for directory in directories:
        if path.exists(path=directory):
            if force is False:
                continue
            elif force is True or input(
                    f'{directory} already exists. Force create it [Y/n]: ') in USER_INPUT_YES:
                try:
                    rmtree(path=directory)
                except PermissionError as e:
                    logger.error(
                        msg=f'Error occurred while removing {directory}: {e}')
                    raise e
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

    Args:
        - *directories (str): The directory to remove
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


def datetime_name() -> str:
    """Get the datetime name (%Y-%m-%d %H-%M-%S-%f)

    Returns:
        - str: The datetime name
    """
    return datetime.now().strftime('%Y-%m-%d %H-%M-%S-%f')


def slugify(value, allow_unicode=True):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.

    Taken from https://github.com/django/django/blob/66e47ac69a7e71cf32eee312d05668d8f1ba24bb/django/utils/text.py#L452
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")
