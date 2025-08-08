import pygame
import sys

# Init Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CREAM = (245, 245, 220)
BLACK = (0, 0, 0)

# Setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Chess")

# Fonts
FONT = pygame.font.SysFont('Comic Sans MS', 20)

# Pokémon "pieces" (replace with sprites later)
pokemon_pieces = {
    "R": "Onix",     # Rook
    "N": "Scyther",  # Knight
    "B": "Gengar",   # Bishop
    "Q": "Mewtwo",   # Queen
    "K": "Pikachu",  # King
    "P": "Eevee"     # Pawn
}

# Initial Board Setup
def init_board():
    board = [["" for _ in range(COLS)] for _ in range(ROWS)]

    # Red Team (bottom)
    board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
    board[6] = ["P"] * COLS

    # Blue Team (top)
    board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
    board[1] = ["p"] * COLS

    return board

board = init_board()

# Draw board
def draw_board(win):
    win.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = CREAM if (row + col) % 2 == 0 else RED
            pygame.draw.rect(win, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            piece = board[row][col]
            if piece:
                name = pokemon_pieces.get(piece.upper(), "?")
                text = FONT.render(name, True, BLACK)
                win.blit(text, (col*SQUARE_SIZE + 10, row*SQUARE_SIZE + 20))

# Convert pixel to board pos
def get_board_pos(pos):
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE

selected = None
turn = 'red'

# Main loop
def main():
    global selected, turn
    run = True
    while run:
        draw_board(WIN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_board_pos(pygame.mouse.get_pos())

                if selected:
                    piece = board[selected[0]][selected[1]]
                    if piece and ((turn == 'red' and piece.isupper()) or (turn == 'blue' and piece.islower())):
                        board[row][col] = piece
                        board[selected[0]][selected[1]] = ""
                        turn = 'blue' if turn == 'red' else 'red'
                    selected = None
                else:
                    if board[row][col]:
                        selected = (row, col)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
