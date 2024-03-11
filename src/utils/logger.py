"""Setup logger."""

from __future__ import annotations

from logging import Logger, Handler, getLogger, getHandlerByName
from logging.config import dictConfig
from os import makedirs, path
from typing import Any
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

    def get_logger(self, logger_name: str, *args: Any, **kwds: Any) -> Logger:
        self.log_folder()
        self.read_logging_config()
        return getLogger(logger_name)


class QueueHandlerLogger:
    """Start the Queue Handler thread.
    Use it by context manager.
    """

    def __init__(self, logger_name: str) -> None:
        """Initialise.

        Args:
            logger_name (str): Name of the logger to get.
        """
        self.logger_name = logger_name
        self.queue_handler: Handler | None

    def get_logger(self) -> Logger:
        """Return the got logger.

        Returns:
            Logger: The logger.
        """
        return ToolLogger().get_logger(self.logger_name)

    def start(self) -> None:
        """Start Queue Handler thread."""
        self.queue_handler = getHandlerByName(self.logger_name)
        if self.queue_handler:
            self.queue_handler.listener.start()  # type: ignore

    def stop(self) -> None:
        """Stop the Queue Handler thread."""
        if self.queue_handler:
            self.queue_handler.listener.stop()  # type: ignore
