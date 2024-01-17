from os import get_terminal_size


def SYSTEM_PAUSE() -> None:
    """Pause the system

    Params:
        - None

    Returns:
        - None
    """
    _ = input("Press Enter to continue . . .")


TERMINAL_SIZE_COLUMNS: int = get_terminal_size().columns
