from graphics import Cell, Window


def main():
    print("Hello from maze-solver!")


if __name__ == "__main__":
    win = Window(640, 480)

    cell_full = Cell(win)
    cell_left = Cell(win)
    cell_left.has_left_wall = False
    cell_right = Cell(win)
    cell_right.has_right_wall = False
    cell_top = Cell(win)
    cell_top.has_top_wall = False
    cell_bottom = Cell(win)
    cell_bottom.has_bottom_wall = False
    cell_full.draw(10, 10, 60, 60, "red")
    cell_left.draw(10, 70, 60, 120, "red")
    cell_right.draw(10, 130, 60, 180, "red")
    cell_top.draw(10, 190, 60, 240, "red")
    cell_bottom.draw(10, 250, 60, 300, "red")
    win.wait_for_close()
