"""VNULIB Downloader"""


from src.bot import Browser, Login
from src.utils import print_title
from src.modules import setup_argparse
from src.modules import PrintIntro, ToolConfig, UserOptions
from src.constants import CONFIG_FILE, CONFIG_FILE_URL


def main() -> None:
    """Main function to run VNULIB Downloader"""
    PrintIntro().print_intro()
    print_title(message='SETUP')
    ToolConfig(
        config_file_name=CONFIG_FILE, url=CONFIG_FILE_URL).setup_config_file()
    user_options = UserOptions(
        argparse=setup_argparse(), config_file=CONFIG_FILE).setup()
    print_title(message='BROWSER')
    driver = Browser(browser=user_options['browser'],
                     headless=user_options['headless']).setup_browser()
    Login(driver=driver,
          username=user_options['username'],
          password=user_options['password']).login()


if __name__ == '__main__':
    main()
