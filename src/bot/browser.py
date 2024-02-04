"""Setup Selenium Browser"""


from selenium import webdriver
# from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
# from selenium.webdriver.ie.service import Service as IEService
# from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
# from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.core.logger import set_logger

from src.constants import BROWSER_ARGUMENTS

from src.utils.logger import logger


set_logger(logger)


class Browser:
    """Setup Selenium Browser"""

    def __init__(self, browser, headless) -> None:
        self.browser: str = browser
        self.headless: bool = headless
        self.options = webdriver.ChromeOptions()
        self.driver: WebDriver

    def setup_browser(self) -> WebDriver:
        """Setup the browser"""
        logger.info(msg='Setting up the browser...')
        self.setup_arguments()
        match self.browser:
            case 'chrome':
                self.driver = self.setup_chrome_browser()
            case 'chromium':
                self.driver = self.setup_chromium_browser()
            case 'brave':
                self.driver = self.setup_brave_browser()
            # case 'edge':
            #     self.driver = self.setup_edge_browser()
            # case 'firefox':
            #     self.driver = self.setup_firefox_browser()
            # case 'ie':
            #     self.driver = self.setup_ie_browser()
            # case 'opera':
            #     self.driver = self.setup_opera_browser()
            case _:
                self.driver = self.setup_local_chrome_browser()
        logger.info(msg=f'Browser {self.browser} setup complete!')
        return self.driver

    def setup_arguments(self) -> None:
        """Setup the browser arguments"""
        for argument in BROWSER_ARGUMENTS:
            self.options.add_argument(argument)
        if self.headless:
            self.options.add_argument('--headless')
            self.options.add_experimental_option(
                "prefs", {"profile.managed_default_content_settings.images": 2}
            )

    def setup_chrome_browser(self) -> WebDriver:
        """Setup Chrome Browser"""
        return webdriver.Chrome(
            options=self.options,
            service=ChromeService(ChromeDriverManager().install()))

    def setup_chromium_browser(self) -> WebDriver:
        """Setup Chromium Browser"""
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    def setup_brave_browser(self) -> WebDriver:
        """Setup Brave Browser"""
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

    def setup_local_chrome_browser(self) -> WebDriver:
        """Setup Local Chrome Browser"""
        return webdriver.Chrome(options=self.options, service=ChromeService(input('Enter the path to the ChromeDriver: )')))

    # def setup_edge_browser(self) -> EdgeWebDriver:
    #     """Setup Edge Browser"""
    #     return webdriver.Edge(
    #         service=EdgeService(EdgeChromiumDriverManager().install()))

    # def setup_firefox_browser(self) -> FirefoxWebDriver:
    #     """Setup Firefox Browser"""
    #     return webdriver.Firefox(
    #         service=FirefoxService(GeckoDriverManager().install()))

    # def setup_ie_browser(self) -> IEDriver:
    #     """Setup IE Browser"""
    #     return webdriver.Ie(
    #         service=IEService(IEDriverManager().install()))

    # def setup_opera_browser(self) -> RemoteWebDriver:
    #     """Setup Opera Browser"""
    #     webdriver_service = service.Service(
    #         OperaDriverManager().install())
    #     webdriver_service.start()
    #     self.options.add_experimental_option('w3c', True)
    #     return webdriver.Remote(
    #         webdriver_service.service_url, options=self.options)
