"""Utilities for Bot."""

from __future__ import annotations

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_element_visible(driver: WebDriver, css_selector: str, timeout: int) -> WebElement:
    """Wait for the element to be visible in DOM.

    Args:
        - driver (WebDriver): Selenium WebDriver.
        - css_selector (str): CSS selector.
        - timeout (int): Timeout to wait for element to be visible.

    Returns:
        - WebElement: The element.
    """
    return WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def wait_element_clickable(driver: WebDriver, css_selector: str, timeout: int) -> WebElement:
    """Wait for the element to be clickable.

    Args:
        - driver (WebDriver): Selenium WebDriver.
        - css_selector (str): CSS selector.
        - timeout (int): Timeout to wait for element to be visible.

    Returns:
        - WebElement: The element.
    """
    return WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
