import os
import time
from random import choice

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

    letters = Widget(list("abcdefghijklmno"), padding=2)
    spinner = Widget(list("    "), alignment=Alignment.CENTER, padding=2)
    table.add_coloumn(spinner, '##')
    table.add_coloumn(Widget(["asdf", 'were', 'fizz', 'buzz', 'bang', '23432', 'vxXxv', "Jason1-David2-Jason3-David4"], alignment=Alignment.CENTER, padding=2), "Words")
    table.add_coloumn(Widget(list("ABCDEFGHIJK"), padding=2), "Caps")
    table.add_coloumn(letters, "Letters")
    table.add_coloumn(Widget(["Super", "Cali", "Fragilistic"], alignment=Alignment.RIGHT, padding=2), "Magic")

    window = Window()
    window.add(Widget(list(["Example Display"]), alignment=Alignment.CENTER, padding=2))
    window.add(table)
    window.add(Widget(list(["Example Footer"]), alignment=Alignment.CENTER, padding=2))

    thumps = beats()
    for _ in range(200):
        os.system('cls' if os.name == 'nt' else 'clear')
        spinner.items = next(thumps)
        items = choice(list("abcX*defghijklmnopqrstuvwxyz"))
        letters.extend([items])
        letters.items = letters.items[1:]
        window.render()
        time.sleep(0.2)

if __name__ == '__main__':
    _main()
