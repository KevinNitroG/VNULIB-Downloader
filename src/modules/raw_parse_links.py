"""Raw parse links to get the raw list of link information"""


from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from re import compile as re_compile, search as re_search


class RawParseLinks:
    """Raw parse links to get the raw list of link information

    Params:
        - links (list[str]): List of links to parse
    """

    def __init__(self, links) -> None:
        self.links: list[str] = links
        self.pattern_book = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/handle/VNUHCM/\d+')
        self.pattern_preview = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/simple_document\.php\?subfolder=.+&doc=\d+&bitsid=.+')
        self.pattern_page = re_compile(
            r'http[s]?://ir\.vnulib\.edu\.vn/flowpaper/services/view\.php\?.+(page=\d+).+')
        self.need_to_convert = False

    def parse(self) -> list[dict]:
        """Parse the links

        Returns:
        - list[dict]: List of dictionary contain parsed links' information
        """
        parsed_links: list[dict] = []
        for link in self.links:
            dict_link = {}
            dict_link.update({'original_link': link})
            if re_search(self.pattern_page, link):
                dict_link.update({'original_type': 'page'})
                dict_link.update({'link': self.parse_page_link(link)})
                dict_link.update({'page_number': -1})
            elif re_search(self.pattern_preview, link):
                dict_link.update({'original_type': 'preview'})
                self.need_to_convert = True
            elif re_search(self.pattern_book, link):
                dict_link.update({'original_type': 'book'})
                self.need_to_convert = True
            parsed_links.append(dict_link)
        return parsed_links

    @staticmethod
    def parse_page_link(link) -> str:
        """Remove the page query parameter from the link

        Params:
            - link (str): Link to parse

        Returns:
            - str: Parsed link (page query parameter removed)
        """
        link_parts = urlparse(link)
        query_params = parse_qs(link_parts.query)
        query_params.pop('page', None)
        new_query_string = urlencode(query_params, doseq=True)
        parsed_link: str = urlunparse(
            (link_parts.scheme, link_parts.netloc,
             link_parts.path, link_parts.params,
             new_query_string, link_parts.fragment))
        return parsed_link
