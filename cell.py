from graphics import Line, Point, Window


class Cell:
    def __init__(self, window: Window | None = None):
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self._x1: int = -1
        self._x2: int = -1
        self._y1: int = -1
        self._y2: int = -1
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2, fill_color: str) -> None:
        if self._win == None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        if self.has_left_wall:
            left_color = fill_color
        else:
            left_color = "white"

        if self.has_right_wall:
            right_color = fill_color
        else:
            right_color = "white"

        if self.has_top_wall:
            top_color = fill_color
        else:
            top_color = "white"

        if self.has_bottom_wall:
            bottom_color = fill_color
        else:
            bottom_color = "white"

        left_wall = Line(top_left, bottom_left)
        top_wall = Line(top_left, top_right)
        right_wall = Line(top_right, bottom_right)
        bottom_wall = Line(bottom_left, bottom_right)
        if self._win:
            self._win.draw_line(left_wall, left_color)
            self._win.draw_line(top_wall, top_color)
            self._win.draw_line(right_wall, right_color)
            self._win.draw_line(bottom_wall, bottom_color)

    def draw_move(self, to_cell: Cell, undo: bool = False) -> None:
        center_self = Point(
            abs(self._x2 + self._x1) // 2, abs(self._y2 + self._y1) // 2
        )
        center_other = Point(
            abs(to_cell._x2 + to_cell._x1) // 2, abs(to_cell._y2 + to_cell._y1) // 2
        )

        center_line = Line(center_self, center_other)

        if self._win:
            if undo:
                self._win.draw_line(center_line, "grey")
                return
            self._win.draw_line(center_line, "red")
