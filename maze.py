from time import sleep

from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window,
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            column = []
            for j in range(self.__num_rows):
                column.append(Cell(self.__win))
            self.__cells.append(column)

            for k in range(len(column)):
                self.__draw_cell(i, k)

    def __draw_cell(self, i, j):
        cell_x1 = i * self.__cell_size_x + self.__x1
        cell_x2 = cell_x1 + self.__cell_size_x

        cell_y1 = j * self.__cell_size_y + self.__y1
        cell_y2 = cell_y1 + self.__cell_size_y

        self.__cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2, "black")
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        sleep(0.005)
