"""Contains utility functions for the project"""

from __future__ import annotations

import re
import sys
import unicodedata
from glob import glob
from datetime import datetime
from time import time
from os import makedirs, path
from shutil import rmtree
from logging import getLogger
from ..constants import USER_INPUT_YES


logger = getLogger(__name__)


def delete_old_meipass(time_threshold=3600) -> None:  # Default setting: Remove after 1 hour, time_threshold in seconds
    """Clean old _MEIPASS folder (Windows only I think).
    This code is from: https://stackoverflow.com/a/61909248/23173098

    Args:
        time_threshold (int, optional): Delete old _MEIPASS older than time_threshold (s). Defaults to 3600.
    """
    try:
        base_path = sys._MEIPASS  # type: ignore # skipcq: PYL-W0212 # pylint: disable=protected-access # nopep8
    except Exception:
        logger.debug("No MEIPASS found")
        return  # Not being ran as OneFile Folder -> Return
    temp_path = path.abspath(path.join(base_path, ".."))  # Go to parent folder of MEIPASS
    # Search all MEIPASS folders...
    mei_folders = glob(path.join(temp_path, "_MEI*"))
    for item in mei_folders:
        if (time() - path.getctime(item)) > time_threshold:
            rmtree(item)
            logger.debug("Deleted: %s", item)


def pause() -> None:
    """Pause the terminal until user hits Enter"""
    _: str = input("Press Enter to continue . . .")


def create_directory(directory: str, force: bool | None = None) -> bool:
    """Remove (if force=True) and create a directory

    Args:
        directory (str): A directory to create
        force (bool | None): Whether to remove the directory if it exists. Default to None to ask for user input [Y/n]

    Raise:
        PermissionError: If the directory cannot be removed due to permission error

    Returns:
        bool: True if the directory was created, False if it was already created
    """
    if path.exists(path=directory):
        if force is False:
            return True
        if force is True or input(f'"{directory}" already exists. Force create it [Y/n]: ').upper() in USER_INPUT_YES:
            try:
                rmtree(path=directory)
            except Exception as e:
                logger.error(e)
                raise e
            logger.info('Deleted: "%s"', directory)
        else:
            logger.info('Skip creating: "%s"', directory)
            return False
    makedirs(name=directory)
    logger.info('Created: "%s"', directory)
    return True


def remove_directory(directory: str) -> bool:
    """Remove a directory

    Args:
        directory (str): A directory to remove

    Raise:
        PermissionError: If the directory cannot be removed due to permission error

    Returns:
        bool: True if the directory was removed, False if it was not found
    """
    if path.exists(path=directory):
        try:
            rmtree(path=directory)
        except Exception as e:
            logger.error(e)
            raise e
        logger.info('Deleted: "%s"', directory)
        return True
    logger.info('Not found: "%s"', directory)
    return False


def datetime_name() -> str:
    """Get the datetime name (%Y-%m-%d %H-%M-%S-%f)

    Returns:
        str: The datetime name
    """
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S-%f")


def slugify(value, allow_unicode=False):
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
        value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")
