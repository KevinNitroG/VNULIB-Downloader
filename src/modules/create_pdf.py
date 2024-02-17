"""Merge the images of books into PDF files
"""


from .link_parse import LinkFile, Link


class CreatePDF:
    """Merge the images of books into PDF files

    Args:
        - links (list[Link]): The list of links object
    """

    def __init__(self, links: list[Link]) -> None:
        self.links = links
