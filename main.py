"""VNULIB Downloader"""

from pprint import pformat
from src import (Browser, Login, Action,
                 PrintIntro, Config, UserOptions, LinkParse,
                 print_title, pause,
                 logger)


def main() -> None:
    """Main function to run VNULIB Downloader"""
    PrintIntro()

    print_title('USER OPTIONS')
    Config()
    user_options = UserOptions()
    user_options.setup()

    print_title('PARSE LINKS')
    link_parse = LinkParse(links=user_options.links)
    user_options.links = link_parse.parse()
    if link_parse.need_to_process:
        logger.info('There is / are some link(s) need to be processed')
        print_title('PROCESS LINKS')
        with Browser(browser=user_options.browser,
                     headless=user_options.headless) as driver:
            Login(driver=driver,
                  username=user_options.username,
                  password=user_options.password).login()
            user_options.links = LinkParse(links=user_options.links).parse()
            user_options.links = Action(driver=driver,
                                        links=user_options.links).action()
    logger.debug(msg=f'LINKS OBJECT:\n{pformat(user_options.links)}')

    print_title('DOWNLOAD')

    print_title('PDF')


if __name__ == '__main__':
    main()
    pause()
