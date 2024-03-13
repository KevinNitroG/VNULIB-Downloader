"""Use Selenium to log in to the website."""

from __future__ import annotations

from logging import getLogger
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .utils import wait_element_clickable
from ..constants import LOGIN_URL


logger = getLogger(__name__)


class Login:
    """Login to the VNULIB website."""

    _LOGIN_URL = LOGIN_URL

    def __init__(self, driver: WebDriver, username, password, timeout: int) -> None:
        """Initialise for Login of Bot.

        Args:
            driver (WebDriver): Selenium WebDriver.
            username (str): Username.
            password (str): Password.
            timeout (int): Time to wait for element to be visible.
        """
        self._driver: WebDriver = driver
        self._username: str = username
        self._password: str = password
        self._timeout: int = timeout

    def _fill_in(self) -> None:
        """Fill in the login form"""
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="username"]').send_keys(self._username)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="password"]').send_keys(self._password)

    def login(self) -> None:
        """Login to VNULIB website.

        Raises:
            ConnectionError: Login failed.
        """
        logger.info("Logging in...")
        self._driver.get(self._LOGIN_URL)
        submit_button: WebElement = wait_element_clickable(
            driver=self._driver,
            css_selector='button[type="submit"]',
            timeout=self._timeout,
        )
        self._fill_in()
        submit_button.click()
        if "https://ir.vnulib.edu.vn/" in self._driver.current_url:
            logger.info("Logged in successfully!")
        else:
            logger.error("Login failed!")
            raise ConnectionError("Login failed!")
