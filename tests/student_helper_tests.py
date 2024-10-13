from unittest import TestCase
from sudoku_solver import SudokuSolver

class SudokuSolverStudentTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_student_helper_function_case(self): 
        # tests setup method
        
        puzzle = [["A", "B", "C", "D"],
                 ["C", None, "A", "B"],
                 ["B", "A", "D", None],
                 ["D", None, "B", "A"]]

        solver = SudokuSolver(["A", "B", "C", "D"])
        solver.setup(puzzle)

        self.assertEquals(solver.valid_col_values, [set(),    {"C", "D"}, set(),    {"C"}])
        self.assertEquals(solver.valid_row_values, [set(),    {"D"},      {"C"}, {"C"}])
        self.assertEquals(solver.valid_box_values, [{"D"}, set(),         {"C"}, {"C"}])