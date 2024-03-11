"""Setup Selenium Browser."""

from __future__ import annotations

import logging
import os
import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.logger import set_logger
from src.constants import BROWSER_ARGUMENTS
from ..utils import ToolLogger


logger = ToolLogger().get_logger("vnulib_downloader")

set_logger(logger)
os.environ["WDM_LOG"] = str(logging.DEBUG)
os.environ["WDM_SSL_VERIFY"] = "0"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Browser:
    """Setup Selenium Browser.

    Args:
        - browser (str): The browser to set up.
        - headless (bool): Headless mode.
        - timeout (int): Timeout for implicit wait for Selenium.
    """

    def __init__(self, browser: str, headless: bool, timeout: int) -> None:
        self.browser: str = browser  # skipcq: PTC-W0052
        self.headless: bool = headless
        self.options = webdriver.ChromeOptions()
        self.driver: WebDriver
        self.timeout: int = timeout

    def __enter__(self) -> WebDriver:
        """Set up the browser when entering the context manager.

        Returns:
            - WebDriver: Selenium WebDriver.
        """
        logger.info(msg="Setting up the browser...")
        self.__setup_arguments()
        match self.browser.strip():
            case "chrome" | "":
                self.driver = self.__setup_chrome_browser()
            case _:
                self.driver = self.__setup_local_chrome_browser()
        self.driver.implicitly_wait(self.timeout)
        logger.info(msg=f'Browser "{self.browser}" setup complete!')
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Exit the context manager"""
        logger.info(msg="Quit the browser")
        self.driver.quit()

    def __setup_arguments(self) -> None:
        """Set up the browser arguments"""
        for argument in BROWSER_ARGUMENTS:
            self.options.add_argument(argument)
        if self.headless:
            self.options.add_argument("--headless")
            self.options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    def __setup_chrome_browser(self) -> WebDriver:
        """Setup Chrome Browser.

        Returns:
            - WebDriver: Selenium WebDriver.
        """
        return webdriver.Chrome(options=self.options, service=Service(ChromeDriverManager().install()))

    def __setup_local_chrome_browser(self) -> WebDriver:
        """Setup Local Chrome Browser.

        Returns:
            - WebDriver: Selenium WebDriver.
        """
        return webdriver.Chrome(options=self.options, service=Service(self.browser))
