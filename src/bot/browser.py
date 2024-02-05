"""Setup Selenium Browser"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from webdriver_manager.core.logger import set_logger
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from selenium.webdriver.chrome import service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager

from src.constants import BROWSER_ARGUMENTS

from src.utils.logger import logger


set_logger(logger)


class Browser:
    """Setup Selenium Browser"""

    def __init__(self, browser: str, headless: bool) -> None:
        self.browser: str = browser
        self.headless: bool = headless
        self.options = webdriver.ChromeOptions()
        self.driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver

    def setup_browser(self) -> ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver:
        """Setup the browser"""
        logger.info(msg='Setting up the browser...')
        self.__setup_arguments()
        match self.browser:
            case 'chrome':
                self.driver = self.__setup_chrome_browser()
            case 'chromium':
                self.driver = self.__setup_chromium_browser()
            case 'brave':
                self.driver = self.__setup_brave_browser()
            case 'edge':
                self.driver = self.__setup_edge_browser()
            case 'firefox':
                self.driver = self.__setup_firefox_browser()
            case 'ie':
                self.driver = self.__setup_ie_browser()
            case 'opera':
                self.driver = self.__setup_opera_browser()
            case _:
                self.driver = self.__setup_local_chrome_browser()
        logger.info(msg=f'Browser {self.browser} setup complete!')
        return self.driver

    def __setup_arguments(self) -> None:
        """Setup the browser arguments"""
        for argument in BROWSER_ARGUMENTS:
            self.options.add_argument(argument)
        if self.headless:
            self.options.add_argument('--headless')
            self.options.add_experimental_option(
                "prefs", {"profile.managed_default_content_settings.images": 2}
            )

    def __setup_chrome_browser(self) -> ChromeWebDriver:
        """Setup Chrome Browser"""
        return webdriver.Chrome(
            options=self.options,
            service=ChromeService(ChromeDriverManager().install()))

    def __setup_chromium_browser(self) -> ChromeWebDriver:
        """Setup Chromium Browser"""
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    def __setup_brave_browser(self) -> ChromeWebDriver:
        """Setup Brave Browser"""
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

    def __setup_local_chrome_browser(self) -> ChromeWebDriver:
        """Setup Local Chrome Browser"""
        return webdriver.Chrome(options=self.options, service=ChromeService(self.browser))

    def __setup_edge_browser(self) -> EdgeWebDriver:
        """Setup Edge Browser"""
        return webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()))

    def __setup_firefox_browser(self) -> FirefoxWebDriver:
        """Setup Firefox Browser"""
        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))

    def __setup_ie_browser(self) -> IEDriver:
        """Setup IE Browser"""
        return webdriver.Ie(
            service=IEService(IEDriverManager().install()))

    def __setup_opera_browser(self) -> RemoteWebDriver:
        """Setup Opera Browser"""
        webdriver_service = service.Service(
            OperaDriverManager().install())
        webdriver_service.start()
        self.options.add_experimental_option('w3c', True)
        return webdriver.Remote(
            webdriver_service.service_url, options=self.options)
