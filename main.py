"""VNULIB Downloader."""

from __future__ import annotations

from pprint import pformat
from multiprocessing import freeze_support
from logging import Logger
from src import (
    Action,
    Browser,
    Config,
    CreatePDF,
    CleanIMG,
    DownloadIMG,
    LinkParse,
    Login,
    PrintIntro,
    UserOptions,
    create_directory,
    ToolLogger,
    pause,
    print_title,
)
from src.constants import DOWNLOAD_DIR


def main() -> None:
    """Main function to run VNULIB Downloader."""
    logger: Logger = ToolLogger().get_logger("vnulib_downloader")

    PrintIntro()

    print_title("USER OPTIONS")
    Config()
    user_options = UserOptions()
    user_options.setup()

    print_title("PARSE LINKS")
    link_parse = LinkParse(links=user_options.links)
    user_options.links = link_parse.parse()
    if link_parse.need_to_process:
        logger.info("There is / are some link(s) need to be processed")
        print_title("PROCESS LINKS")
        with Browser(
            browser=user_options.browser,
            headless=user_options.headless,
            timeout=user_options.timeout,
        ) as driver:
            Login(
                driver=driver,
                username=user_options.username,
                password=user_options.password,
                timeout=user_options.timeout,
            ).login()
            user_options.links = Action(
                timeout=user_options.timeout,
                driver=driver,
                links=user_options.links,
            ).action()
    logger.debug(msg=f"LINKS OBJECT:\n{pformat(user_options.links)}")

    print_title("DOWNLOAD")
    create_directory(DOWNLOAD_DIR, force=False)
    DownloadIMG(
        links=user_options.links,
        download_directory=DOWNLOAD_DIR,
        timeout=user_options.timeout,
    ).dowload()

    if user_options.create_pdf:
        print_title("PDF")
        CreatePDF(user_options.links, DOWNLOAD_DIR).create_pdf()

    if user_options.clean_img:
        print_title("DELETE IMAGES")
        CleanIMG(user_options.links, DOWNLOAD_DIR).clean_img()

    print_title("END PROGRAM")
    pause()


if __name__ == "__main__":
    freeze_support()  # For pyinstaller to fix multiprocessing in Windows
    main()
