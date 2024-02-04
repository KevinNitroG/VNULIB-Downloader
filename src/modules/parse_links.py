"""Parse links from book website -> book page link"""


from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from re import compile as re_compile, search as re_search

from urllib.parse import urlparse, urlunparse, parse_qs, urlencode


class ParseLinks:
    """Parse links from book website -> book page link

    Params:
        - links (list[str]): List of links to parse

    Returns:
        - list[dict]: List of dictionary contain parsed links' information
    """

    def __init__(self, links) -> None:
        self.links: list[str] = links
        self.pattern_book = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/handle/VNUHCM/\d+')
        self.pattern_preview = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/simple_document\.php\?subfolder=.+&doc=\d+&bitsid=.+')
        self.pattern_page = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/services/view\.php\?.+(page=\d+).+')

    def parse(self) -> list[dict]:
        """Parse the links"""
        parsed_links: list[dict] = []
        for link in self.links:
            dict_link = {}
            if re_search(self.pattern_page, link):
                dict_link.update({'original_link': link})
                dict_link.update({'original_type': 'page'})
                dict_link.update({'link': self.parse_page_link(link)})
                dict_link.update({'page_number': -1})
            elif re_search(self.pattern_preview, link):
                pass
            elif re_search(self.pattern_book, link):
                pass
            parsed_links.append(dict_link)
        return parsed_links

    @staticmethod
    def parse_page_link(link):
        """Remove the page query parameter from the link

        Params:
            - link (str): Link to parse

        Returns:
            - str: Parsed link (page query parameter move to the end)"""
        link_parts = urlparse(link)
        query_params = parse_qs(link_parts.query)
        query_params.pop('page', None)
        new_query_string = urlencode(query_params, doseq=True)
        parsed_link = urlunparse(
            (link_parts.scheme, link_parts.netloc, link_parts.path, link_parts.params, new_query_string, link_parts.fragment)) + '&page='
        return parsed_link
