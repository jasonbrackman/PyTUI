from itertools import zip_longest
from typing import TypeVar, Iterator, Any, Generator

from src.alignment import Alignment, alignment_as_str
from src.constants import VLINE
from src.text import Text
from src.widget import Widget

T = TypeVar("T")


class LayoutImpl:
    """Expected to be inherited by a customized Layout."""

    def __init__(self) -> None:
        self._alignment: Alignment = Alignment.CENTER
        self._padding: int = 0
        self._items: list[LayoutImpl | Widget] = []
        self._height: int = 0
        self.display_headers: bool = False

    def add(self, widget: Widget) -> None:
        self._items.append(widget)
        self._height = max(self._height, widget._height)

    def width(self) -> int:
        return max(r.width() for r in self._items)

    def collect_rows(self) -> list[list[Text]]:
        rows = (w.items_as_rows() for w in self._items)
        widths: list[int] = [t.width() for t in self._items]
        collection = []

        _fill = [Text("")]

        for row in zip_longest(*rows, fillvalue=_fill):
            items = []
            for cols, width in zip(row, widths):
                # print(cols, type(cols))
                for col in cols:
                    # print(col)
                    # col.width = width
                    items.append(col)
            collection.append(items)

        return collection
