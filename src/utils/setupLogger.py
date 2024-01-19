"""Setup the logger"""


from logging import basicConfig
from datetime import datetime
from tkinter.font import BOLD

from src.utils.setupVariables import LOG
from .utils import createDirectory
from ..utils.printColor import printInfo


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


def setupLogger(LOG: bool | None, LOG_LEVEL: str | None) -> None:
    """Check to decide whether to setup the logger or not

    Params:
        - LOG (bool | None): The LOG variable
        - LOG_LEVEL (str | None): The LOG_LEVEL variable

    Returns:
        - None
    """
    if LOG:
        printInfo(message=f'LOG_LEVEL is set to {LOG_LEVEL}')
        setupLoggerNow(level=LOG_LEVEL)
