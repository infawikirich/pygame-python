#import the pygame module
import sys

import pygame

# initiat the game
pygame.init()

# set the surface to draw the objects
DISPLAYSURF = pygame.display.set_mode((400, 500))



# set the game loop
while True:
    # get all the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()           # this enable the entire screen to update






