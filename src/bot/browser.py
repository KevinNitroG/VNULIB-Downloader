"""Setup Selenium Browser"""


from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager

from src.utils.utils import create_directory
from src.constants import BROWSER_ARGUMENTS


class Browser:
    """Setup Selenium Browser"""

    def __init__(self, browser, headless) -> None:
        self.browser: str = browser
        self.headless: bool = headless
        self.options = webdriver.ChromeOptions()
        self.driver: ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver

    def setup_browser(self) -> ChromeWebDriver | EdgeWebDriver | FirefoxWebDriver | IEDriver | RemoteWebDriver:
        """Setup the browser"""
        create_directory('Profiles')
        for argument in BROWSER_ARGUMENTS:
            self.options.add_argument(argument)
        self.options.add_experimental_option("detach", True)
        if self.headless:
            self.options.add_argument('--headless')
            self.options.add_experimental_option(
                "prefs", {"profile.managed_default_content_settings.images": 2}
            )
            self.options.add_argument('--disable-gpu')
        match self.browser:
            case 'chrome':
                self.driver = self.setup_chrome_browser()
            case 'chromium':
                self.driver = self.setup_chromium_browser()
            case 'brave':
                self.driver = self.setup_brave_browser()
            case 'edge':
                self.driver = self.setup_edge_browser()
            case 'firefox':
                self.driver = self.setup_firefox_browser()
            case 'ie':
                self.driver = self.setup_ie_browser()
            case 'opera':
                self.driver = self.setup_opera_browser()
            case _:
                self.driver = self.setup_chrome_browser()
        return self.driver

    def setup_chrome_browser(self) -> ChromeWebDriver:
        """Setup Chrome Browser"""
        self.options.add_argument('--user-data-dir=Profiles/Chrome')
        return webdriver.Chrome(options=self.options,
                                service=ChromeService(ChromeDriverManager().install()))

    def setup_chromium_browser(self) -> ChromeWebDriver:
        """Setup Chromium Browser"""
        self.options.add_argument('--user-data-dir=Profiles/Chromium')
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    def setup_brave_browser(self) -> ChromeWebDriver:
        """Setup Brave Browser"""
        self.options.add_argument('--user-data-dir=Profiles/Brave')
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

    def setup_edge_browser(self) -> EdgeWebDriver:
        """Setup Edge Browser"""
        self.options.add_argument('--user-data-dir=Profiles/Edge')
        return webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()))

    def setup_firefox_browser(self) -> FirefoxWebDriver:
        """Setup Firefox Browser"""
        self.options.add_argument('--user-data-dir=Profiles/Firefox')
        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))

    def setup_ie_browser(self) -> IEDriver:
        """Setup IE Browser"""
        self.options.add_argument('--user-data-dir=Profiles/IE')
        return webdriver.Ie(
            service=IEService(IEDriverManager().install()))

    def setup_opera_browser(self) -> RemoteWebDriver:
        """Setup Opera Browser"""
        webdriver_service = service.Service(
            OperaDriverManager().install())
        webdriver_service.start()
        self.options.add_argument('--user-data-dir=Profiles/Opera')
        self.options.add_experimental_option('w3c', True)
        return webdriver.Remote(
            webdriver_service.service_url, options=self.options)
