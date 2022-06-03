#import pygame module
import sys

import pygame

#intialize the game
pygame.init()

# set the screen size
DISPLAYSURF = pygame.display.set_mode((400, 400))

# set colors
WHITE = 255, 255, 255
RED = 255, 0, 0
BLUE = 0, 0, 255
BACKGROUND = 128, 128, 128


# game loop goes here
while True:

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BACKGROUND)

    # draw the rectangle
    pygame.draw.rect(DISPLAYSURF, WHITE, pygame.Rect(75, 10, 50, 100), 0)
    pygame.draw.polygon(DISPLAYSURF, RED, [(100, 100), (0, 200), (200, 200)], 5)
    pygame.draw.polygon(DISPLAYSURF, BLUE, [(150, 100), (200, 150), (200, 200), (150, 250), (100, 250), (50, 200), (50, 150), (100, 100)])
    pygame.draw.circle(DISPLAYSURF, WHITE, (250, 300), 100, 2)

    pygame.display.update()