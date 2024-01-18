"""Setup the logger"""


from os import getenv
from logging import basicConfig
from datetime import datetime
from utils import createDirectory
from utils.printColor import printWarning, printInfo
from ..CONSTANTS import DOTENV_TRUE_VALUES


def setupLoggerNow(level: str | None = 'INFO') -> None:
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


def setupLogger() -> None:
    """Check to decide whether to setup the logger or not

    Params:
        - None

    Returns:
        - None
    """
    if getenv(key='LOG') in DOTENV_TRUE_VALUES:
        LOG_LEVEL: str | None = getenv(key='LOG_LEVEL')
        if LOG_LEVEL is None:
            printWarning(
                message='LOG_LEVEL is not set in config.env. Defaulting to INFO')
            setupLoggerNow()
        else:
            printInfo(message=f'LOG_LEVEL is set to {LOG_LEVEL}')
            setupLoggerNow(level=LOG_LEVEL)
