"""VNULIB Downloader"""


from src import (Browser, Login, PrintIntro,
                 ToolConfig, UserOptions, LinkParse,
                 print_title,
                 logger)
from src.constants import CONFIG_FILE, CONFIG_FILE_URL


def main() -> None:
    """Main function to run VNULIB Downloader"""
    PrintIntro().print_intro()

    print_title(message='SETUP')
    ToolConfig(
        config_file_name=CONFIG_FILE, url=CONFIG_FILE_URL).setup()
    user_options = UserOptions()
    user_options.setup()

    print_title(message='PARSE LINKS')
    link_parse = LinkParse(links=user_options.links)
    user_options.links = link_parse.parse()
    if link_parse.need_to_convert:
        logger.info('There is / are some link(s) need to be converted')
        driver = Browser(browser=user_options.browser,
                         headless=user_options.headless).setup_browser()
        Login(driver=driver,
              username=user_options.username,
              password=user_options.password).login()
        user_options.links = LinkParse.convert(
            driver=driver, links=user_options.links)

    print_title(message='DOWNLOAD')

    print_title(message='PDF')


if __name__ == '__main__':
    main()
