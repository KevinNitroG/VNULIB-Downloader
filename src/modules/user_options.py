"""Setup user input, priority: argparse > config file > user input"""


from argparse import Namespace
from yaml import safe_load
from src.utils.logger import logger
from src.constants import USER_INPUT_YES, USER_INPUT_NO


class UserOptions:
    """Setup user input

    Params:
        - argparse (Namespace): Argpare
        - config_file (str): Config file path
    """

    def __init__(self, argparse: Namespace, config_file: str) -> None:
        self.argparse: Namespace = argparse
        with open(config_file, 'r', encoding='utf-8') as config:
            self.config = safe_load(config)
        self.user_options: dict[str, list[str] | str | bool] = {
            'username': '',
            'password': '',
            'links': [],
            'browser': '',
            'headless': False,
            'create_pdf': True,
            'clean_imgs': False,
        }

    def setup(self) -> dict[str, list[str] | str | bool]:
        """Setup user options"""
        self.user_options['username'] = self.setup_username()
        self.user_options['password'] = self.setup_password()
        self.user_options['links'] = self.setup_links()
        self.user_options['browser'] = self.setup_browser().lower()
        self.user_options['headless'] = self.setup_headless()
        self.user_options['create_pdf'] = self.setup_create_pdf()
        self.user_options['clean_imgs'] = self.setup_clean_imgs()
        self.log_the_variables()
        return self.user_options

    def log_the_variables(self) -> None:
        """Log the variable to log file"""
        logger.debug(msg=f'Username: {self.user_options['username']}')
        logger.debug(msg=f'Links: {self.user_options['links']}')
        logger.debug(msg=f'Browser: {self.user_options['browser']}')
        logger.debug(msg=f'Headless: {self.user_options['headless']}')
        logger.debug(msg=f'Create PDF: {self.user_options['create_pdf']}')
        logger.debug(msg=f'Clean images: {self.user_options['clean_imgs']}')

    def setup_username(self) -> str:
        """Setup username"""
        if self.argparse.username is not None:
            self.log_set_by_argparse('username')
            return self.argparse.username
        if self.config['USERNAME'] is not None:
            self.log_set_by_config('username')
            return str(self.config['USERNAME'])
        self.log_set_by_user_input('username')
        return input('Enter your VNULIB username: ').strip()

    def setup_password(self) -> str:
        """Setup password"""
        if self.argparse.password is not None:
            self.log_set_by_argparse('password')
            return self.argparse.password
        if self.config['PASSWORD'] is not None:
            self.log_set_by_config('password')
            return str(self.config['PASSWORD'])
        self.log_set_by_user_input('password')
        return input('Enter your VNULIB password: ').strip()

    def setup_links(self) -> list[str]:
        """Setup links"""
        if self.argparse.links is not None:
            self.log_set_by_argparse('links')
            return self.argparse.links
        if self.config['LINKS'] is not None:
            self.log_set_by_config('links')
            return self.config['LINKS']
        self.log_set_by_user_input('links')
        return list(
            input('Enter link(s), separate by space: ').strip().split(' '))

    def setup_browser(self) -> str:
        """Setup browser"""
        if self.argparse.browser is not None:
            self.log_set_by_argparse('browser')
            return self.argparse.browser
        if self.config['BROWSER'] is not None:
            self.log_set_by_config('browser')
            return self.config['BROWSER']
        self.log_set_by_user_input('browser')
        return input('Enter browser you are using'
                     '(chrome, chromium, brave, edge, firefox, IE, opera, local (chromedriver only)): ').strip()

    def setup_headless(self) -> bool:
        """Setup headless mode"""
        if self.argparse.headless is not None:
            self.log_set_by_argparse('headless')
            return self.argparse.headless
        if self.config['HEADLESS'] is not None:
            self.log_set_by_config('headless')
            return self.config['HEADLESS']
        self.log_set_by_user_input('headless')
        return input('Open the browser in headless mode'
                     '(no GUI) [Y/n]: ').strip().upper() in USER_INPUT_YES

    def setup_create_pdf(self) -> bool:
        """Setup links"""
        if self.argparse.create_pdf is not None:
            self.log_set_by_argparse('create_pdf')
            return self.argparse.create_pdf
        if self.config['CREATE_PDF'] is not None:
            self.log_set_by_config('create_pdf')
            return self.config['CREATE_PDF']
        self.log_set_by_user_input('create_pdf')
        return input('Create PDF of book(s)'
                     'after being downloaded [Y/n]: ').strip().upper() in USER_INPUT_YES

    def setup_clean_imgs(self) -> bool:
        """Setup clean images"""
        if self.argparse.clean_imgs is not None:
            self.log_set_by_argparse('clean_imgs')
            return self.argparse.create_pdf
        if self.config['CLEAN_IMGS'] is not None:
            self.log_set_by_config('clean_imgs')
            return self.config['CLEAN_IMGS']
        self.log_set_by_user_input('clean_imgs')
        return input('Create images of book(s)'
                     'after being merged into PDF [y/N]: ').strip().upper() in USER_INPUT_NO

    @staticmethod
    def log_set_by_argparse(var: str) -> None:
        """Log variable set by argparse

        Params:
            - var (str): Variable name

        Returns:
            - None
        """
        logger.info(msg=f'Variable: {var} - Set by argparse')

    @staticmethod
    def log_set_by_config(var: str) -> None:
        """Log variable set by config file

        Params:
            - var (str): Variable name

        Returns:
            - None
        """
        logger.info(msg=f'Variable: {var} - Set by config file')

    @staticmethod
    def log_set_by_user_input(var: str) -> None:
        """Log variable retrieved from user input

        Params:
            - var (str): Variable name

        Returns:
            - None
        """
        logger.info(msg=f'Variable: {var}'
                    ' - Retrieve from user input')
