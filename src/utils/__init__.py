from os import get_terminal_size
from setupDotEnv import setupConfigEnv


TERMINAL_SIZE_COLUMNS: int = get_terminal_size().columns


setupConfigEnv()
