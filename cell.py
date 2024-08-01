
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.solution = value
        self.screen = screen
        self.can_edit = False
        self.is_sketch = False
        pass

    def set_cell_value(self, value, setup):
        font = setup['font_value']
        if 1 <= value <= 9:
            self.value = value
            self.is_sketch = False
            self.screen.blit(font.render(str(self.value), False, setup['value_color'])
                             , ((self.col * setup['cell_size']) + setup['cell_space_a']
                                , (self.row * setup['cell_size']) + setup['cell_space_b']))
        pass

    def set_sketched_value(self, value, setup):
        font = setup['font_sketch']
        if 1 <= value <= 9:
            self.value = value
            self.is_sketch = True
            self.screen.blit(font.render(str(self.value), False, setup['sketch_color']),
                             ((self.col * setup['cell_size'])+5, (self.row * setup['cell_size'])+5))
        pass

    def draw(self, screen, setup):
        self.screen = screen
        pg = setup['pygame']
        font = setup['font_value']
        pg.draw.rect(self.screen, setup['cell_color'], ((self.col * setup['cell_size'])
                                                        , (self.row * setup['cell_size'])
                                                        , setup['cell_size']
                                                        , setup['cell_size']), setup['cell_width'])
        if self.value != 0:
            self.screen.blit(font.render(str(self.value), False, setup['sudoku_color'])
                             , ((self.col * setup['cell_size']) + setup['cell_space_a']
                                , (self.row * setup['cell_size']) + setup['cell_space_b']))
        pass


    def select_cell(self, screen, setup, color):
        pg = setup['pygame']
        if self.can_edit:
            pg.draw.rect(self.screen, color, ((self.col * setup['cell_size'])
                                              , (self.row * setup['cell_size'])
                                              , setup['cell_size']
                                              , setup['cell_size']), setup['cell_width'])
            return True
        return False
        pass

    def set_initial_value(self, value):
        self.value = value
        self.solution = value
        pass

    def clear(self, setup):
        font = setup['font_value']
        font_sketch = setup['font_sketch']
        # Clear previous value
        if self.is_sketch:
            self.screen.blit(font_sketch.render(str(self.value), False, setup['screen_color']),
                             ((self.col * setup['cell_size']) + 5, (self.row * setup['cell_size']) + 5))
        else:
            self.screen.blit(font.render(str(self.value), False, setup['screen_color']),
                             ((self.col * setup['cell_size']) + setup['cell_space_a']
                              , (self.row * setup['cell_size']) + setup['cell_space_b']))
        pass

    def set_remove_value(self):
        self.value = 0
        self.can_edit = True
        pass

    def is_Valid(self):
        return self.value == self.solution




