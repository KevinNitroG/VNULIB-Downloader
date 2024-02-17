"""VNULIB Downloader"""

from pprint import pformat
from src import (Browser, Login, Action,
                 PrintIntro, Config, UserOptions, LinkParse,
                 print_title, pause,
                 logger)


def main() -> None:
    """Main function to run VNULIB Downloader"""
    PrintIntro().print_intro()

    print_title(message='SETUP')
    Config().setup()
    user_options = UserOptions()
    user_options.setup()

    print_title(message='PARSE LINKS')
    link_parse = LinkParse(links=user_options.links)
    user_options.links = link_parse.parse()
    if link_parse.need_to_convert:
        logger.info('There is / are some link(s) need to be processed')
        with Browser(browser=user_options.browser,
                     headless=user_options.headless) as driver:
            Login(driver=driver,
                  username=user_options.username,
                  password=user_options.password).login()
            user_options.links = LinkParse(links=user_options.links).parse()
            user_options.links = Action(driver=driver,
                                        links=user_options.links).action()
    logger.debug(msg='LINKS OBJECT:\n'
                 f'{pformat(user_options.links)}')

    print_title(message='DOWNLOAD')

    print_title(message='PDF')


if __name__ == '__main__':
    main()
    pause()
