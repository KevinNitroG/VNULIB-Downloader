"""Setup logger."""

from __future__ import annotations

from logging import Logger, getLogger
from logging.config import dictConfig
from logging.handlers import QueueHandler
from multiprocessing import Queue
from os import makedirs, path
from yaml import safe_load
from src.constants import LOGGING_CONFIG_FILE_PATH, LOGGING_PATH


class ToolLogger:
    """Setup logger."""

    def __init__(
        self,
        config_path: str = LOGGING_CONFIG_FILE_PATH,
        logging_path: str = LOGGING_PATH,
    ) -> None:
        """Initialise for ToolLogger

        Args:
            - config_path (str): The path of logging config file.
                Default to LOGGING_CONFIG_FILE_PATH.
            - logging_path (str): The logging directory. Default to LOGGING_PATH.
        """
        self.config_path: str = config_path
        self.logging_path = logging_path

    def log_folder(self) -> None:
        """Create the logging folder if not exists."""
        if not path.exists(self.logging_path):
            makedirs(self.logging_path)

    def read_logging_config(self) -> None:
        """Read the logging config file."""
        with open(self.config_path, encoding="utf-8") as config_file:
            dictConfig(safe_load(config_file))  # skipcq: PY-A6006

    def setup(self) -> None:
        """Setup the logger folder and read logging config file."""
        self.log_folder()
        self.read_logging_config()


def logger_listener(logger_name: str, queue: Queue) -> None:
    """Logger listener. Suitable for multiprocessing logger.

    Args:
        logger_name (str): The name of logger to get.
        queue (Queue): The queue to take record to handle.
    """
    logger: Logger = getLogger(logger_name)
    while True:
        record = queue.get()
        if record is None:
            break
        logger.handle(record=record)


def get_queue_logger(queue: Queue) -> Logger:
    """Get the queue logger which is pre-configured in config file.
    Then add the Queue into the Logger in order to send records to the Queue.

    Args:
        queue (Queue): The queue to send records to.

    Returns:
        Logger: The logger.
    """
    logger: Logger = getLogger("vnulib_downloader_sub_process")
    logger.addHandler(QueueHandler(queue))
    return logger
