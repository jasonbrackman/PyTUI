from dataclasses import dataclass, field
from itertools import zip_longest
from typing import TypeVar, Iterator

from src.alignment import Alignment, alignment_as_str
from src.constants import (
    UPPER_CORNER_LEFT, HLINE, UPPER_CORNER_RIGHT, VLINE, JUNCTION_LEFT, LOWER_CORNER_RIGHT,
    JUNCTION_RIGHT, LOWER_CORNER_LEFT,
)
from src.widget import Widget

T = TypeVar('T')


@dataclass
class Style:
    alignment: Alignment = field(default=Alignment.LEFT)
    padding: int = field(default=0)

class LayoutImpl:
    """Expected to be inherited by a customized Layout."""

    def __init__(self) -> None:
        self._alignment: Alignment = Alignment.CENTER
        self._padding: int = 0
        self._items: list[LayoutImpl | Widget] = []

    def add(self, widget: Widget) -> None:
        self._items.append(widget)

    def collect_coloumn_data(self) -> tuple[
        Iterator[list[T]], list[int], list[Alignment], list[int]]:
        content = (w.display_items() for w in self._items)
        widths = [w.width() for w in self._items]
        aligns = [w.alignment() for w in self._items]
        pads = [w.padding() for w in self._items]

        return content, widths, aligns, pads

    def collect_rows(self) -> list[str]:
        content, widths, aligns, pads = self.collect_coloumn_data()
        rows = []
        _fill = VLINE
        for row in zip_longest(*content, fillvalue=''):
            s = self._stylized_row(aligns, pads, widths, row, fill=_fill)
            rows.append(f'{s:{alignment_as_str(self._alignment)}{self._padding + len(s)}}')

        return rows

    def render_lines(self) -> list[str]:
        return self.collect_rows()


    def render(self, fill: str = '') -> None:
        count = 0
        collection = {}
        max_width = 0
        for item in self._items:
            rows = item.render_lines()
            collection[count] = rows
            for row in rows:
                max_width = max(max_width, len(row))
            count += 1

        print(UPPER_CORNER_LEFT + (HLINE * max_width) + UPPER_CORNER_RIGHT)
        for k, rows in collection.items():
            for row in rows:
                row = row.rstrip()
                row += ' ' * (max_width - len(row))
                print(f"{VLINE}{row}{VLINE}")
            if k < len(collection) - 1:
                print(f"{JUNCTION_RIGHT}{HLINE * max_width}{JUNCTION_LEFT}")
        print(f"{LOWER_CORNER_LEFT}{HLINE * max_width}{LOWER_CORNER_RIGHT}")

    def _render_rows(self, widgets: list[Widget]) -> str:
        formatted = []
        for w in widgets:
            align = alignment_as_str(w.alignment())
            width = w.width()
            padd = w.padding()

            for item in w.display_items():
                s = f"{item[:width]:{align}{width + padd}}"
                formatted.append(s)

        s = VLINE.join(formatted)
        return f"{s}"

    def _stylized_row(self, aligns: list[Alignment], pads: list[int], widths: list[int],
                      row: list[str], fill: str = VLINE) -> str:
        s = f'{fill}'.join(
            [f"{item:{alignment_as_str(align)}{width + pad}}"
             for align, pad, width, item in zip(aligns, pads, widths, row)]
        )

        return s

class TableLayout(LayoutImpl):
    def __init__(self):
        super().__init__()
        self._headers: list[T] = []
        self.display_headers = True

    def add_coloumn(self, widget: Widget, header: T) -> None:
        self.add(widget)
        self._headers.append(header)

    def collect_coloumn_data(self) -> tuple[
        Iterator[list[T]], list[int], list[Alignment], list[int]]:

        content = [list(w.display_items()) for w in self._items]
        widths = [w.width() for w in self._items]
        aligns = [w.alignment() for w in self._items]
        pads = [w.padding() for w in self._items]

        if self.display_headers:
            for idx, item in enumerate(self._headers):
                content[idx].insert(0, item)
                widths[idx] = max(len(item), widths[idx])

        return content, widths, aligns, pads


class Window(LayoutImpl):
    def render(self, fill: str = '') -> None:
        count = 0
        collection = {}
        max_width = 0

        for item in self._items:
            rows = item.render_lines()
            collection[count] = rows
            for row in rows:
                max_width = max(max_width, len(row))
            count += 1

        # -------- Actual Rendering -----
        print(UPPER_CORNER_LEFT + (HLINE * max_width) + UPPER_CORNER_RIGHT)

        for k, rows in collection.items():
            for row in rows:
                row_aligned = f"{row:^{max_width}}"
                print(f"{VLINE}{row_aligned}{VLINE}")
            if k < len(collection) - 1:
                print(f"{JUNCTION_RIGHT}{HLINE * max_width}{JUNCTION_LEFT}")

        print(f"{LOWER_CORNER_LEFT}{HLINE * max_width}{LOWER_CORNER_RIGHT}")
