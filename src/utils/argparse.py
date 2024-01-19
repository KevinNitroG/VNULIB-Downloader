from argparse import ArgumentParser, Namespace

from ..utils.printColor import printInfo


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
                    default=False, help='Log the process to logs folder')
parser.add_argument('--log-level', '-ll', type=str, default='',
                    help='Options: DEBUG, INFO, WARNING, ERROR, CRITICAL (Default: INFO)')

args: Namespace = parser.parse_args()


def argParse() -> Namespace:
    """Parse the arguments

    Params:
        - None

    Returns:
        - None
    """
    if args.log_level and not args.log:
        parser.error(message='--log-level requires --log to be set.')
    if args.log and not args.log_level:
        args.log_level = 'INFO'
        printInfo(
            message=f'--log is set. But --log-level is not set. Therefore --log-level is set to Default: {args.log_level}')
    if args.log and args.log_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        parser.error(
            message=f'Invalid log level "{args.log_level}". Options: DEBUG, INFO, WARNING, ERROR, CRITICAL')
    return args
