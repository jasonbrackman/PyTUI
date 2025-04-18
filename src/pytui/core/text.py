from dataclasses import dataclass

from pytui.core.alignment import Alignment, alignment_as_str
from pytui.core.colour import Colour, strip_ansi


@dataclass
class Text:
    def __init__(self, s: str, colour: Colour = Colour.DEFAULT_FG) -> None:
        self._ori = s
        self._raw = strip_ansi(s)
        self._raw_len: int = len(self._raw)

        # --
        self._col = colour

        # --
        self._align: Alignment = Alignment.CENTER
        self._width = self._raw_len
        self._pad: int = 0

    def paint(self, s: str) -> str:
        if self._col == Colour.DEFAULT_FG:
            return s
        return f"\033[{self._col}m{s}\033[0m"

    @property
    def colour(self) -> Colour:
        return self._col

    @colour.setter
    def colour(self, colour: Colour) -> None:
        self._col = colour

    @property
    def align(self) -> Alignment:
        return self._align

    @align.setter
    def align(self, align: Alignment) -> None:
        self._align = align

    @property
    def padding(self) -> int:
        return self._pad

    @padding.setter
    def padding(self, pad: int) -> None:
        self._pad = pad

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self._width = width

    def __len__(self):
        return len(self._raw)

    def __str__(self):
        r = 0 if self._col == Colour.DEFAULT_FG else 9
        a = alignment_as_str(self.align)
        p = self.paint(self._raw[: self.width])
        return f"{' ' * self.padding}{p:{a}{self.width + r}}{' ' * self.padding}"

    def __repr__(self):
        return f'Text("{self._raw}")'
