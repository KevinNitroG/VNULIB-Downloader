"""Use Selenium to login to the website"""


from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from selenium.webdriver.common.by import By


class Login:
    """Login to the website"""

    def __init__(self, driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver,
                 username: str, password: str) -> None:
        self.driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver = driver
        self.username: str = username
        self.password: str = password
        self.url = 'https://ir.vnulib.edu.vn/login/oa/dologin.jsp'

    def login(self) -> None:
        """Login to the website"""
        self.driver.get(self.url)
        self.driver.find_element(
            by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(
            by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='button[type="submit"]').click()
