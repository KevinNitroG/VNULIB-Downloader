"""VNULIB Downloader"""

from selenium.webdriver.chrome.webdriver import WebDriver

from src.bot import Browser, Login
from src.utils import logger
from src.utils import print_title
from src.modules import setup_argparse
from src.modules import PrintIntro, ToolConfig, UserOptions, RawParseLinks, ConvertParseLink
from src.constants import CONFIG_FILE, CONFIG_FILE_URL


def main() -> None:
    """Main function to run VNULIB Downloader"""
    PrintIntro().print_intro()

    print_title(message='SETUP')
    ToolConfig(
        config_file_name=CONFIG_FILE, url=CONFIG_FILE_URL).setup_config_file()
    user_options: dict = {
        'username': '',
        'password': '',
        'links': [],
        'browser': '',
        'headless': False,
        'create_pdf': False,
        'clean_imgs': False,
    }
    user_options = UserOptions(
        argparse=setup_argparse(), config_file=CONFIG_FILE, user_options=user_options).setup()

    print_title(message='PARSE LINKS')
    raw_parser = RawParseLinks(links=user_options['links'])
    list_of_links: list[dict] = raw_parser.parse()
    if raw_parser.need_to_convert:
        logger.info('There is / are some link(s) need to be converted')
        driver: WebDriver = Browser(browser=user_options['browser'],
                                    headless=user_options['headless']).setup_browser()
        Login(driver=driver,
              username=user_options['username'],
              password=user_options['password']).login()
        list_of_links = ConvertParseLink(
            driver=driver, links=list_of_links).convert()

    print_title(message='DOWNLOAD')

    print_title(message='PDF')


if __name__ == '__main__':
    main()
