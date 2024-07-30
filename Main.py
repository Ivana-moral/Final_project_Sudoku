import Board
# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
pygame.font.init()
num_font = pygame.font.SysFont('Chiller', 50)
num_font_sketch = pygame.font.SysFont('Arial', 25)

screen = pygame.display.set_mode((900, 900))
board = Board.Board(900, 900, screen, "medium")
clock = pygame.time.Clock()
pygame.display.set_caption('Sudoku MX')
running = True
#dt = 0

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
board.draw("pink", "yellow", "orange", pygame, num_font)

cell_selected = None
is_sketch = False
cell = None

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if cell_selected is not None:
                board.unselect(cell_selected[1], cell_selected[0], pygame)
            cell_selected = board.click(position[1], position[0])
            cell = board.select(cell_selected[1], cell_selected[0], pygame)
            if pygame.mouse.get_pressed()[0]: #Left Click for ACTUAL VALUE
                is_sketch = False
            else:
                is_sketch = True
        if event.type == pygame.KEYDOWN and cell is not None:
            if event.key == pygame.K_1:
                if not is_sketch:
                    cell.set_cell_value(1, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(1, num_font, num_font_sketch)
            elif event.key == pygame.K_2:
                if not is_sketch:
                    cell.set_cell_value(2, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(2, num_font, num_font_sketch)
            elif event.key == pygame.K_3:
                if not is_sketch:
                    cell.set_cell_value(3, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(3, num_font, num_font_sketch)
            elif event.key == pygame.K_4:
                if not is_sketch:
                    cell.set_cell_value(4, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(4, num_font, num_font_sketch)
            elif event.key == pygame.K_5:
                if not is_sketch:
                    cell.set_cell_value(5, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(5, num_font, num_font_sketch)
            elif event.key == pygame.K_6:
                if not is_sketch:
                    cell.set_cell_value(6, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(6, num_font, num_font_sketch)
            elif event.key == pygame.K_7:
                if not is_sketch:
                    cell.set_cell_value(7, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(7, num_font, num_font_sketch)
            elif event.key == pygame.K_8:
                if not is_sketch:
                    cell.set_cell_value(8, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(8, num_font, num_font_sketch)
            elif event.key == pygame.K_9:
                if not is_sketch:
                    cell.set_cell_value(9, num_font, num_font_sketch)
                else:
                    cell.set_sketched_value(9, num_font, num_font_sketch)



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()