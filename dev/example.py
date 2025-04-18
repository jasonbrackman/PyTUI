import os
import time
from random import choice

from pytui.layout import TableLayout
from pytui.widget import Widget, WidgetAudio, Window
from pytui.core import Alignment


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
    header = Widget(["Example Display"], alignment=Alignment.CENTER, padding=0)
    footer = Widget(["Example Footer"], alignment=Alignment.CENTER, padding=0)
    letters = Widget(list("abcdefghijklmno"), alignment=Alignment.CENTER, padding=1)
    spinner = WidgetAudio(list("    "), alignment=Alignment.CENTER, padding=1)
    caps = Widget(list("ABCDEFGHIJK"), padding=1)
    magic = Widget(
        ["Super", "Cali", "Fragilistic"], alignment=Alignment.RIGHT, padding=1
    )
    list_01 = Widget(
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
        padding=1,
    )

    table = TableLayout()

    table.add_coloumn(spinner, "##")
    table.add_coloumn(list_01, "Words")
    table.add_coloumn(caps, "Caps")
    table.add_coloumn(letters, "Letters")
    table.add_coloumn(magic, "Magic")

    window = Window()
    window.add(header)
    window.add(table)
    window.add(footer)

    thumps = beats()
    for _ in range(1):
        os.system("cls" if os.name == "nt" else "clear")
        spinner.items = next(thumps)
        item = choice("abcX*defghijklmnopqrstuvwxyz")
        letters.extend([item])
        letters.items = letters.items[1:]
        window.render()
        time.sleep(0.2)


if __name__ == "__main__":
    _main()
