from src.colour import Colour

UPPER_CORNER_LEFT = "┌"
UPPER_CORNER_RIGHT = "┐"
HLINE = "─"
VLINE = "│"
JUNCTION_RIGHT = "├"
JUNCTION_LEFT = "┤"
LOWER_CORNER_LEFT = "└"
LOWER_CORNER_RIGHT = "┘"

# Colours should only be used when sent to screen, if piped
# they should be removed.


COLOURPRE = "\033["
COLOUREND = "\033[0m"

COLOURS = {
    Colour.CYAN: "",
}
