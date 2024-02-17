"""Argparse for VNULIB-Downloader"""


from argparse import ArgumentParser, Namespace


def setup_argparse() -> Namespace:
    """Parse the arguments

    Returns:
        - Namespace: The parsed arguments
    """
    parser = ArgumentParser()
    parser.add_argument('--username', '-u', type=str,
                        help='Your VNULIB username')
    parser.add_argument('--password', '-p', type=str,
                        help='Your VNULIB password')
    parser.add_argument('--link', type=str, nargs='*',
                        help='Links of the book(s) to be downloaded')
    parser.add_argument('--browser', '-b',
                        default=None, help='Browser you are using, to use the correct webdriver'
                        ' (chrome, firefox, edge, safari, opera, ie)'
                        ' \'local\' to use local \'webdriver\' in the same directory')
    parser.add_argument('--headless', '-hl', action='store_true',
                        default=None, help='Open the browser in headless mode (no GUI)')
    parser.add_argument('--create-pdf', '-pdf', action='store_true',
                        default=None, help='Merge images to a PDF')
    parser.add_argument('--clean-imgs', '-c', action='store_true',
                        default=None, help='Delete images after merging to PDF')
    # skipcq: PY-W0069
    # parser.add_argument('--update', '-u', action='store_true',
    # skipcq: PY-W0069
    #                     default=False, help='Update the tool from Repository')
    args: Namespace = parser.parse_args()
    return args
