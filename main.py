"""VNULIB Downloader"""

from __future__ import annotations

from pprint import pformat

from src import (
    Action,
    Browser,
    Config,
    CreatePDF,
    DeleteIMG,
    DownloadIMG,
    LinkParse,
    Login,
    PrintIntro,
    UserOptions,
    create_directory,
    logger,
    pause,
    print_title,
)
from src.constants import DOWNLOAD_DIR


def main() -> None:
    """Main function to run VNULIB Downloader"""
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
            ).login()
            user_options.links = LinkParse(links=user_options.links).parse()
            user_options.links = Action(
                driver=driver, links=user_options.links
            ).action()
    logger.debug(msg=f"LINKS OBJECT:\n{pformat(user_options.links)}")

    create_directory(DOWNLOAD_DIR, force=False)

    print_title("DOWNLOAD")
    DownloadIMG(
        links=user_options.links,
        download_directory=DOWNLOAD_DIR,
        timeout=user_options.timeout,
    ).dowload_images()

    # if user_options.create_pdf:
    #     print_title('PDF')
    #     CreatePDF.create_pdf(DOWNLOAD_DIR, user_options.links)

    # if user_options.clean_img:
    #     print_title('DELETE IMAGES')
    #     DeleteIMG.delete_jpg(DOWNLOAD_DIR, user_options.links)


if __name__ == "__main__":
    main()
    pause()
