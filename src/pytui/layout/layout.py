from itertools import zip_longest
from typing import TypeVar

from ..core import Alignment, Text
# from ..widget import Widget

T = TypeVar("T")

class Layout:
    """Expected to be inherited by a customized Layout."""

    def __init__(self) -> None:
        self._alignment: Alignment = Alignment.CENTER
        self._padding: int = 0
        self._items = []
        self._height: int = 0
        self.display_headers: bool = False

    def add(self, widget) -> None:
        self._items.append(widget)
        self._height = max(self._height, widget._height)

    def width(self) -> int:
        return max(r.width() for r in self._items)

    def padding(self) -> int:
        return max(r.padding() for r in self._items)

    def collect_rows(self) -> list[list[Text]]:
        rows = (w.items_as_rows() for w in self._items)
        widths: list[int] = [t.width() for t in self._items]
        collection = []

        _fill = [Text("")]

        for row in zip_longest(*rows, fillvalue=_fill):
            items = []
            for cols, width in zip(row, widths):
                for col in cols:
                    items.append(col)
            collection.append(items)

        return collection
