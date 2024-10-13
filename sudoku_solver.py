from copy import deepcopy
from datetime import datetime
from typing import List, Tuple

import math

# Generic Sudoku Solver
class SudokuSolver:

    # Constructor
    # ************************
    # cell_options param might look like ["W", "L", "F", "S", "T", "R", "N", "G", "P"]
    # The size of the grid will always be the length of cell_options  
    def __init__(self, cell_options:List[str]) -> None:
        self.cell_options: List[str] = cell_options
        self.grid_size: int = len(cell_options)
        self.grid_sqrt: int = int(math.sqrt(self.grid_size))

        # Lists of sets for values you can still put in each col, row, and box
        self.valid_col_values: List[set] = []
        self.valid_row_values: List[set] = []
        self.valid_box_values: List[set] = []
    
    # solve
    # *************************
    # Takes a sudoku grid with some values filled in (2D array) and returns a solution grid 
    # with all cells filled in (also a 2D array).  Empty cell values are None.
    def solve(self, grid:List[List[str]]) -> List[List[str]]:
        self.setup(grid)
        return self.recurse(grid, 0, 0)
        

                    
    def recurse(self, grid:List[List[str]], col, row) -> List[List[str]]:

        # find next None cell (or make row go past gridsize by 1)
        col, row = self.find_next_cell(grid, col, row)
        
        if row >= self.grid_size:
            # return the filled out grid
            return grid

        else:
            # for loop through the valid characters you can put in the current cell                
            for character in self.valid_characters(col, row):

                ''' CHOOSE '''
                self.remove_valid_value(character, col, row)
                grid[row][col] = character

                ''' EXPLORE '''
                board = self.recurse(grid, col, row)
                if board != None:
                    return board
                
                ''' UNCHOOSE '''
                grid[row][col] = None
                self.add_valid_value(character, col, row)
                
            return None



    def setup(self, grid):
        setup_set = set()
        for cell_option in self.cell_options:
            setup_set.add(deepcopy(cell_option))

        print(setup_set)

        # setup the 3 lists of sets for rows, columns, and boxes
        for i in range(self.grid_size):
            self.valid_col_values.append(deepcopy(setup_set))
            self.valid_row_values.append(deepcopy(setup_set))
            self.valid_box_values.append(deepcopy(setup_set))

        # need to update the valid values to be aware of the values the grid starts with
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if grid[i][j] != None:
                    self.remove_valid_value(grid[i][j], j, i)
        



    def remove_valid_value(self, char, col, row):
        self.valid_col_values[col].discard(char)
        self.valid_row_values[row].discard(char)
        self.valid_box_values[self.current_box_index(col, row)].discard(char)

    def add_valid_value(self, char, col, row):
        self.valid_col_values[col].add(char)
        self.valid_row_values[row].add(char)
        self.valid_box_values[self.current_box_index(col, row)].add(char)




    def valid_characters(self, col, row) -> set:
        valid_characters = self.valid_col_values[col].intersection(self.valid_row_values[row]).intersection(self.valid_box_values[self.current_box_index(col, row)])
        return valid_characters

    def current_box_index(self, col, row) -> int:
        return (col // self.grid_sqrt) + (row // self.grid_sqrt) * self.grid_sqrt

    def find_next_cell(self, grid, col, row) -> Tuple:
        while grid[row][col] != None or row > self.grid_size:

            if col+1 >= self.grid_size:
                col = 0
                row += 1
            else:
                col += 1
            if row == self.grid_size:
                break
        return (col, row)