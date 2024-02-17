"""Download book's images"""


from .link_parse import LinkFile, Link


class DownloadImages:
    """Download book's images

    Args:
        - links (list[Link]): The list of links object
    """

    def __init__(self, links: list[Link]) -> None:
        self.links = links
