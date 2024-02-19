"""Setup the logger"""


import sys
from os import path, makedirs
from logging.config import dictConfig
from logging import getLogger, Logger
from yaml import safe_load
from src.constants import LOGGING_CONFIG_FILE_PATH, LOGGING_PATH


class ToolLogger:
    """Setup logger

    Args:
        - config_path (str): The path of logging config file. Default to LOGGING_CONFIG_FILE_PATH
        - logging_path (str): The logging directory. Default to LOGGING_PATH
    """

    def __init__(self, config_path: str = LOGGING_CONFIG_FILE_PATH, logging_path: str = LOGGING_PATH) -> None:
        self.config_path: str = config_path
        self.logging_path = logging_path

    def log_folder(self) -> None:
        """Create the logging folder if not exists"""
        if not path.exists(self.logging_path):
            makedirs(self.logging_path)

    def reset_config_path(self) -> None:
        """Reset the config path depends on pyinstaller environment or not"""
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            self.config_path = path.join(
                sys._MEIPASS, self.config_path)  # type: ignore # skipcq: PYL-W0212 # pylint: disable=protected-access # nopep8

    def read_logging_config(self) -> None:
        """Read the logging config file"""
        self.reset_config_path()
        with open(self.config_path, 'r', encoding='utf-8') as config_file:
            dictConfig(safe_load(config_file))  # skipcq: PY-A6006


tool_logger = ToolLogger()
tool_logger.log_folder()
tool_logger.read_logging_config()
logger: Logger = getLogger()
