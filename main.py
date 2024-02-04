"""VNULIB Downloader"""


from src import (Browser, Login, PrintIntro,
                 ToolConfig, UserOptions, LinkParse,
                 setup_argparse, print_title,
                 logger)
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
    link_parse = LinkParse(links=user_options['links'])
    links_dict: list[dict] = link_parse.setup()
    if link_parse.need_to_convert:
        logger.info('There is / are some link(s) need to be converted')
        driver = Browser(browser=user_options['browser'],
                         headless=user_options['headless']).setup_browser()
        Login(driver=driver,
              username=user_options['username'],
              password=user_options['password']).login()
        links_dict = LinkParse.convert(
            driver=driver, links_dict=links_dict)

    print_title(message='DOWNLOAD')

    print_title(message='PDF')


if __name__ == '__main__':
    main()
