"""Setup the logger"""


from logging import Logger, getLogger, Formatter, FileHandler, INFO, DEBUG, WARNING, ERROR, CRITICAL
from datetime import datetime

from .utils import createDirectory


def setupLoggerNow(LOG_LEVEL: str | None = 'INFO') -> Logger:
    """Setup the logger

    Params:
        - LOG_LEVEL (str | None): The level to log at. Only accept DEBUG, INFO, WARNING, ERROR, CRITICAL

    Returns:
        - Logger: The logger
    """
    file_name: str = datetime.now().strftime(format='%Y-%m-%d-%H-%M-%S') + '.log'
    LOGGER: Logger = getLogger()
    match LOG_LEVEL:
        case 'DEBUG':
            LOGGER.setLevel(level=DEBUG)
        case 'INFO':
            LOGGER.setLevel(level=INFO)
        case 'WARNING':
            LOGGER.setLevel(level=WARNING)
        case 'ERROR':
            LOGGER.setLevel(level=ERROR)
        case 'CRITICAL':
            LOGGER.setLevel(level=CRITICAL)
        case _:
            LOGGER.setLevel(level=INFO)
    file_handler: FileHandler = FileHandler(filename=f'logs/{file_name}')
    format = Formatter(
        '%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d')
    file_handler.setFormatter(fmt=format)
    LOGGER.addHandler(hdlr=file_handler)
    return LOGGER


def setupLogger(LOG: bool | None) -> Logger | None:
    """Check to decide whether to setup the logger or not

    Params:
        - LOG (bool | None): The LOG variable

    Returns:
        - Logger | None: The logger
    """
    if LOG:
        createDirectory('logs')
        return setupLoggerNow()
    return None
