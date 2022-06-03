import sys

import pygame
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300, 300))

surface1 = pygame.Surface((50, 50))
surface1.fill((0, 255, 0))

surface2 = pygame.Surface((150, 50))
surface2.fill((255, 255, 0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(surface1, (50, 50))
    DISPLAYSURF.blit(surface2, (50, 150))

    pygame.display.update()



