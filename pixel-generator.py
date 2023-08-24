import pygame
import sys

# Initialize pygame
pygame.init()

# Display settings
GRID_SIZE = 20  # Size of each pixel block
GRID_WIDTH = 25  # Number of pixel blocks in width
GRID_HEIGHT = 25  # Number of pixel blocks in height
WIDTH = GRID_SIZE * GRID_WIDTH
HEIGHT = GRID_SIZE * GRID_HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Art Generator")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize the grid
grid = [[WHITE for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(WIN, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
    clock = pygame.time.Clock()
    drawing = False
    current_color = BLACK

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

            if drawing and event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                grid[y // GRID_SIZE][x // GRID_SIZE] = current_color

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            current_color = RED
        elif keys[pygame.K_g]:
            current_color = GREEN
        elif keys[pygame.K_b]:
            current_color = BLUE
        elif keys[pygame.K_w]:
            current_color = BLACK

        draw_grid()
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

