import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_wrong_row_col_count(self):
        with self.assertRaises(ValueError) as context:
            Maze(0,0,0,0,10,10)
        self.assertEqual(str(context.exception),"num_rows or num cols cant be 0 or negative")
    
    def test_invalid_types(self):
        with self.assertRaises(TypeError) as context:
            Maze(0,0,2.0,10,10,10)
        self.assertEqual(str(context.exception),"please stick to integer values for num_rows and num_cols")

    def test_cell_count(self):
        num_rows = 10
        num_cols = 10
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(len(m1._cells),num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)
        self.assertEqual(len(m1._cells)*len(m1._cells[0]),num_rows*num_cols)

        num_rows = 1
        num_cols = 5
        m2 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(len(m2._cells),num_rows)
        self.assertEqual(len(m2._cells[0]), num_cols)
        self.assertEqual(len(m2._cells)*len(m2._cells[0]),num_rows*num_cols)

        num_rows = 5
        num_cols = 1
        m3 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(len(m3._cells),num_rows)
        self.assertEqual(len(m3._cells[0]), num_cols)
        self.assertEqual(len(m3._cells)*len(m3._cells[0]),num_rows*num_cols)

    def test_break_entrance_and_exit(self):
        m1 = Maze(0,0,10,10,10,10)
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_top_wall,False)
        self.assertEqual(m1._cells[9][9].has_bottom_wall,False)

    def test_visit_reset(self):
        m1 = Maze(0,0,3,3,10,10)
        m1._cells[0][0].visited = True
        m1._cells[1][1].visited = True
        m1._reset_cells_visited()
        self.assertEqual(m1._cells[0][0].visited,False)
        self.assertEqual(m1._cells[1][1].visited,False)




if __name__ == "__main__":
    unittest.main()