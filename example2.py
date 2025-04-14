from src.alignment import Alignment
from src.colour import Colour
from src.table_layout import TableLayout
from src.text import Text
from src.widget import Widget
from src.window import Window


def table_layout_example():
    a = Widget(["a", "b", "cakes", "d"], alignment=Alignment.CENTER)
    b = Widget(["1", "2", "200", "23", "00"], alignment=Alignment.LEFT)
    c = Widget(["Jason", "Ali", "Phyllis"], padding=0)
    tbl = TableLayout()
    tbl.add_coloumn(a, "-Super-")
    tbl.add_coloumn(b, "Duper")
    tbl.add_coloumn(c)

    print("~" + ("=" * (tbl.width() + 3 - 1)) + "~")
    for rows in tbl.items_as_rows():
        for row in rows:
            print("|" + "|".join(str(c) for c in row) + "|")
        print("~" + ("=" * (tbl.width() + 3 - 1)) + "~")


def widget_example():
    w = Widget(["a", "b", "cakes", "d", "e"], alignment=Alignment.CENTER)
    for rows in w.items_as_rows():
        for col in rows:
            if "ak" in str(col):
                col._col = Colour.RED
            print("".join(str(c) for c in rows))


def window_example():
    title = Widget(["Title"], alignment=Alignment.CENTER, padding=0)
    items = Widget(["one", "two", "three"], alignment=Alignment.CENTER)

    window = Window()
    window.add(title)
    window.add(items)
    window.render()


def window2_example():
    example = Widget(["Title"], alignment=Alignment.CENTER, padding=0)
    tbl = TableLayout()
    tbl.add(Widget(["Example Display", "asdf"], alignment=Alignment.CENTER, padding=0))
    tbl.add(Widget(["one", "two", "three"]))

    window = Window()
    window.add(example)
    window.add(tbl)

    window.render()


def text_example():
    t = Text("hello", colour=Colour.RED)
    t.width = 10
    print(t)

    t2 = Text("  \033[36mhello\033[0m   ", colour=Colour.BLUE)
    print(t2)


def main():
    for func in (
        # table_layout_example,
        # widget_example,
        window_example,
        window2_example,
        # text_example,
    ):
        func()
        print("-" * 25)


if __name__ == "__main__":
    main()
