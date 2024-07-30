
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

    def select_cell(self, screen, pg, color="green", width=1):
        if self.can_edit:
            pg.draw.rect(self.screen, color, ((self.col * 100), (self.row * 100), 100, 100), width)
            return True
        return False
        pass

    def unselect_cell(self, screen, pg, color="blue", width=1):
        if self.can_edit:
            pg.draw.rect(self.screen, color, ((self.col * 100), (self.row * 100), 100, 100), width)
        pass

    def set_initial_value(self, value):
        self.value = value
        self.solution = value
        pass

    def set_cell_value(self, value, font, font_small):
        if 1 <= value <= 9:
            self.clear_previous_value(font, font_small)
            self.value = value
            self.is_sketch = False
            self.screen.blit(font.render(str(self.value), False, "brown"), ((self.col * 100) + 35, (self.row * 100) + 25))
        pass

    def set_sketched_value(self, value, font, font_small):
        if 1 <= value <= 9:
            self.clear_previous_value(font, font_small)
            self.value = value
            self.is_sketch = True
            self.screen.blit(font_small.render(str(self.value), False, "navy"),
                             ((self.col * 100)+5, (self.row * 100)+5))
        pass

    def clear_previous_value(self, font, font_small):
        if self.is_sketch:
            self.screen.blit(font_small.render(str(self.value), False, "pink"),
                             ((self.col * 100) + 5, (self.row * 100) + 5))
        else:
            self.screen.blit(font.render(str(self.value), False, "pink"),
                             ((self.col * 100) + 35, (self.row * 100) + 25))
        pass

    def set_remove_value(self):
        self.value = 0
        self.can_edit = True
        pass

    def is_Valid(self):
        return self.value == self.solution

    def draw(self, screen, pg, font, color="blue", width=1):
        self.screen = screen
        pg.draw.rect(self.screen, color, ((self.col * 100), (self.row * 100), 100, 100), width)
        if self.value != 0:
            self.screen.blit(font.render(str(self.value), False, "blue"), ((self.col * 100) + 35, (self.row * 100) + 25))
        pass


