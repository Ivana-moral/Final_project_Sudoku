import SudokuGenerator
import pygame
#This class represents an entire Sudoku board. A Board object has 81 Cell objects.
class Board:


   def __init__(self, width, height, screen, difficulty):
       self.width = width
       self.height = height
       self.screen = screen
       self.difficulty = difficulty #difficulty is a variable to indicate if the user chose easy medium, or hard.
       self.sudoku = self.generate_sudoku()
       pass


   def generate_sudoku(self):
       to_remove = 50
       if self.difficulty == "easy":
           to_remove = 30
       elif self.difficulty == "medium":
           to_remove = 40


       sudoku = SudokuGenerator.SudokuGenerator(9, to_remove)
       sudoku.fill_values()
       sudoku.remove_cells()
       return sudoku


   def draw(self, screen_color, box_color, cell_color, pg, font):
       self.screen.fill(screen_color)
       # Draws every cell on this board.
       for row in self.sudoku.get_board():
           for cell in row:
               cell.draw(self.screen, pg, font, cell_color, 1)
       #Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
       for y in range(3):
           for x in range(3):
               pg.draw.rect(self.screen, box_color, (0 + (x * 300), 0 + (y * 300), 300, 300), 2)
       pass




   def select(self, row, col, pg):
       if self.sudoku.get_board()[row][col].select_cell(self.screen, pg, "green", 1):
           return self.sudoku.get_board()[row][col]
       return None


       #Marks the cell at (row, col) in the board as the current selected cell.
       #Once a cell has been selected, the user can edit its value or sketched value.
       pass


   def unselect(self, row, col, pg):
       self.sudoku.get_board()[row][col].select_cell(self.screen, pg, "orange", 1)
       pass


   def click(self, row, col):
       x, y = None, None
       if 0 <= col <= self.width and 0 <= row <= self.height:
           x, y = col//100, row // 100
       xy_location = (x,y)
       return xy_location
       #If a tuple of (x,y) coordinates is within the displayed board,
       #this function returns a tuple of the (row, col) of the cell which was clicked.
       #Otherwise, this function returns None.
       pass




   def clear(self):
       #Clears the value cell.
       #Note that the user can only remove the cell values and
       #sketched values that are filled by themselves.
       pass




   def sketch(self, value):
       #Sets the sketched value of the current selected cell equal to the user entered value.
       #It will be displayed at the top left corner of the cell using the draw() function.
       pass




   def place_number(self, value):
       #Sets the value of the current selected cell equal to the user entered value.
       #Called when the user presses the Enter key.


       pass




   def reset_to_original(self):
       #Resets all cells in the board to their original values
       #(0 if cleared, otherwise the corresponding digit).
       pass




   def is_full(self):
       #Returns a Boolean value indicating whether the board is full or not.
       pass




   def update_board(self):
       #Updates the underlying 2D board with the values in all cells.
       pass




   def find_empty(self):
       #Finds an empty cell and returns its row and col as a tuple (x,y).
       pass




   def check_board(self):
       #Check whether the Sudoku board is solved correctly.
       pass

