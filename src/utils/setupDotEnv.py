"""Setup .env file for the project."""


from os import path
from requests import get
from printColor import printInfo


def setupConfigEnv(file_name: str = 'config.env') -> None:
    """Setup the config.env file

    Params:
        - file_name (str): The name of the config file (Default: config.env)

    Returns:
        - None
    """
    if not path.exists(path=file_name):
        printInfo(
            message=f'{file_name} does not exist. Fetch the config from repository')
        with open(file=file_name, mode='w', encoding='utf-8') as file:
            content = get(
                url='https://raw.githubusercontent.com/KevinNitroG/VNULIB-Downloader/main/config-sample.env',
                allow_redirects=True
            ).content.decode(encoding='utf-8')
            file.write(content)
