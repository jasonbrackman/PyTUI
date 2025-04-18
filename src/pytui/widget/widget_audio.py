from typing import Generator, Any

from ..core import Colour, Text
from ..widget import Widget


class WidgetAudio(Widget):
    def colour_choice(self, index: int) -> Colour:
        total = len(self._items)
        if index > total / 1.3:
            return Colour.GREEN
        if index > total / 1.8:
            return Colour.YELLOW
        return Colour.RED

    def items_as_rows(self) -> Generator[list[list[Text]], Any, None]:

        for idx, s in enumerate(self._items):
            txt = Text(s)
            txt.width = self._width
            txt.padding = self._padding
            txt.align = self.alignment()
            txt.colour = self.colour_choice(idx)
            yield [txt]
