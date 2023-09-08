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
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window
pygame.display.set_caption("Pixel Art Generator")  # Set the window caption

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize the grid
grid = [[WHITE for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # Create a 2D grid filled with white

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(WIN, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))  # Draw grid cells

def main():
    clock = pygame.time.Clock()  # Create a clock object to control frame rate
    drawing = False  # Flag to indicate whether the mouse is being held down for drawing
    current_color = BLACK  # Current drawing color is initialized to black

    while True:  # Main game loop
        for event in pygame.event.get():  # Check for events (e.g., mouse clicks, key presses, window close)
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit pygame
                sys.exit()  # Exit the script

            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse button is pressed
                drawing = True  # Start drawing

            if event.type == pygame.MOUSEBUTTONUP:  # Mouse button is released
                drawing = False  # Stop drawing

            if drawing and event.type == pygame.MOUSEMOTION:  # Mouse is moving while drawing
                x, y = event.pos  # Get the mouse position
                grid[y // GRID_SIZE][x // GRID_SIZE] = current_color  # Update the color of the corresponding grid cell

        keys = pygame.key.get_pressed()  # Get a list of keys that are currently pressed
        if keys[pygame.K_r]:
            current_color = RED  # Change drawing color to red when 'r' key is pressed
        elif keys[pygame.K_g]:
            current_color = GREEN  # Change drawing color to green when 'g' key is pressed
        elif keys[pygame.K_b]:
            current_color = BLUE  # Change drawing color to blue when 'b' key is pressed
        elif keys[pygame.K_w]:
            current_color = BLACK  # Change drawing color to black when 'w' key is pressed

        draw_grid()  # Draw the grid on the screen
        pygame.display.update()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS

if __name__ == "__main__":
    main()  # Run the main function if this script is executed


