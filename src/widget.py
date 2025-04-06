from typing import Generic, Optional, Iterator, TypeVar

from src.alignment import Alignment, alignment_as_str

T = TypeVar('T')

class Widget(Generic[T]):
    def __init__(self, items: Optional[list[T]] = None, alignment: Alignment = Alignment.LEFT,
                 padding: int = 0) -> None:

        self._alignment = alignment
        self._padding = padding
        self._width: int = 0
        self._width_max: int = 20
        self._width_min: int = 0

        self._items: list[T] = []
        if items:
            self.extend(items)

        # self._header: Optional[T] = None

    def add(self, val: T) -> None:
        max_len = len(str(val))
        if max_len > self._width:
            self._width = max_len
        self._items.append(val)

    def extend(self, vals: list[T]) -> None:
        max_len = max(len(str(v)) for v in vals)
        if max_len > self._width:
            self._width = max_len
        self._items.extend(vals)

    def alignment(self):
        return self._alignment

    def display_items(self) -> Iterator[str]:
        """
        An iterator that returns the items at the max length specified.

        If the items collectively have a mixed sized, but all fall within the min-max
        range, they will display at the max size of any one of the entries.
        """
        yield from (str(t)[:self.width()] for t in self._items)

    def width(self) -> int:
        """
        Returns width of the longest item as long as width_min < len(item) < width_max.
        Else the width returned is:
         - the width_min if less than the item width, or
         - the width_max if greater.
        """

        if self._width_max < self._width:
            return self._width_max
        if self._width_min > self._width:
            return self._width_min
        return self._width

    def padding(self) -> int:
        return self._padding

    def render_lines(self) -> list[str]:
        align = alignment_as_str(self.alignment())
        width = self.width()
        pad = self.padding()
        return [f"{str(item):{align}{width + pad}}" for item in self.display_items()]
