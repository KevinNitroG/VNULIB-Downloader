"""VNULIB Downloader"""


from src.modules import setup_argparse
from src.modules import PrintIntro, ToolConfig, UserOptions
from src.utils import print_title
from src.constants import CONFIG_FILE
from src.bot import Browser, Login


def main() -> None:
    """Main function to run VNULIB Downloader

    Params:
        - None

    Returns:
        - None
    """
    PrintIntro().print_intro()
    print_title(message='SETUP')
    ToolConfig(
        config_file_name='config.yml',
        url='https://raw.githubusercontent.com/KevinNitroG/VNULIB-Downloader/main/config-sample.yml'
    ).setup_config_file()
    user_options: dict[str, list[str] | str | bool] = UserOptions(
        argparse=setup_argparse(), config_file=CONFIG_FILE).setup()
    driver = Browser(user_options['browser'],
                     user_options['headless']).setup_browser()


if __name__ == '__main__':
    main()
