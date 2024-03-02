"""Setup user input, priority: argparse > config file > user input"""

from __future__ import annotations

from argparse import Namespace
from dataclasses import dataclass
from pprint import pformat
from yaml import safe_load
from ..constants import CONFIG_FILE, USER_INPUT_NO, USER_INPUT_YES
from ..utils import logger
from .argpase import setup_argparse


@dataclass(slots=True)
class LinkFile:
    """Dataclass to store book file's information

    Args:
        - page_link (str): Page link
        - num_pages (int): Number of pages
        - name (str): Name of the file. If original link is preview link, it will be datetime format
    """

    page_link: str = ""
    num_pages: int = -1
    name: str = ""


@dataclass(slots=True)
class Link:
    """Dataclass to store links' information

    Args:
        - original_link (str): Original link
        - original_type (str): Original type of the link
        - files (list[LinkFile]): List of book files from the book
        - name (str): Name of the book. If preview / page link, it will be ''
    """

    original_link: str
    original_type: str
    files: list[LinkFile]
    name: str = ""


class UserOptions:  # pylint: disable=too-many-instance-attributes
    """Setup user input"""

    def __init__(self) -> None:
        self.argparse: Namespace = setup_argparse()
        with open(CONFIG_FILE, encoding="utf-8") as config:
            self.config = safe_load(config)
        self.username: str = ""
        self.password: str = ""
        self.links: list[Link] = []
        self.timeout: int = 0
        self.browser: str = ""
        self.headless: bool = False
        self.create_pdf: bool = True
        self.clean_img: bool = True
        # Just pre-set the variables, not really matter

    def setup(self) -> None:
        """Setup user options"""
        self.username = self.__setup_username()
        self.password = self.__setup_password()
        self.links = self.__setup_links()
        self.timeout = self.__setup_timeout()
        self.browser = self.__setup_browser().lower()
        self.headless = self.__setup_headless()
        self.create_pdf = self.__setup_create_pdf()
        self.clean_img = self.__setup_clean_img()
        self.__log_the_variables()
        logger.info(msg="User options setup completed")

    def __log_the_variables(self) -> None:
        """Log the variable to log file"""
        logger.debug(msg=f"User options:\n{self}")

    def __str__(self) -> str:
        """For debug printing purpose

        Returns:
            str: object information
        """
        debug_object = {
            "username": self.username,
            "timeout": self.timeout,
            "browser": self.browser,
            "headless": self.headless,
            "create_pdf": self.create_pdf,
            "clean_img": self.clean_img,
        }
        return "User options:\n" f"{pformat(debug_object)}"

    def __setup_username(self) -> str:
        """Setup username

        Returns:
            - str: Username
        """
        if self.argparse.username is not None:
            self.__log_set_by_argparse("username")
            return self.argparse.username
        if self.config["USERNAME"] is not None:
            self.__log_set_by_config("username")
            return str(self.config["USERNAME"])
        self.__log_set_by_user_input("username")
        return input("Enter your VNULIB username: ").strip()

    def __setup_password(self) -> str:
        """Setup password

        Returns:
            - str: Password
        """
        if self.argparse.password is not None:
            self.__log_set_by_argparse("password")
            return self.argparse.password
        if self.config["PASSWORD"] is not None:
            self.__log_set_by_config("password")
            return str(self.config["PASSWORD"])
        self.__log_set_by_user_input("password")
        return input("Enter your VNULIB password: ").strip()

    def __setup_links(self) -> list[Link]:
        """Setup links

        Returns:
            - list[Link]: List of links object
        """
        if self.argparse.link is not None:
            self.__log_set_by_argparse("links")
            return [
                Link(original_link=link, original_type="", files=[LinkFile()])
                for link in self.argparse.link
            ]
        if self.config["LINKS"] is not None:
            self.__log_set_by_config("links")
            return [
                Link(original_link=link, original_type="", files=[LinkFile()])
                for link in self.config["LINKS"]
            ]
        self.__log_set_by_user_input("links")
        return [
            Link(original_link=link, original_type="", files=[LinkFile()])
            for link in input("Enter link(s), separate by space: ").strip().split(" ")
        ]

    def __setup_timeout(self) -> int:
        """Setup timeout

        Returns:
            int: Timeout
        """
        if self.argparse.timeout is not None:
            self.__log_set_by_argparse("timeout")
            return int(self.argparse.browser)
        if self.config["TIMEOUT"] is not None:
            self.__log_set_by_config("timeout")
            return int(self.config["TIMEOUT"])
        user_timeout: str = input("Enter timeout for Selenium & request [20]").strip()
        if user_timeout == "":
            return 20
        return int(user_timeout)

    def __setup_browser(self) -> str:
        """Setup browser

        Returns:
            - str: Browser
        """
        if self.argparse.browser is not None:
            self.__log_set_by_argparse("browser")
            return self.argparse.browser
        if self.config["BROWSER"] is not None:
            self.__log_set_by_config("browser")
            return self.config["BROWSER"]
        self.__log_set_by_user_input("browser")
        return input(
            "Enter browser you are using [chrome, path/to/chrome_driver]: "
        ).strip()

    def __setup_headless(self) -> bool:
        """Setup headless mode

        Returns:
            - bool: Headless mode
        """
        if self.argparse.headless is not None:
            self.__log_set_by_argparse("headless")
            return self.argparse.headless
        if self.config["HEADLESS"] is not None:
            self.__log_set_by_config("headless")
            return self.config["HEADLESS"]
        self.__log_set_by_user_input("headless")
        return (
            input("Open the browser in headless mode [Y/n]: ").strip().upper()
            in USER_INPUT_YES
        )

    def __setup_create_pdf(self) -> bool:
        """Setup create pdf

        Returns:
            - bool: Create PDF
        """
        if self.argparse.create_pdf is not None:
            self.__log_set_by_argparse("create_pdf")
            return self.argparse.create_pdf
        if self.config["CREATE_PDF"] is not None:
            self.__log_set_by_config("create_pdf")
            return self.config["CREATE_PDF"]
        self.__log_set_by_user_input("create_pdf")
        return (
            input("Create PDF of book(s) after being downloaded [Y/n]: ")
            .strip()
            .upper()
            in USER_INPUT_YES
        )

    def __setup_clean_img(self) -> bool:
        """Setup clean images

        Returns:
            - bool: Clean images
        """
        if self.argparse.clean_img is not None:
            self.__log_set_by_argparse("clean_img")
            return self.argparse.clean_img
        if self.config["CLEAN_IMG"] is not None:
            self.__log_set_by_config("clean_img")
            return self.config["CLEAN_IMG"]
        self.__log_set_by_user_input("clean_img")
        return (
            input("Create images of book(s) after being merged into PDF [y/N]: ")
            .strip()
            .upper()
            in USER_INPUT_NO
        )

    @staticmethod
    def __log_set_by_argparse(var: str) -> None:
        """Log variable set by argparse

        Args:
            - var (str): Variable name
        """
        logger.debug(msg=f"Variable: {var} - Set by argparse")

    @staticmethod
    def __log_set_by_config(var: str) -> None:
        """Log variable set by config file

        Args:
            - var (str): Variable name
        """
        logger.debug(msg=f"Variable: {var} - Set by config file")

    @staticmethod
    def __log_set_by_user_input(var: str) -> None:
        """Log variable retrieved from user input

        Args:
            - var (str): Variable name
        """
        logger.debug(msg=f"Variable: {var}" " - Retrieve from user input")
