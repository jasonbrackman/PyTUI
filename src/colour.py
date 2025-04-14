from enum import IntEnum
import re


class Colour(IntEnum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

    BLACK_L = 90
    RED_L = 91
    GREEN_L = 92
    CYAN_L = 96
    WHITE_L = 97

    DEFAULT_FG = 39
    DEFAULT_BG = 49


def colourize(text: str, colour: Colour) -> str:
    return f"\033[{colour}m{text}\033[0m"


def strip_ansi(text):
    ansi_escape = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)
