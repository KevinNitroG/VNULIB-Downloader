"""VNULIB Downloader."""

from __future__ import annotations

from logging import Logger, getLogger
from multiprocessing import freeze_support
from pprint import pformat

from urllib3 import disable_warnings as urllib3_disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from src import Action, Browser, CleanIMG, Config, CreatePDF, DownloadIMG, LinkParse, Login, PrintIntro, ToolLogger, UserOptions, create_directory, delete_old_meipass, pause, print_title
from src.constants import DOWNLOAD_DIR


def main() -> None:
    """Main function to run VNULIB Downloader."""
    logger: Logger = getLogger(__name__)
    delete_old_meipass(time_threshold=300)

    PrintIntro()

    print_title("USER OPTIONS")
    Config()
    user_options = UserOptions()
    user_options.setup()

    print_title("PARSE LINKS")
    link_parser = LinkParse(links=user_options.links)
    link_parser.parse()
    user_options.links = link_parser.links
    if link_parser.need_to_process:
        logger.info("There is / are some link(s) need to be processed")
        print_title("PROCESS LINKS")
        with Browser(browser=user_options.browser, headless=user_options.headless, timeout=user_options.timeout) as driver:
            Login(driver=driver, username=user_options.username, password=user_options.password, timeout=user_options.timeout).login()
            bot_action = Action(timeout=user_options.timeout, driver=driver, links=user_options.links)
            bot_action.run()
            user_options.links = bot_action.links
    logger.debug("LINKS OBJECT:\n%s", pformat(user_options.links))

    print_title("DOWNLOAD")
    create_directory(DOWNLOAD_DIR, force=False)
    DownloadIMG(links=user_options.links, download_directory=DOWNLOAD_DIR, timeout=user_options.timeout).dowload()

    if user_options.create_pdf:
        print_title("PDF")
        CreatePDF(user_options.links, DOWNLOAD_DIR).create_pdf()

    if user_options.clean_img:
        print_title("DELETE IMAGES")
        CleanIMG(user_options.links, DOWNLOAD_DIR).clean_img()

    print_title("END PROGRAM")
    pause()


ToolLogger().setup()


if __name__ == "__main__":
    freeze_support()  # For pyinstaller to fix multiprocessing in Windows due to freeze scheme
    urllib3_disable_warnings(InsecureRequestWarning)
    main()
