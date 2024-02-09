"""Utils for Bot"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


TIMEOUT = 30


# def wait_element_visible(driver: ChromeWebDriver | EdgeWebDriver |
#                          FirefoxWebDriver | IEDriver | RemoteWebDriver,
#                          element: WebElement) -> None:
#     """Wait for the element to be visible

#     Params:
#         - driver (ChromeWebDriver | EdgeWebDriver |
#                     FirefoxWebDriver | IEDriver | RemoteWebDriver): Selenium WebDriver
#         - element (WebElement): The element to wait for

#     Returns:
#         - None
#     """
#     wait = WebDriverWait(driver=driver, timeout=10)
#     wait.until(lambda d: element.is_enabled() or element.is_displayed())


# def wait_load_preview_book(driver: ChromeWebDriver | EdgeWebDriver |
#                            FirefoxWebDriver | IEDriver | RemoteWebDriver,
#                            element: WebElement) -> None:
#     """Wait for the preview book to load

#     Params:
#         - driver (ChromeWebDriver | EdgeWebDriver |
#                   FirefoxWebDriver | IEDriver | RemoteWebDriver): Selenium WebDriver
#         - element (WebElement): The element to wait for (preview page)

#     Returns:
#         - None
#     """
#     errors = [NoSuchElementException]
#     wait = WebDriverWait(
#         driver, timeout=10, poll_frequency=0.5, ignored_exceptions=errors)
#     wait.until(lambda d: element.send_keys("Displayed") or True)


def wait_element_visible(driver: WebDriver, css_selector: str) -> WebElement:
    """Wait for the element to be visible in DOM

    Params:
        - driver (WebDriver): Selenium WebDriver
        - css_selector (str): CSS selector

    Returns:
        - WebElement: The element
    """
    return WebDriverWait(driver, timeout=TIMEOUT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )


def wait_element_clickable(driver: WebDriver, css_selector: str) -> WebElement:
    """Wait for the element to be clickable

    Params:
        - driver (WebDriver): Selenium WebDriver
        - css_selector (str): CSS selector

    Returns:
        - WebElement: The element
    """
    return WebDriverWait(driver, timeout=TIMEOUT).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
