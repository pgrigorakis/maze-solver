from graphics import Window
from maze import Maze

BORDER_COLOR = "black"


def main():
    print("Hello from maze-solver!")


if __name__ == "__main__":
    win = Window(640, 480)

    maze = Maze(10, 10, 20, 20, 50, 50, win)
    win.wait_for_close()
