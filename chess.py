import pygame
from enum import Enum

HEIGHT, WIDTH = 800, 800
CELL_SIZE = 100

SX = WIDTH // CELL_SIZE
SY = HEIGHT // CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def load(which):
    img = pygame.image.load(f'images/{which}.png').convert_alpha()
    return pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))

board = [[None for _ in range(SX)] for _ in range(SY)]

pawn_b = load("pawn-b")
pawn_w = load("pawn-w")
for i in range(SX):
    board[1][i] = pawn_b
    board[SY - 2][i] = pawn_w

board[0][0] = board[0][SX-1] = load("rook-b")
board[0][1] = board[0][SX-2] = load("knight-b")
board[0][2] = board[0][SX-3] = load("bishop-b")
board[0][3] = load("queen-b")
board[0][SX-4] = load("king-b")

board[SY-1][0] = board[SY-1][SX-1] = load("rook-w")
board[SY-1][1] = board[SY-1][SX-2] = load("knight-w")
board[SY-1][2] = board[SY-1][SX-3] = load("bishop-w")
board[SY-1][3] = load("queen-w")
board[SY-1][SX-4] = load("king-w")

class State(Enum):
    IDLE = 0
    MOVING = 1

state = State.IDLE
moving_img = None

def draw():
    for x in range(SX):
        for y in range(SY):
            parity = (x + y) % 2
            color = ( (133, 83, 27), (200, 200, 200) )[parity]
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if piece := board[y][x]:
                screen.blit(piece, (x * CELL_SIZE, y * CELL_SIZE))

    if state == State.MOVING and moving_img:
        mx, my = pygame.mouse.get_pos()
        screen.blit(moving_img, (mx - CELL_SIZE // 2, my - CELL_SIZE // 2))

    pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and state == State.IDLE:
            mx, my = event.pos
            x, y = mx // CELL_SIZE, my // CELL_SIZE
            if piece := board[y][x]:
                state = State.MOVING
                moving_img = piece
                board[y][x] = None

        if event.type == pygame.MOUSEBUTTONUP and state == State.MOVING:
            assert moving_img is not None
            mx, my = event.pos
            x, y = mx // CELL_SIZE, my // CELL_SIZE
            board[y][x] = moving_img
            moving_img = None
            state = State.IDLE

    draw()
    pygame.time.delay(30)