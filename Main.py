import Board
import pygame

def key_pressed(value):
    if 49 <= event.key <= 57:
        return event.key - 48
    elif 1073741913 <= event.key <= 1073741921:
        return event.key - 1073741912
    else:
        return None
    pass



# pygame setup for graph and fonts
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

#control variables
running_board = True
cell_location = None
position = None
# True : Actual Value otherwise Sketched Value
left_click = None
cell_selected = None

#pygame object development kit for our game
pg_setup={}
pg_setup['screen_color'] = "pink"
pg_setup['cell_color'] = "yellow"
pg_setup['sudoku_color'] = "blue"
pg_setup['select_color'] = "green"
pg_setup['value_color'] = "purple"
pg_setup['sketch_color'] = "navy"
pg_setup['buttons_bgcolor'] = "magenta"
pg_setup['buttons_color'] = "white"
pg_setup['cell_size'] = 75
pg_setup['cell_space_a'] = int(round((pg_setup['cell_size'] * 35)/100))
pg_setup['cell_space_b'] = int(round((pg_setup['cell_size'] * 25)/100))
pg_setup['cell_space_c'] = int(round((pg_setup['cell_size'] * 100)/100))
pg_setup['cell_width'] = 1
pg_setup['box_width'] = 2
pg_setup['pygame'] = pygame
pg_setup['font_value'] = pygame.font.SysFont('Chiller', int(round((pg_setup['cell_size'] * 50)/100)))
pg_setup['font_sketch'] = pygame.font.SysFont('Arial', int(round((pg_setup['cell_size'] * 25)/100)))
pg_setup['buttons_game'] = ['Reset', 'Restart', 'Exit']

# Initialize the Game
pygame.display.set_caption('Sudoku MX')
screen = pygame.display.set_mode((pg_setup['cell_size'] * 9, pg_setup['cell_size']*10))



# Start the game = generate the Sudoku game and draw the board
board = Board.Board(pg_setup['cell_size'] * 9, pg_setup['cell_size'] * 9, screen, pg_setup, 'Easy')
board.draw()

# Capture the control events
while running_board:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_board = False
        # Left Click will control the Value
        # Right Click will control the sketched
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            cell_location = board.click(position[1], position[0])
            left_click = pygame.mouse.get_pressed()[0]
            # Detect Button Area
            if cell_location[1] > 8:
                # Reset
                if 0 <= cell_location[0] <= 2:
                    board.reset_to_original()
                # Restart
                elif 3 <= cell_location[0] <= 5:
                    board.update_board()
                else:
                # Exit
                    running_board = False
                    cell_selected = False
            elif cell_location is not None:
                cell_selected = board.select(cell_location[1], cell_location[0], not left_click)
        if event.type == pygame.KEYDOWN and cell_selected:
            # Clear the value with backspace and delete keys
            key_value = key_pressed(event.key)
            # Event Key = 49 = 1 .... 57 = 9
            # or 1073741913 = 1 .... 1073741921 = 9
            if key_value is not None:
                if left_click:
                    board.place_number(key_value)
                else:
                    board.sketch(key_value)


            # Clear the beard
            elif event.key == 99:
                board.reset_to_original()
            elif event.key == 102:
                print(board.is_full(), ' is full')
            elif event.key == 101:
                print(board.find_empty(), ' is empty')
            elif event.key == 114:
                board.update_board()

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
