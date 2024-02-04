"""Contains Bot actions: Book website -> Book preview -> Book page link"""


from selenium.webdriver.chrome.webdriver import WebDriver


class Action:
    """Bot actions for the bot to perform"""

    @staticmethod
    def book_web_to_page(driver: WebDriver, url: str) -> str:
        """Book website link to book preview link"""
        driver.get(url)
        return ''

    @staticmethod
    def book_preview_to_page(driver: WebDriver, url: str) -> str:
        """Book preview link to book page link"""
        driver.get(url)
        return ''
