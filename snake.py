import pygame
import random
from collections import deque

HEIGHT = 720
WIDTH = 1280
CELL_SIZE = 20

SX = WIDTH // CELL_SIZE
SY = HEIGHT // CELL_SIZE

SNAKE_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snek')

#######################################################

snake = deque([
    (1, SY // 2),
    (2, SY // 2),
])
snake_set = set(snake)
direction = (1, 0)

apple = (SX-2, SY // 2)

def draw():
    screen.fill((255, 255, 255))
    pygame.draw.rect(
        screen,
        APPLE_COLOR,
        (
            apple[0] * CELL_SIZE,
            apple[1] * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        )
    )
    for x, y in snake:
        pygame.draw.rect(
            screen,
            SNAKE_COLOR,
            (
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
        )

def update():
    global apple

    x, y = snake[-1]
    x = (x + direction[0]) % SX
    y = (y + direction[1]) % SY

    if (x, y) == apple:
        snake.append((x, y))
        snake_set.add((x, y))

        while apple in snake_set:
            apple = (random.randint(0, SX-1), random.randint(0, SY-1))

    elif (x, y) in snake_set and (x, y) != snake[0]:
        print('Game over')
        exit()
    else:
        snake.append((x, y))
        snake_set.add((x, y))
        prev = snake.popleft()
        snake_set.remove(prev)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
            elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                running = False
            break

    update()
    draw()

    pygame.display.flip()
    pygame.time.delay(80)