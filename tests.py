import random
import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_20(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_3(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entry_test(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[2][2].has_bottom_wall, False)

    def test_maze_reset_cells(self):
        num_cols = 8
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        random_cell = (random.randrange(8), random.randrange(8))
        i, j = random_cell
        self.assertEqual(m1._cells[i][j].visited, False)
        random_cell = (random.randrange(8), random.randrange(8))
        i, j = random_cell
        self.assertEqual(m1._cells[i][j].visited, False)
        random_cell = (random.randrange(8), random.randrange(8))
        i, j = random_cell
        self.assertEqual(m1._cells[i][j].visited, False)
        random_cell = (random.randrange(8), random.randrange(8))
        i, j = random_cell
        self.assertEqual(m1._cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()
