import os
import time
from random import choice

from src.widget_audio import WidgetAudio
from src.window import Window
from src.table_layout import TableLayout
from src.widget import Widget
from src.alignment import Alignment


def beats():
    thumpers = [
        list("              #"),
        list("             ##"),
        list("            ###"),
        list("         ######"),
        list("             ##"),
        list("           ####"),
        list("         ######"),
        list("     ##########"),
        list("       ########"),
        list("            ###"),
        list("             ##"),
        list("            ###"),
        list("             ##"),
        list("         ######"),
        list("             ##"),
    ]
    while True:
        for thump in thumpers:
            yield [item * 2 for item in thump]


def _main():
    table = TableLayout()

    letters = Widget(list("abcdefghijklmno"), padding=0)
    spinner = WidgetAudio(list("    "), alignment=Alignment.CENTER, padding=0)
    table.add_coloumn(spinner, "##")
    table.add_coloumn(
        Widget(
            [
                "asdf",
                "were",
                "fizz",
                "buzz",
                "bang",
                "23432",
                "vxXxv",
                "Jason1-David2-Jason3-David4",
            ],
            alignment=Alignment.CENTER,
            padding=0,
        ),
        "Words",
    )
    table.add_coloumn(Widget(list("ABCDEFGHIJK"), padding=0), "Caps")
    table.add_coloumn(letters, "Letters")
    table.add_coloumn(
        Widget(["Super", "Cali", "Fragilistic"], alignment=Alignment.RIGHT, padding=0),
        "Magic",
    )

    window = Window()
    window.add(Widget(list(["Example Display"]), alignment=Alignment.CENTER, padding=0))
    window.add(table)
    window.add(Widget(list(["Example Footer"]), alignment=Alignment.CENTER, padding=0))

    thumps = beats()
    for _ in range(100):
        os.system("cls" if os.name == "nt" else "clear")
        spinner.items = next(thumps)
        item = choice("abcX*defghijklmnopqrstuvwxyz")
        letters.extend([item])
        letters.items = letters.items[1:]
        window.render()
        time.sleep(0.2)


if __name__ == "__main__":
    _main()
