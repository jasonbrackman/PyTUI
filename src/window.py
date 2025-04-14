from src.colour import strip_ansi
from src.constants import (
    UPPER_CORNER_LEFT,
    HLINE,
    UPPER_CORNER_RIGHT,
    VLINE,
    JUNCTION_RIGHT,
    JUNCTION_LEFT,
    LOWER_CORNER_LEFT,
    LOWER_CORNER_RIGHT,
)
from src.layout import LayoutImpl


class Window(LayoutImpl):
    def render(self) -> None:
        count = 0
        collection = {}
        max_width = 0

        for item in self._items:
            for rows in item.items_as_rows():

                for row in rows:
                    if not row:
                        count += 1
                        continue
                    collection[count] = rows
                    max_width = max(max_width, self.width())
                    # print(max_width, self.width())
                count += 1

        # -------- Actual Rendering -----
        print(UPPER_CORNER_LEFT + (HLINE * max_width) + UPPER_CORNER_RIGHT)
        for k, rows in collection.items():
            for row in rows:
                try:
                    print(
                        f"{VLINE}{VLINE.join(str(r) for r in row):^{max_width}}{VLINE}"
                    )
                except TypeError as e:
                    print(
                        f"{VLINE}{VLINE.join(str(r) for r in rows):^{max_width}}{VLINE}"
                    )
            if k < len(collection) - 1:
                print(f"{JUNCTION_RIGHT}{HLINE * max_width}{JUNCTION_LEFT}")
        print(f"{LOWER_CORNER_LEFT}{HLINE * max_width}{LOWER_CORNER_RIGHT}")

    def render2(self):
        print("~" + ("=" * (self.width() + 3 - 1)) + "~")
        for item in self._items:
            for rows in item.items_as_rows():
                for row in rows:
                    if not row:
                        continue
                    try:
                        print("|" + "|".join(str(c) for c in row) + "|")
                    except TypeError as e:
                        print("|" + "|".join(str(c) for c in rows) + "|")
            print("~" + ("=" * (item.width() + 3 - 1)) + "~")
