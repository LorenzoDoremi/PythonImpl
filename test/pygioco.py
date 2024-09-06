import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Create the screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw a Rectangle")

# Fill the screen with the background color
screen.fill(BACKGROUND_COLOR)

# Define the rectangle parameters
rect_color = (255, 0, 0)  # Red
x = 200
y = 200
rect_position = [x, y]  # Top-left corner of the rectangle
rect_size = (200, 150)  # Width and height of the rectangle



# Main game loop
running = True
while running:
    rect_position[0]+=1
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_position, rect_size))
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)