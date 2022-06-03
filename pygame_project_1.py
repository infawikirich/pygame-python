"""
    This program launches the pygame module
"""

# import module
import pygame

# initialize the modules or set it for use
pygame.init()

# create a window for object surface
screen = pygame.display.set_mode((400, 500))


done = False
GREEN = (0, 255, 0)   # RGB color triplet for GREEN
radius = 50


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen, GREEN, (100, 100), radius)
    pygame.display.update()


pygame.quit()