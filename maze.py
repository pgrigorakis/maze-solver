import random
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
        win: Window | None = None,
        seed=None,
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list[Cell]] = []
        if seed:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.005)

    def __create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)

            for k in range(len(column)):
                self.__draw_cell(i, k)

    def __draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = i * self._cell_size_x + self.__x1
        cell_x2 = cell_x1 + self._cell_size_x

        cell_y1 = j * self._cell_size_y + self.__y1
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2, "black")
        self.__animate()

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self._num_cols - 1, self._num_rows - 1)

    def __break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_moves = []
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (
                    0 <= ni < self._num_cols
                    and 0 <= nj < self._num_rows
                    and self._cells[ni][nj].visited == False
                ):
                    possible_moves.append((ni, nj))

            if len(possible_moves) == 0:
                self.__draw_cell(i, j)
                return
            else:
                random_direction = random.choice(possible_moves)
                ni, nj = random_direction
                if ni == i - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[ni][nj].has_right_wall = False
                    self.__break_walls_r(ni, nj)
                if ni == i + 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[ni][nj].has_left_wall = False
                    self.__break_walls_r(ni, nj)
                if nj == j - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[ni][nj].has_bottom_wall = False
                    self.__break_walls_r(ni, nj)
                if nj == j + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[ni][nj].has_top_wall = False
                    self.__break_walls_r(ni, nj)

    def __reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _solve_r(self, i: int, j: int) -> bool:
        self.__animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # left
        if (
            i > 0
            and self._cells[i][j].has_left_wall == False
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            val = self._solve_r(i - 1, j)
            if val == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)

        # right
        if (
            i < self._num_cols - 1
            and self._cells[i][j].has_right_wall == False
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            val = self._solve_r(i + 1, j)
            if val == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)

        # top
        if (
            j > 0
            and self._cells[i][j].has_top_wall == False
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            val = self._solve_r(i, j - 1)
            if val == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)

        # bottom
        if (
            j < self._num_rows - 1
            and self._cells[i][j].has_bottom_wall == False
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            val = self._solve_r(i, j + 1)
            if val == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)

        return False

    def solve(self) -> bool:
        return self._solve_r(0, 0)
