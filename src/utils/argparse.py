from argparse import ArgumentParser, Namespace


parser = ArgumentParser()
parser.add_argument('links', type=list, nargs='+', required=True,
                    help='Links of the book(s) to be downloaded')
parser.add_argument('--overwrite-book', '-o', action='store_true', default=None,
                    help='If the folder of images / PDF file of the book is already exist, then overwrite it')
parser.add_argument('--create-pdf', '-pdf', action='store_true',
                    default=None, help='Merge images to a PDF')
parser.add_argument('--keep-imgs', '-k', action='store_true',
                    default=None, help='Keep images after merging to PDF')
parser.add_argument('--log', '-l', action='store_true',
                    default=False, help='Log the process')
parser.add_argument('--log-level', '-ll', type=str, default='INFO',
                    help='Log level\nOptions: DEBUG, INFO, WARNING, ERROR, CRITICAL\nDefault: INFO')

args: Namespace = parser.parse_args()


def argParse() -> Namespace:
    """Parse the arguments

    Params:
        - None

    Returns:
        - None
    """

    # global LINKS, OVERWRITE_BOOK, CREATE_PDF, KEEP_IMGS, LOG, LOG_LEVEL
    # LINKS: list[str] = args.links
    # OVERWRITE_BOOK: bool = args.overwrite_book
    # CREATE_PDF: bool = args.create_pdf
    # KEEP_IMGS: bool = args.keep_imgs
    # LOG: bool = args.log
    # LOG_LEVEL: str = args.log_level.upper()

    if args.log_level and not args.log:
        parser.error(message="--log-level requires --log to be set.")

    if args.log_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        parser.error(
            message=f'Invalid log level "{args.log_level}". Options: DEBUG, INFO, WARNING, ERROR, CRITICAL')

    return args
