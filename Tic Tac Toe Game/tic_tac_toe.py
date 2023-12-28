import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
LINE_WIDTH = 15
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize fonts
font = pygame.font.SysFont(None, 55)

# Initialize variables
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'
game_over = False
winner = None

def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * WIDTH / 3, 0), (i * WIDTH / 3, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * HEIGHT / 3), (WIDTH, i * HEIGHT / 3), LINE_WIDTH)

def draw_players():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                x_pos = col * WIDTH / 3 + WIDTH / 6
                y_pos = row * HEIGHT / 3 + HEIGHT / 6
                pygame.draw.line(screen, LINE_COLOR, (x_pos - 50, y_pos - 50), (x_pos + 50, y_pos + 50), LINE_WIDTH)
                pygame.draw.line(screen, LINE_COLOR, (x_pos + 50, y_pos - 50), (x_pos - 50, y_pos + 50), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, (col * WIDTH / 3 + WIDTH / 6, row * HEIGHT / 3 + HEIGHT / 6), 50, LINE_WIDTH)

def check_winner():
    global game_over, winner
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            game_over = True
            winner = board[row][0]
            return

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            game_over = True
            winner = board[0][col]
            return

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        game_over = True
        winner = board[0][0]
        return
    if board[0][2] == board[1][1] == board[2][0] != '':
        game_over = True
        winner = board[0][2]
        return

def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return False
    return True

def draw_text(msg, color, y_displace=0):
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_displace))
    screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            col = x // (WIDTH // 3)
            row = y // (HEIGHT // 3)

            if board[row][col] == '':
                board[row][col] = current_player
                check_winner()
                if not game_over:
                    current_player = 'O' if current_player == 'X' else 'X'

    screen.fill(WHITE)
    draw_board()
    draw_players()

    if winner:
        draw_text(f"Player {winner} wins!", LINE_COLOR, 20)
    elif game_over:
        draw_text("It's a tie!", LINE_COLOR, -50)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
