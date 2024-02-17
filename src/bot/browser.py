"""Setup Selenium Browser"""


import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.core.logger import set_logger
from webdriver_manager.chrome import ChromeDriverManager
import urllib3
from src.constants import BROWSER_ARGUMENTS
from src.utils.logger import logger


set_logger(logger)
os.environ['WDM_LOG'] = str(logging.DEBUG)
os.environ['WDM_SSL_VERIFY'] = '0'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Browser:
    """Setup Selenium Browser

    Args:
        - browser (str): The browser to setup
        - headless (bool): Headless mode
    """

    def __init__(self, browser: str, headless: bool) -> None:
        self.browser: str = browser  # skipcq: PTC-W0052
        self.headless: bool = headless
        self.options = webdriver.ChromeOptions()
        self.driver: WebDriver

    def __enter__(self) -> WebDriver:
        """Setup the browser when entering the context manager

        Returns:
            - WebDriver: Selenium WebDriver
        """
        logger.info(msg='Setting up the browser...')
        self.__setup_arguments()
        match self.browser:
            case 'chrome':
                self.driver = self.__setup_chrome_browser()
            case _:
                self.driver = self.__setup_local_chrome_browser()
        self.driver.implicitly_wait(15)
        logger.info(msg=f'Browser \'{self.browser}\' setup complete!')
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Exit the context manager"""
        logger.info(msg='Quit the browser')
        self.driver.quit()

    def __setup_arguments(self) -> None:
        """Setup the browser arguments"""
        for argument in BROWSER_ARGUMENTS:
            self.options.add_argument(argument)
        if self.headless:
            self.options.add_argument('--headless')
            self.options.add_experimental_option(
                "prefs", {"profile.managed_default_content_settings.images": 2}
            )

    def __setup_chrome_browser(self) -> WebDriver:
        """Setup Chrome Browser

        Returns:
            - WebDriver: Selenium WebDriver
        """
        return webdriver.Chrome(
            options=self.options,
            service=Service(ChromeDriverManager().install()))

    def __setup_local_chrome_browser(self) -> WebDriver:
        """Setup Local Chrome Browser

        Returns:
            - WebDriver: Selenium WebDriver
        """
        return webdriver.Chrome(options=self.options, service=Service(self.browser))
