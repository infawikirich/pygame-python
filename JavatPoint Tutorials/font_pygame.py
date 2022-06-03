import sys

import pygame


pygame.init()


DISPLAYSURF = pygame.display.set_mode((640, 480))


done = False


# load the font
font = pygame.font.SysFont("Times new Roman", 72)

# render the text in new surface
text = font.render("Hello, Pygame", True, (158, 16, 16))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            done = True

    DISPLAYSURF.fill((255, 255, 255))

    DISPLAYSURF.blit(text, (320 - text.get_width()//2, text.get_height()//2))

    # update the entire screen
    pygame.display.flip()




