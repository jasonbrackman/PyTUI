from src.constants import UPPER_CORNER_LEFT, HLINE, UPPER_CORNER_RIGHT, VLINE, \
    JUNCTION_RIGHT, JUNCTION_LEFT, LOWER_CORNER_LEFT, LOWER_CORNER_RIGHT
from src.layout import LayoutImpl


class Window(LayoutImpl):
    def render(self, fill: str = '') -> None:
        count = 0
        collection = {}
        max_width = 0

        for item in self._items:
            if hasattr(item, 'display_headers') and item.display_headers:
                rows = item.render_headers()
                collection[count] = rows
                count += 1

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
