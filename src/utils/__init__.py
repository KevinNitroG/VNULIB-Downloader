from os import get_terminal_size, system


def SYSTEM_PAUSE() -> None:
    """Pause the system

    Params:
        - None

    Returns:
        - None
    """
    system('pause')


TERMINAL_SIZE_COLUMNS: int = get_terminal_size().columns
