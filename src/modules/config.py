"""Setup pre-config file for VNULIB-Downloader."""

from __future__ import annotations

from os import path
from shutil import copyfile
from logging import getLogger
from ..constants import CONFIG_FILE, CONFIG_SAMPLE_FILE


logger = getLogger(__name__)


class Config:
    """Setup tool pre-config file."""

    def __init__(self, config_file: str = CONFIG_FILE, config_sample_file: str = CONFIG_SAMPLE_FILE) -> None:
        """Initialise for Config.

        Args:
            config_file (str, optional): The config file name. Defaults to CONFIG_FILE.
            url (str, optional): The link of the raw config file. Defaults to CONFIG_SAMPLE_FILE.
        """
        self._config_file: str = config_file
        self._config_sample_file: str = config_sample_file
        self.setup()

    def _prepare_config_file(self) -> None:
        """Copy config sample file to config file."""
        copyfile(self._config_sample_file, self._config_file)
        logger.info('Created tool config: "%s"', self._config_file)

    def _check_exist_config_file(self) -> bool:
        """Check if the config file exists or not.

        Returns:
            bool: True if the config file exists, False otherwise.
        """
        if path.exists(path=self._config_file):
            return True
        logger.info('"%s" does not exist', self._config_file)
        return False

    def setup(self) -> None:
        """Prepare the config file for the project."""
        if not self._check_exist_config_file():
            self._prepare_config_file()
