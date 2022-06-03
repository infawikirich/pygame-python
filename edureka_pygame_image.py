import sys

import pygame

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400))
WHITE = 255, 255, 255
BLACK = 0, 0, 0

# load image
image = pygame.image.load("tennis_ball.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(image, (100, 100))
    pygame.display.flip()