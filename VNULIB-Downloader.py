"""VNULIB Downloader"""

from src.utils.utils import pause
from src.utils.printIntro import printIntro


def main() -> None:
    """Main function

    Params:
        - None

    Returns:
        - None
    """
    printIntro()

    pause()


if __name__ == '__main__':
    main()
