"""VNULIB Downloader"""

from src.utils import SYSTEM_PAUSE
from src.utils.printIntro import printIntro


def main() -> None:
    """Main function

    Params:
        - None

    Returns:
        - None
    """
    printIntro()
    SYSTEM_PAUSE()


if __name__ == '__main__':
    main()
