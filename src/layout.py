from itertools import zip_longest
from typing import TypeVar, Iterator

from src.alignment import Alignment, alignment_as_str
from src.constants import VLINE
from src.widget import Widget

T = TypeVar('T')


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

    def collect_coloumn_data(self) -> tuple[
        Iterator[list[T]], list[int], list[Alignment], list[int]]:
        content = (w.display_items() for w in self._items)
        widths = [w.width() for w in self._items]
        aligns = [w.alignment() for w in self._items]
        pads = [w.padding() for w in self._items]

        return content, widths, aligns, pads

    def collect_rows(self, content, widths, aligns, pads) -> list[str]:

        rows = []
        _fill = VLINE
        for row in zip_longest(*content, fillvalue=''):
            s = self._stylized_row(aligns, pads, widths, row, fill=_fill)
            rows.append(f'{s:{alignment_as_str(self._alignment)}{self._padding + len(s)}}')

        return rows

    def render_lines(self) -> list[str]:
        content, widths, aligns, pads = self.collect_coloumn_data()
        return self.collect_rows(content, widths, aligns, pads)

    def _stylized_row(self, aligns: list[Alignment], pads: list[int], widths: list[int],
                      row: list[str], fill: str = VLINE) -> str:
        s = f'{fill}'.join(
            [f"{item[:width]:{alignment_as_str(align)}{width + pad}}"
             for align, pad, width, item in zip(aligns, pads, widths, row)]
        )

        return s

    def display_items(self) -> None:
        raise NotImplementedError
