"""Utils for Bot"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


TIMEOUT = 30


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
