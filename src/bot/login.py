"""Use Selenium to login to the website"""


from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from src.utils.logger import logger

from src.constants import LOGIN_URL


class Login:
    """Login to the website"""

    def __init__(self, driver: ChromeWebDriver | EdgeWebDriver |
                 FirefoxWebDriver | IEDriver | RemoteWebDriver,
                 username, password) -> None:
        self.driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver = driver
        self.username: str = username
        self.password: str = password
        self.url = LOGIN_URL

    def login(self) -> None:
        """Login to the website"""
        logger.info(msg='Logging in...')
        try:
            self.driver.get(self.url)
        except Exception as e:
            logger.error(msg=f'Error: {e}')
            raise e
        self.fill_in()
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='button[type="submit"]').click()
        logger.info(msg='Logged in successfully!')

    def fill_in(self) -> None:
        """Fill in the login form"""
        username_field: WebElement = self.driver.find_element(
            by=By.NAME, value='username')
        password_field: WebElement = self.driver.find_element(
            by=By.NAME, value='password')
        wait = WebDriverWait(driver=self.driver, timeout=10)
        wait.until(lambda d: username_field.is_displayed()
                   and password_field.is_displayed())
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
