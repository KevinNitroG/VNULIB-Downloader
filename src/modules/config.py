"""Setup pre config file for VNULIB-Downloader"""

from os import path

from requests import get

from ..constants import CONFIG_FILE, CONFIG_FILE_URL
from ..utils import logger


class Config():
    """Setup tool config file

    Args:
        - config_file (str): The config file name
        - url (str): The link of the raw config file
    """

    def __init__(self, config_file: str = CONFIG_FILE, url: str = CONFIG_FILE_URL) -> None:
        self.config_file: str = config_file
        self.url: str = url
        self.setup()

    def download_config_file(self) -> None:
        """Download the config file from repository"""
        logger.info(msg=f'Downloading "{self.config_file}" from repository.'
                    ' It will download once')
        with open(file=self.config_file, mode='w', encoding='utf-8') as file:
            try:
                content = get(
                    url=self.url,
                    allow_redirects=True,
                    timeout=10
                ).content.decode(encoding='utf-8')
            except ConnectionError:
                logger.error(
                    msg='Couldn\'t connect to Repository Source to download the config file.'
                    'Please check the connection or the source of the repo and try again.')
            else:
                file.write(content)
                logger.info(msg='Downloaded config file successfully at '
                                f'"{self.config_file}"')

    def check_exist_config_file(self) -> bool:
        """Check if the config file exists or not

        Returns:
            - bool: True if the config file exists, False otherwise
        """
        if path.exists(path=self.config_file):
            return True
        logger.info(msg=f'{self.config_file} does not exist')
        return False

    def setup(self) -> None:
        """Prepare the config file for the project"""
        if not self.check_exist_config_file():
            self.download_config_file()
