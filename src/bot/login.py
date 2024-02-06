"""Use Selenium to login to the website"""


from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from .utils import wait_element_visible
from ..utils.logger import logger
from ..constants import LOGIN_URL


class Login:
    """Login to the website"""

    def __init__(self, driver: WebDriver,
                 username, password) -> None:
        self.driver: WebDriver = driver
        self.username: str = username
        self.password: str = password
        self.url = LOGIN_URL

    def __fill_in(self) -> None:
        """Fill in the login form"""
        username_field: WebElement = wait_element_visible(
            driver=self.driver, css_selector='.form-control[name="username"]')
        password_field: WebElement = wait_element_visible(
            driver=self.driver, css_selector='.form-control[name="password"]')
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

    def login(self) -> None:
        """Login to the website"""
        logger.info(msg='Logging in...')
        try:
            self.driver.get(self.url)
        except Exception as e:
            logger.error(msg=f'Error: {e}')
            raise e
        self.__fill_in()
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='button[type="submit"]').click()
        if "https://ir.vnulib.edu.vn/" in self.driver.current_url:
            logger.info(msg='Logged in successfully!')
        else:
            logger.error(msg='Login failed!')
            raise Exception('Login failed!')
