from multiprocessing import Queue, current_process
from logging import Logger, Handler, getLogger, getHandlerByName, DEBUG
from logging.handlers import QueueHandler
from .logger import ToolLogger


class QueueHandlerRun:
    """Start the Queue Handler thread.
    Use it by context manager.
    """

    def __init__(self, handler_name: str) -> None:
        """Initialise.

        Args:
            handler_name (str): Name of the handler to get, not logger :)).
        """
        self.handler_name: str = handler_name
        ToolLogger().read_logging_config()
        self._queue_handler: Handler | None = getHandlerByName(handler_name)
        self.queue = Queue(-1)

    @staticmethod
    def logger_listener(queue: Queue):
        logger: Logger = ToolLogger().get_logger("vnulib_downloader")
        while True:
            record = queue.get()
            if record is None:
                break
            logger.handle(record=record)

    @staticmethod
    def get_logger(queue: Queue) -> Logger:
        queue_handler = QueueHandler(queue)
        logger: Logger = getLogger("queue_logger")
        logger.propagate = False
        logger.addHandler(queue_handler)
        logger.setLevel(DEBUG)
        return logger
