from enum import Enum, auto


class Alignment(Enum):
    CENTER = auto()
    LEFT = auto()
    RIGHT = auto()


ALIGNMENT_MAP: dict[Alignment, str] = {
    Alignment.CENTER: '^',
    Alignment.LEFT: '<',
    Alignment.RIGHT: '>',
}

def alignment_as_str(alignment: Alignment) -> str:
    return ALIGNMENT_MAP.get(alignment, ALIGNMENT_MAP[Alignment.CENTER])