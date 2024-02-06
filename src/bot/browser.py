"""Setup Selenium Browser"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.core.logger import set_logger
from webdriver_manager.chrome import ChromeDriverManager
from src.constants import BROWSER_ARGUMENTS
from src.utils.logger import logger


set_logger(logger)


class Browser:
    """Setup Selenium Browser"""

    def __init__(self, browser: str, headless: bool) -> None:
        self.browser: str = browser
        self.headless: bool = headless
        self.options = webdriver.ChromeOptions()
        self.driver: WebDriver

    def setup_browser(self) -> WebDriver:
        """Setup the browser"""
        logger.info(msg='Setting up the browser...')
        self.__setup_arguments()
        match self.browser:
            case 'chrome':
                self.driver = self.__setup_chrome_browser()
            case _:
                self.driver = self.__setup_local_chrome_browser()
        self.driver.implicitly_wait(30)
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

    def __setup_chrome_browser(self) -> WebDriver:
        """Setup Chrome Browser"""
        return webdriver.Chrome(
            options=self.options,
            service=ChromeService(ChromeDriverManager().install()))

    def __setup_local_chrome_browser(self) -> WebDriver:
        """Setup Local Chrome Browser"""
        return webdriver.Chrome(options=self.options, service=ChromeService(self.browser))
