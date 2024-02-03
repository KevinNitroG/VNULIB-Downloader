"""Setup config file for VNULIB-DOWNLOADER"""


from os import path
from requests import get
from src.modules.logger import logger


class ToolConfig():
    """Setup tool config file

    Params:
        - config_file_name (str): The config file name
        - url (str): The link of the raw config file
    """

    def __init__(self, config_file_name: str, url: str) -> None:
        self.config_file_name: str = config_file_name
        self.url: str = url

    def download_config_file(self) -> None:
        """Download the config file file from repository"""
        logger.info(msg=f'Downloading {
                    self.config_file_name} from repository.'
                    ' Don\'t worry it will downloade once')
        with open(file=self.config_file_name, mode='w', encoding='utf-8') as file:
            try:
                content = get(
                    url=self.url,
                    allow_redirects=True,
                    timeout=10
                ).content.decode(encoding='utf-8')
            except ConnectionError:
                logger.error(
                    msg='Couldn\'t connect to Repository Source to download the config file.'
                        ' Please check the connection or the source of the repo and try again.')
            else:
                file.write(content)
                logger.info(msg='Downloaded config file successfully')

    def check_exist_config_file(self) -> bool:
        """Check if the config file exists or not

        Returns:
            - bool: True if the config file exists, False otherwise
        """
        if path.exists(path=self.config_file_name):
            return True
        logger.warning(msg=f'{self.config_file_name} does not exist')
        return False

    def setup_config_file(self) -> None:
        """Prepare the config file for the project"""
        if not self.check_exist_config_file():
            self.download_config_file()
