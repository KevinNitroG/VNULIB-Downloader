"""Setup the logger"""


import sys
from os import path, makedirs
from logging import getLogger, Logger
from logging.config import dictConfig
from yaml import safe_load
from src.constants import LOGGING_FILE


def setup_logger(config_path: str) -> Logger:
    """Setup the Logger

    Params:
        - config_path (str): The path of logging config file

    Returns:
        - Logger: The Logger
    """
    if not path.exists('VNULIB-Downloader/logs'):
        makedirs('VNULIB-Downloader/logs')
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        config_path = path.join(sys._MEIPASS, config_path)
    with open(config_path, 'r', encoding='utf-8') as config_file:
        dictConfig(safe_load(config_file))
    return getLogger("vnulib_downloader")


logger: Logger = setup_logger(config_path=LOGGING_FILE)
