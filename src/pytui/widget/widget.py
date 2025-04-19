from typing import Generic, Optional, TypeVar, Any, Generator

from ..core import Alignment, Colour, Text

T = TypeVar("T")


class Widget(Generic[T]):
    def __init__(
        self,
        items: Optional[list[T]] = None,
        alignment: Alignment = Alignment.LEFT,
        padding: int = 0,
    ) -> None:

        self._alignment = alignment
        self._colour = Colour.CYAN
        self._height = 0
        self._padding = padding

        self._width: int = 0
        self._width_max: int = 20
        self._width_min: int = 0

        self._items: list[T] = []
        if items:
            self.extend(items)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items: list[T]) -> None:
        self._items = items
        self._width = max((len(str(m)) for m in self._items))
        self._height = len(items)

    def items_as_rows(self) -> Generator[list[list[Text]], Any, None]:
        """
        An iterator that returns the items at the max length specified.

        If the items collectively have a mixed sized, but all fall within the min-max
        range, they will display at the max size of any one of the entries.
        """
        for s in self._items:
            txt = Text(str(s))
            txt.width = self._width
            txt.padding = self._padding
            txt.align = self._alignment
            yield ([txt])

    def add(self, val: T) -> None:
        max_len = len(str(val))
        if max_len > self._width:
            self._width = max_len
        self._items.append(val)
        self._height += 1

    def extend(self, vals: list[T]) -> None:
        new_len = max(len(str(v)) for v in vals)
        if new_len > self._width:
            self._width = new_len
        self._items.extend(vals)
        self._height += len(vals)

    def alignment(self):
        return self._alignment

    def width(self) -> int:
        """
        Returns width of the longest item as long as width_min < len(item) < width_max.
        Else the width returned is:
         - the width_min if less than the item width, or
         - the width_max if greater.
        """
        if self._width_max < self._width:
            return self._width_max  # + self._padding
        if self._width_min > self._width:
            return self._width_min  # + self._padding
        return self._width  #  + self._padding

    def padding(self) -> int:
        return self._padding
