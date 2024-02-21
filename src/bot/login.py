"""Use Selenium to log in to the website"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .utils import wait_element_clickable
from ..constants import LOGIN_URL
from ..utils import logger


class Login:
    """Login to the VNULIB website

    Args:
        - driver (WebDriver): Selenium WebDriver
        - username (str): Username
        - password (str): Password
    """

    def __init__(self, driver: WebDriver,
                 username, password) -> None:
        self.driver: WebDriver = driver
        self.username: str = username
        self.password: str = password
        self.url = LOGIN_URL

    def __fill_in(self) -> None:
        """Fill in the login form"""
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="username"]').send_keys(self.username)
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="password"]').send_keys(self.password)

    def login(self) -> None:
        """Login to VNULIB website

        Raises:
            ConnectionError: Login failed
        """
        logger.info(msg='Logging in...')
        self.driver.get(self.url)
        submit_button: WebElement = wait_element_clickable(
            driver=self.driver, css_selector='button[type="submit"]')
        self.__fill_in()
        submit_button.click()
        if "https://ir.vnulib.edu.vn/" in self.driver.current_url:
            logger.info(msg='Logged in successfully!')
        else:
            logger.error(msg='Login failed!')
            raise ConnectionError('Login failed!')
