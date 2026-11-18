from cell import Cell
from graphics import Window

BORDER_COLOR = "black"


def main():
    print("Hello from maze-solver!")


if __name__ == "__main__":
    win = Window(640, 480)

    c1 = Cell(win)
    c2 = Cell(win)

    c1.draw(10, 10, 60, 60, BORDER_COLOR)
    c2.draw(70, 70, 120, 120, BORDER_COLOR)

    c1.draw_move(c2, undo=True)

    win.wait_for_close()
