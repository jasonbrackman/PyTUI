from itertools import zip_longest, chain
from typing import Iterator, Any, Generator

from src.alignment import Alignment
from src.colour import Colour
from src.layout import LayoutImpl, T
from src.widget import Widget
from src.text import Text


class TableLayout(LayoutImpl):
    def __init__(self) -> None:
        super().__init__()
        self._headers: Widget = Widget([], alignment=Alignment.CENTER)
        self.display_headers = True

    def add_coloumn(self, widget: Widget, header: str = "") -> None:
        widget._width_min = max(widget._width_min, len(header))
        self.add(widget)
        self._headers.add(header)

    def items_as_rows(self) -> Generator[list[list[Text]], Any, None]:
        widths = [wid.width() for wid in self._items]
        header_rows = self._headers.items_as_rows()
        if header_rows:
            headers = list(chain.from_iterable(header_rows))
            for idx, col in enumerate(headers):
                #                         |-- Hack: Widget will take largest of
                #                         |         header list, instead of treating
                #                         v         each one as its own widget.
                col.width = widths[idx] = max(len(headers[idx]), widths[idx])
                col.colour = Colour.WHITE_L
            yield [headers]

        combined_rows = []
        # fill_ = Text("")
        items = [w.items_as_rows() for w in self._items]
        flattened = [list(chain.from_iterable(item)) for item in items]
        for flat in zip_longest(*flattened, fillvalue=None):
            final_list = list(flat)
            for idx, col in enumerate(final_list):
                if final_list[idx] is None:
                    final_list[idx] = Text("")
                    col = final_list[idx]
                col.width = widths[idx]

            combined_rows.append(final_list)
        yield combined_rows

    def width(self):
        return sum(r.width() for r in self._items) + len(self._items) - 1
