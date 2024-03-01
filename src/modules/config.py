"""Setup pre config file for VNULIB-Downloader"""

from __future__ import annotations

from os import path
from shutil import copyfile
from ..constants import CONFIG_FILE, CONFIG_SAMPLE_FILE
from ..utils import logger


class Config:
    """Setup tool config file

    Args:
        - config_file (str): The config file name
        - url (str): The link of the raw config file
    """

    def __init__(
        self,
        config_file: str = CONFIG_FILE,
        config_sample_file: str = CONFIG_SAMPLE_FILE,
    ) -> None:
        self.config_file: str = config_file
        self.config_sample_file: str = config_sample_file
        self.setup()

    def prepare_config_file(self) -> None:
        """Copy config sample file to config file"""
        copyfile(self.config_sample_file, self.config_file)
        logger.info(msg=f'Created tool config: "{self.config_file}"')

    def check_exist_config_file(self) -> bool:
        """Check if the config file exists or not

        Returns:
            - bool: True if the config file exists, False otherwise
        """
        if path.exists(path=self.config_file):
            return True
        logger.info(msg=f"{self.config_file} does not exist")
        return False

    def setup(self) -> None:
        """Prepare the config file for the project"""
        if not self.check_exist_config_file():
            self.prepare_config_file()
