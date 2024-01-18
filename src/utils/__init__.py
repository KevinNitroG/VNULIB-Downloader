from os import get_terminal_size


def pause() -> None:
    """Pause the system

    Params:
        - None

    Returns:
        - None
    """
    _: str = input("Press Enter to continue . . .")


TERMINAL_SIZE_COLUMNS: int = get_terminal_size().columns
