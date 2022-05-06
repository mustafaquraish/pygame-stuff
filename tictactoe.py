import pygame

WIDTH = 900
HEIGHT = 900
CELL_SIZE = 300
SX = WIDTH // CELL_SIZE
SY = HEIGHT // CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToe')

grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def draw():
    screen.fill((255, 255, 255))
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 0: continue
            if cell == 1:
                pygame.draw.circle(
                    screen,
                    (255, 0, 0),
                    (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),
                    CELL_SIZE * 0.9 / 2,
                    10
                )
            else:
                off = CELL_SIZE * 0.1
                pygame.draw.line(
                    screen,
                    (0, 0, 255),
                    (x * CELL_SIZE + off, y * CELL_SIZE + off),
                    (x * CELL_SIZE + CELL_SIZE - off, y * CELL_SIZE + CELL_SIZE - off),
                    15
                )
                pygame.draw.line(
                    screen,
                    (0, 0, 255),
                    (x * CELL_SIZE + off, y * CELL_SIZE + CELL_SIZE - off),
                    (x * CELL_SIZE + CELL_SIZE - off, y * CELL_SIZE + off),
                    15
                )


    for i in range(4):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
        )
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (0,     i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
        )
    pygame.display.flip()

def check_win():
    rows = any(sum(row) in (3, 30) for row in grid)
    cols = any(sum(col) in (3, 30) for col in zip(*grid))
    diag1 = sum(grid[i][i] for i in range(3)) in (3, 30)
    diag2 = sum(grid[i][2-i] for i in range(3)) in (3, 30)
    return rows or cols or diag1 or diag2

player = 1
running = True
draw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            x, y = mx // CELL_SIZE, my // CELL_SIZE

            if grid[y][x] == 0:
                grid[y][x] = player
                player = 1 if player == 10 else 10

            draw()
            if check_win():
                print("Game over :)")
                exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                running = False

    pygame.time.delay(30)