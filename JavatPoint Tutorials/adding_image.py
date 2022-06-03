#import the pygame module
import sys

import pygame

# initialize the game
pygame.init()

# set the display size
WIDTH = 500
HEIGHT = 400
WHITE = 255, 255, 255

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

# set the caption of the window
pygame.display.set_caption("Pygame Image")


image = pygame.image.load("pygame.png")


# game loop
while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(image, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
