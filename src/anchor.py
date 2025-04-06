from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Anchor(Enum):
    TOP = auto()
    BOTTOM = auto()