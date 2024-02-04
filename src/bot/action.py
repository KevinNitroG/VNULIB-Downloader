"""Contains Bot actions: Book website -> Book preview -> Book page link"""


from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class Action:
    """Bot actions for the bot to perform"""

    @staticmethod
    def book_web_to_page(driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver, url: str) -> str:
        """Book website link to book page link

        Params:
            - driver (ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver): Selenium WebDriver
            - url (str): Book website link

        Returns:

        """
        driver.get(url)
        return ''

    @staticmethod
    def book_preview_to_page(driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver, url: str) -> str:
        """Book preview link to book page link

        Params:
            - driver (ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver): Selenium WebDriver
            - url (str): Book preview link

        Returns:
        """
        driver.get(url)
        return ''
