"""Constant variables throughout the program."""

from __future__ import annotations
import sys


if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    BUNDLE_DIR: str = f"{sys._MEIPASS}/"  # type: ignore # skipcq: PYL-W0212 # pylint: disable=protected-access # nopep8
else:
    BUNDLE_DIR = ""


VERSION: str = "1.10"
AUTHORS: str = "KevinNitroG & NTGNguyen"
BANNER: str = """
██╗   ██╗███╗   ██╗██╗   ██╗██╗     ██╗██████╗ 
██║   ██║████╗  ██║██║   ██║██║     ██║██╔══██╗
██║   ██║██╔██╗ ██║██║   ██║██║     ██║██████╔╝
╚██╗ ██╔╝██║╚██╗██║██║   ██║██║     ██║██╔══██╗
 ╚████╔╝ ██║ ╚████║╚██████╔╝███████╗██║██████╔╝
  ╚═══╝  ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝╚═════╝ 

██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
REPOSITORY_URL: str = "https://github.com/KevinNitroG/VNULIB-Downloader"
CONFIG_FILE: str = "config.yml"
CONFIG_SAMPLE_FILE: str = f"{BUNDLE_DIR}config-sample.yml"
CONFIG_FILE_URL: str = "https://raw.githubusercontent.com/KevinNitroG/VNULIB-Downloader/main/config-sample.yml"  # skipcq: [FLK-E501, FLK-W505]
LOGGING_CONFIG_FILE_PATH: str = f"{BUNDLE_DIR}src/logging_configuration.yml"
LOGGING_PATH: str = "log"
ERROR_PAGE_IMAGE_PATH: str = "assets/images/error_page.jpg"
DOWNLOAD_DIR: str = "Downloads"
LOGGER_MODE: list[str] = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
USER_INPUT_YES: list[str] = ["Y", "YES", "", "1"]
USER_INPUT_NO: list[str] = ["N", "NO", "", "0"]
LOGIN_URL: str = "https://ir.vnulib.edu.vn/login/oa/dologin.jsp?RedirectURL=/"
# https://jtway.co/optimize-your-chrome-options-for-testing-to-get-x1-25-impact-4f19f071bf45
BROWSER_ARGUMENTS: set[str] = {
    "--allow-running-insecure-content",
    "--autoplay-policy=user-gesture-required",
    "--disable-add-to-shelf",
    "--disable-background-networking",
    "--disable-background-timer-throttling",
    "--disable-backgrounding-occluded-windows",
    "--disable-breakpad",
    "--disable-checker-imaging",
    "--disable-client-side-phishing-detection",
    "--disable-component-extensions-with-background-pages",
    "--disable-datasaver-prompt",
    "--disable-default-apps",
    "--disable-desktop-notifications",
    "--disable-dev-shm-usage",
    "--disable-domain-reliability",
    "--disable-extensions",
    "--disable-features=TranslateUI,BlinkGenPropertyTrees",
    "--disable-hang-monitor",
    "--disable-infobars",
    "--disable-ipc-flooding-protection",
    "--disable-logging",
    "--disable-notifications",
    "--disable-popup-blocking",
    "--disable-prompt-on-repost",
    "--disable-renderer-backgrounding",
    "--disable-setuid-sandbox",
    "--disable-site-isolation-trials",
    "--disable-sync",
    "--disable-web-security",
    "--ignore-certificate-errors",
    "--mute-audio",
    "--no-default-browser-check",
    "--no-first-run",
    "--no-sandbox",
    "--password-store=basic",
    "--ignore-certificate-errors-spki-list",
    "--ignore-ssl-errors",
    "--log-level=3",
    "--silent",
    "--disable-gpu",
}
