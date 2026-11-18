from graphics import Line, Point, Window


class Cell:
    def __init__(self, window: Window):
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.__x1: int = -1
        self.__x2: int = -1
        self.__y1: int = -1
        self.__y2: int = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2, fill_color: str) -> None:
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            self.__win.draw_line(left_wall, fill_color)
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self.__win.draw_line(top_wall, fill_color)
        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self.__win.draw_line(right_wall, fill_color)
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            self.__win.draw_line(bottom_wall, fill_color)
