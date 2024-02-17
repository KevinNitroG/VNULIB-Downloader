"""Setup the logger
"""


import sys
from os import path, makedirs
from logging import getLogger, Logger
from logging.config import dictConfig
from yaml import safe_load
from src.constants import LOGGING_CONFIG_FILE, LOGGING_DIR


def setup_logger(config_path: str, logging_path: str) -> Logger:
    """Setup the Logger

    Args:
        - config_path (str): The path of logging config file
        - logging_path (str): The logging directory

    Returns:
        - Logger: The Logger
    """
    if not path.exists(logging_path):
        makedirs(logging_path)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        config_path = path.join(sys._MEIPASS, config_path)
    with open(config_path, 'r', encoding='utf-8') as config_file:
        dictConfig(safe_load(config_file))
    return getLogger("vnulib_downloader")


logger: Logger = setup_logger(config_path=LOGGING_CONFIG_FILE,
                              logging_path=LOGGING_DIR)
