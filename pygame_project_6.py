"""
This program draws different plane figures including line
"""

# import the turtle module
import pygame, math

# Initiliaze the module
pygame.init()

# set the caption of the screen
pygame.display.set_caption("Plane figure drawing")

# set the window size
screen = pygame.display.set_mode((400, 300))

# instantiate the pygame clock
clock = pygame.time.Clock()

done = False

while not done:
    # clock.tick() limits the while loop to a max of 10 times per second
    clock.tick(5)

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            done = True

    # Clear the default screen background and set the white screen background
    screen.fill((0, 0, 255))

    # Draw a rectangle outline
    pygame.draw.rect(screen, (0, 100, 0), [75, 50, 75, 20], 2)

    # Draw a solid rectangle
    pygame.draw.rect(screen, (150, 0, 20), [155, 10, 50, 20])

    # Draw a line
    pygame.draw.line(screen, (200, 0, 0), [0, 0], [400, 300], 5)

    # Draw a circle
    pygame.draw.circle(screen, (100, 100, 0), [60, 100], 40, 2)

    # Draw a triangle
    pygame.draw.polygon(screen, (100, 30, 0), [[100, 20], [10, 100], [160, 100]])

    # Draw an ellipse
    pygame.draw.ellipse(screen, (0, 0, 0), [150, 200, 100, 50], 4)

    # Draw an arc
    pygame.draw.arc(screen, (30, 30, 100), [210, 75, 150, 150], 0, math.pi/4, 2)

    # update the drawing on the screen
    pygame.display.flip()


