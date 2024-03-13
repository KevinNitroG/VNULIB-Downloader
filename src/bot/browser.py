"""Setup Selenium Browser."""

from __future__ import annotations

from logging import getLogger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from src.constants import BROWSER_ARGUMENTS


logger = getLogger(__name__)


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
        logger.info("Setting up the browser...")
        self.__setup_arguments()
        match self.browser.strip():
            case "chrome" | "":
                self.driver = self.__setup_chrome_browser()
            case _:
                self.driver = self.__setup_local_chrome_browser()
        self.driver.implicitly_wait(self.timeout)
        logger.info('Browser "%s" setup complete!', self.browser)
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Exit the context manager"""
        logger.info("Quit the browser")
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
