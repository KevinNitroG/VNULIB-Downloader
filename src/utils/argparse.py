from argparse import ArgumentParser, Namespace


parser = ArgumentParser()
parser.add_argument('--links', type=list, nargs='+',
                    help='Links of the book(s) to be downloaded')
parser.add_argument('--overwrite-book', '-o', action='store_true', default=None,
                    help='If the folder of images / PDF file of the book is already exist, then overwrite it')
parser.add_argument('--create-pdf', '-pdf', action='store_true',
                    default=None, help='Merge images to a PDF')
parser.add_argument('--keep-imgs', '-k', action='store_true',
                    default=None, help='Keep images after merging to PDF')
parser.add_argument('--log', '-l', action='store_true',
                    default=False, help='Log the processed books information to logs folder')

args: Namespace = parser.parse_args()


def argParse() -> Namespace:
    """Parse the arguments

    Params:
        - None

    Returns:
        - None
    """
    return args
