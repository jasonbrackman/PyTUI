from typing import Iterator

from src.alignment import Alignment
from src.layout import LayoutImpl, T
from src.widget import Widget


class TableLayout(LayoutImpl):
    def __init__(self) -> None:
        super().__init__()
        self._headers: list[str] = []
        self.display_headers = True

    def add_coloumn(self, widget: Widget, header: str = "") -> None:
        widget._width_min = max(widget._width_min, len(header))
        self.add(widget)
        self._headers.append(header)

    def collect_header_data(self) -> tuple[Iterator[list[T]], list[int], list[Alignment], list[int]]:
        content = ([h] for h in self._headers)
        widths = [w.width() for w in self._items]
        aligns = [w.alignment() for w in self._items]
        pads = [w.padding() for w in self._items]

        return content, widths, aligns, pads

    def collect_coloumn_data(self) -> tuple[Iterator[list[T]], list[int], list[Alignment], list[int]]:

        content = (w.display_items() for w in self._items)
        widths = [w.width() for w in self._items]
        aligns = [w.alignment() for w in self._items]
        pads = [w.padding() for w in self._items]

        return content, widths, aligns, pads

    def render_headers(self) -> list[str]:
        content, widths, aligns, pads = self.collect_header_data()
        return self.collect_rows(content, widths, aligns, pads)