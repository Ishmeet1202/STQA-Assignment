import pygame
import sys
from game_logic import TicTacToe

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 3
BACKGROUND_COLOR = (33, 33, 33)  # #212121
CELL_COLOR = (98, 213, 148)       # rgb(98, 213, 148)
HOVER_COLOR = (16, 207, 99)       # rgb(16, 207, 99)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Font for displaying text
font = pygame.font.Font(None, 40)

# Initialize the game
game = TicTacToe()

def draw_board():
    # Draw the grid lines and cells
    for row in range(3):
        for col in range(3):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.rect(screen, CELL_COLOR, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BACKGROUND_COLOR, (x, y, CELL_SIZE, CELL_SIZE),5)  # Grid lines

def draw_symbols():
    # Draw X and O symbols
    for i in range(9):
        row = i // 3
        col = i % 3
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        if game.board[i] == "X":
            pygame.draw.line(screen, RED, (x - 50, y - 50), (x + 50, y + 50), 10)     # DRAWING "X"
            pygame.draw.line(screen, RED, (x + 50, y - 50), (x - 50, y + 50), 10)
        elif game.board[i] == "O":
            pygame.draw.circle(screen, BLUE, (x, y), 50, 10)                          # DRAWING "O"

def draw_hover():
    # Highlight the cell under the mouse
    mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    col = mouse_pos[0] // CELL_SIZE
    row = mouse_pos[1] // CELL_SIZE
    index = row * 3 + col

    if 0 <= index < 9 and game.board[index] == " ":
        pygame.draw.rect(screen, HOVER_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def display_message(message):
    # Display a message (e.g., "Winner is X" or "Game Drawn!")
    screen.fill(BACKGROUND_COLOR)  # Clear the screen with #212121
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # HEIGHT AND WIDTH BOTH ARE 600px
    screen.blit(text, text_rect)

def draw_button(text, x, y, width, height, color, hover_color):
    # Draw a button with hover effect
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # print(click)

    # starting_x < mouseX < starting_x + width -> HERE width is the total width of the button
    # starting_y < mouseY < starting_y + height -> HERE height is the total height of the button

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return False

def main():
    global game
    running = True
    message = ""
    show_start_screen = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game.winner and not show_start_screen:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                position = row * 3 + col + 1  # Convert to 1-9 position
                result = game.make_move(position)
                if "Winner" in result or "Draw" in result:
                    message = result

        screen.fill(BACKGROUND_COLOR)

        if show_start_screen:
            display_message("Tic-Tac-Toe")
            if draw_button("Play", WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50, CELL_COLOR, HOVER_COLOR):
                show_start_screen = False
        else:
            if not message:
                draw_board()
                draw_symbols()
                draw_hover()  # Draw hover effect
            else:
                display_message(message)
                if draw_button("Play Again", WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50, CELL_COLOR, HOVER_COLOR):
                    game.reset_game()
                    message = ""
                    show_start_screen = True

        pygame.display.flip() # FOR REFRESHING AFTER EVERY TURN

    pygame.quit()  # EXITING THE GAME
    sys.exit()  # CLOSE RUNNING PYTHON SCRIPT

if __name__ == "__main__":
    main()