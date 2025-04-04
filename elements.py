from enum import Enum, auto
from itertools import zip_longest
from typing import TypeVar, Generic, Optional, Union, Iterator

from constants import (
    UPPER_CORNER_LEFT, HLINE, UPPER_CORNER_RIGHT, VLINE, JUNCTION_LEFT, LOWER_CORNER_RIGHT,
    JUNCTION_RIGHT, LOWER_CORNER_LEFT,
)

T = TypeVar('T')


class Alignment(Enum):
    CENTER = auto()
    LEFT = auto()
    RIGHT = auto()


class Widget(Generic[T]):
    def __init__(self, items: Optional[list[T]] = None, alignment: Alignment = Alignment.LEFT,
                 padding: int = 0) -> None:

        self._alignment = alignment
        self._padding = padding
        self._width: int = 0

        self._items: list[T] = []
        if items:
            self.extend(items)

        self._header: Optional[T] = None

    def add(self, val: T) -> None:
        max_len = len(val)
        if max_len > self._width:
            self._width = len(val)
        self._items.append(val)

    def extend(self, vals: list[T]) -> None:
        max_len = max(len(v) for v in vals)
        if max_len > self._width:
            self._width = max_len
        self._items.extend(vals)

    def alignment(self):
        return self._alignment

    def items(self) -> list[T]:
        return self._items

    def width(self) -> int:
        return self._width

    def padding(self) -> int:
        return self._padding


class LayoutImpl:
    """Expected to be inherited by a customized Layout."""

    def __init__(self):
        self._alignment: Alignment = Alignment.CENTER
        self._padding: int = 0
        self._items: list[Union[LayoutImpl, Widget]] = []

    def add(self, widget: Widget) -> None:
        self._items.append(widget)

    def _alignment_as_str(self, alignment: Alignment) -> str:
        if alignment == Alignment.LEFT:
            return '<'
        if alignment == Alignment.RIGHT:
            return '>'
        if alignment == Alignment.CENTER:
            return '^'

    def collect_coloumn_data(self) -> tuple[
        Iterator[list[T]], list[int], list[Alignment], list[int]]:
        content = (w.items() for w in self._items)
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
            rows.append(f'{s:{self._alignment_as_str(self._alignment)}{self._padding + len(s)}}')

        return rows

    def render(self, fill: str = '') -> None:
        raise NotImplementedError()

    def _render_row(self, widgets: list[Widget], fill: str = "|") -> str:
        formatted = []
        for w in widgets:

            align = self._alignment_as_str(w.alignment())
            width = w.width()
            padd = w.padding()

            for item in w.items():
                s = f"{item:{align}{width + padd}}"
                formatted.append(s)

        s = VLINE.join(formatted)
        return f"{s}"

    def _stylized_row(self, aligns: list[Alignment], pads: list[int], widths: list[int],
                      row: list[str], fill: str = VLINE) -> str:
        s = f'{fill}'.join(
            [f"{item:{self._alignment_as_str(align)}{width + pad}}"
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

        content = [w.items()[::] for w in self._items]
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
            if isinstance(item, TableLayout):
                rows = item.collect_rows()
                max_width = max(len(rows[0]), max_width)
                if item.display_headers:
                    collection[count] = rows[:1]
                    count += 1
                    collection[count] = rows[1:]
                else:
                    collection[count] = rows
            if isinstance(item, Window):
                rows = item.collect_rows()
                max_width = max(len(rows[0]), max_width)
                collection[count] = rows
            elif isinstance(item, Widget):
                s = self._render_row([item])
                max_width = max(len(s), max_width)
                collection[count] = [s]
            count += 1
        # get longest row

        print(UPPER_CORNER_LEFT + (HLINE * max_width) + UPPER_CORNER_RIGHT)
        for k, rows in collection.items():
            for row in rows:
                print(f"{VLINE}{row:^{max_width}}{VLINE}")
            if k < len(collection) - 1:
                print(f"{JUNCTION_RIGHT}{HLINE * max_width}{JUNCTION_LEFT}")
        print(f"{LOWER_CORNER_LEFT}{HLINE * max_width}{LOWER_CORNER_RIGHT}")
