"""Setup .env file for the project."""


from os import path
from requests import get
from .printColor import printError, printInfo


def downloadYAMLConfigFile(file_name: str = 'config.yml') -> None:
    """Download the config.env file from repository

    Params:
        - file_name (str): The name of the config file (Default: config.yml)

    Returns:
        - None
    """
    printInfo(message=f'Downloading {file_name} from repository')
    with open(file=file_name, mode='w', encoding='utf-8') as file:
        try:
            content = get(
                url='https://raw.githubusercontent.com/KevinNitroG/VNULIB-Downloader/main/config-sample.yml',
                allow_redirects=True,
                timeout=10
            ).content.decode(encoding='utf-8')
            file.write(content)
        except ConnectionError:
            printError(message='Couldn\'t connect to Repository Source to download the config file. Please check the connection or the source of the repo and try again.')


def checkExistYAMLConfigFile(file_name: str = 'config.yml') -> bool:
    """Check if the config file exists or not

    Params:
        - file_name (str): The name of the config file (Default: config.yml)

    Returns:
        - bool: True if the config file exists, False otherwise
    """
    if path.exists(path=file_name):
        return True
    else:
        printInfo(message=f'{file_name} does not exist')
        return False


def prepareYAMLConfigFile(file_name: str = 'config.yml') -> None:
    """Prepare the config file for the project

    Params:
        - file_name (str): The name of the config file (Default: config.yml)

    Returns:
        - None
    """
    if not checkExistYAMLConfigFile(file_name=file_name):
        downloadYAMLConfigFile(file_name=file_name)
