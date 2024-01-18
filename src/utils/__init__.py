from os import get_terminal_size
from dotenv import load_dotenv
from setupDotEnv import setupConfigEnv
from setupLogger import setupLogger


TERMINAL_SIZE_COLUMNS: int = get_terminal_size().columns


setupConfigEnv()
load_dotenv(dotenv_path='config.env')

setupLogger()
