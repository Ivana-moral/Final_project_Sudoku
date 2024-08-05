import SudokuGenerator

# demo sample
# This class represents an entire Sudoku board. A Board object has 81 Cell objects.
class Board:

    def __init__(self, width, height, screen, setup, difficulty):
        # Screen Measurements
        self.width = width
        self.height = height
        # PyGame Controllers
        self.setup = setup
        self.screen = screen
        # difficulty is a variable to indicate if the user chose easy medium, or hard.
        self.difficulty = difficulty
        # Board Sudoku Logic
        self.sudoku = self.generate_sudoku()
        # Cell control
        self.selected_cell = None
        # Type of Value to enter (Sketched or Value)
        self.is_sketched_value = None
        pass

    def generate_sudoku(self):
        to_remove = 50
        if self.difficulty == "Easy":
            to_remove = 30
        elif self.difficulty == "Medium":
            to_remove = 40

        sudoku = SudokuGenerator.SudokuGenerator(9, to_remove)
        sudoku.fill_values()
        sudoku.remove_cells()
        return sudoku

    def draw(self):
        self.screen.fill(self.setup['screen_color'])
        font = self.setup['font_value']
        # Draws every cell on this board.
        for row in self.sudoku.get_board():
            for cell in row:
                cell.draw(self.screen, self.setup)

        pg = self.setup['pygame']
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        for y in range(3):
            for x in range(3):
                pg.draw.rect(self.screen, self.setup['cell_color'], (0 + (x * (self.setup['cell_size'] * 3))
                                                                     , 0 + (y * (self.setup['cell_size'] * 3))
                                                                     , (self.setup['cell_size'] * 3)
                                                                     , (self.setup['cell_size'] * 3))
                             , self.setup['box_width'])

        # Draws additional controls for Reset, Restart, and Exit
        for i in range(3):
            # Back Ground
            pg.draw.rect(self.screen, self.setup['buttons_bgcolor'], (i * (self.setup['cell_size'] * 3)
                                                                    , self.height
                                                                    , self.setup['cell_size'] * 3
                                                                    , self.setup['cell_size'])
                         )
            # Outline
            pg.draw.rect(self.screen, self.setup['buttons_color'], (i * (self.setup['cell_size'] * 3)
                                                                    , self.height
                                                                    , self.setup['cell_size'] * 3
                                                                    , self.setup['cell_size'])
                         ,self.setup['box_width'])
            # Button Display
            self.screen.blit(font.render(self.setup['buttons_game'][i], False, self.setup['buttons_color'])
                             , ((i * (self.setup['cell_size'] * 3)) + self.setup['cell_space_c']
                                , self.height + self.setup['cell_space_b']))
        pass



    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value.
    # Value Type will store either the Value or Sketched to identify the input type
    def select(self, row, col, is_sketched):
        pg = self.setup['pygame']
        # Remove Selection to Previous Selected Cell
        if self.selected_cell is not None:
            self.selected_cell.select_cell(self.screen, self.setup, self.setup['cell_color'])
        # Set Selection to Selected Cell
        new_cell_selected = self.sudoku.get_board()[row][col]
        self.is_sketched_value = is_sketched
        if new_cell_selected.select_cell(self.screen, self.setup, self.setup['select_color']):
            self.selected_cell = new_cell_selected
            return True
        return False
        pass

    # If a tuple of (x,y) coordinates is within the displayed board,
    # this function returns a tuple of the (row, col) of the cell which was clicked.
    # Otherwise, this function returns None.
    # Returns a tuple with the cell position that was clicked
    def click(self, row, col):
        x, y = None, None
        if 0 <= col <= self.width and 0 <= row <= self.height:
            x, y = col//self.setup['cell_size'], row // self.setup['cell_size']
            return (x, y)
        elif row > self.height:
            x, y = col//self.setup['cell_size'], row // self.setup['cell_size']
            return (x, y)
        return None
        pass

    # Clears the value cell.
    # Note that the user can only remove the cell values and
    # sketched values that are filled by themselves.
    def clear(self):
        self.selected_cell.clear(self.setup)
        self.selected_cell.set_remove_value()
        pass

    # Sets the sketched value of the current selected cell equal to the user entered value.
    # It will be displayed at the top left corner of the cell using the draw() function.
    def sketch(self, value):
        self.clear()
        self.selected_cell.set_sketched_value(value, self.setup)
        pass

    # Sets the value of the current selected cell equal to the user entered value.
    # Called when the user presses the Enter key.
    def place_number(self, value):
        self.clear()
        self.selected_cell.set_cell_value(value, self.setup)
        pass

    # Resets all cells in the board to their original values
    # (0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        for row in self.sudoku.get_board():
            for cell in row:
                if cell.can_edit:
                    cell.clear(self.setup)
                    cell.set_remove_value()
        pass

    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        for row in self.sudoku.get_board():
            for cell in row:
                if cell.can_edit:
                    if cell.value == 0 or cell.is_sketch:
                        # If any value is zero that means it is not Full
                        return False
        return True
        pass

    def update_board(self):
        self.sudoku = self.generate_sudoku()
        self.selected_cell = None
        self.is_sketched_value = None
        self.draw()
        pass

    # Finds an empty cell and returns its row and col as a tuple (x,y).
    def find_empty(self):
        board = self.sudoku.get_board()
        for row in board:
            for cell in row:
                if cell.can_edit:
                    if cell.value == 0:
                        # If value is zero then is an empty value
                        location = (board.index(row), row.index(cell))
                        return location
        return None
        pass


    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        if self.is_full():
            for row in self.sudoku.get_board():
                for cell in row:
                    if cell.can_edit:
                        if cell.value != cell.solution:
                            # If any value is different that solution return False
                            return False
            return True
        pass
