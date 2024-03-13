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
    """Setup Selenium Browser."""

    def __init__(self, browser: str, headless: bool, timeout: int) -> None:
        """Initialise for Browser.

        Args:
            - browser (str): The browser to set up.
            - headless (bool): Headless mode.
            - timeout (int): Timeout for implicit wait for Selenium.
        """
        self._browser: str = browser  # skipcq: PTC-W0052
        self._headless: bool = headless
        self._options = webdriver.ChromeOptions()
        self.driver: WebDriver
        self._timeout: int = timeout

    def __enter__(self) -> WebDriver:
        """Set up the browser when entering the context manager.

        Returns:
            - WebDriver: Selenium WebDriver.
        """
        logger.info("Setting up the browser...")
        self._setup_arguments()
        match self._browser.strip():
            case "chrome" | "":
                self.driver = self._setup_chrome_browser()
            case _:
                self.driver = self._setup_local_chrome_browser()
        self.driver.implicitly_wait(self._timeout)
        logger.info('Browser "%s" setup complete!', self._browser)
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Exit the context manager"""
        logger.info("Quit the browser")
        self.driver.quit()

    def _setup_arguments(self) -> None:
        """Set up the browser arguments"""
        for argument in BROWSER_ARGUMENTS:
            self._options.add_argument(argument)
        if self._headless:
            self._options.add_argument("--headless")
            self._options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    def _setup_chrome_browser(self) -> WebDriver:
        """Setup Chrome Browser.

        Returns:
            - WebDriver: Selenium WebDriver.
        """
        return webdriver.Chrome(options=self._options, service=Service(ChromeDriverManager().install()))

    def _setup_local_chrome_browser(self) -> WebDriver:
        """Setup Local Chrome Browser.

        Returns:
            - WebDriver: Selenium WebDriver.
        """
        return webdriver.Chrome(options=self._options, service=Service(self._browser))
