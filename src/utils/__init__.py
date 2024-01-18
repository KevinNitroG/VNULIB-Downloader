from os import get_terminal_size, getenv
from typing import Literal
from logging import basicConfig
from datetime import datetime
from dotenv import load_dotenv
from utils import createDirectory
from utils.printColor import printWarning, printInfo


LOGGER_MODE = Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
DOTENV_TRUE_VALUES: list[str] = ['True', 'true', '1']
DOTENV_FALSE_VALUES: list[str] = ['False', 'false', '0', '', ' ']
TERMINAL_SIZE_COLUMNS: int = get_terminal_size().columns


def pause() -> None:
    """Pause the terminal until user hits Enter

    Params:
        - None

    Returns:
        - None
    """
    _: str = input('Press Enter to continue . . .')


def setupLogger(level: str | None = 'INFO') -> None:
    """Setup the logger

    Params:
        - level (str | None): The level to log at. Only accept DEBUG, INFO, WARNING, ERROR, CRITICAL

    Returns:
        - None
    """
    createDirectory('logs')
    file_name: str = datetime.now().strftime(format='%Y-%m-%d-%H-%M-%S') + '.log'
    basicConfig(
        filename=f'log/{file_name}',
        format="%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d",
        level=level
    )


# SETUP LOGGER
load_dotenv(dotenv_path='config.env')
if getenv(key='LOG') in DOTENV_TRUE_VALUES:
    LOG_LEVEL: str | None = getenv(key='LOG_LEVEL')
    if LOG_LEVEL is None:
        printWarning(
            message='LOG_LEVEL is not set in config.env. Defaulting to INFO')
        setupLogger()
    else:
        printInfo(message=f'LOG_LEVEL is set to {LOG_LEVEL}')
        setupLogger(level=LOG_LEVEL)
