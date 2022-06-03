import sys

import pygame
from pygame.locals import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((300, 300))
FPS_CLOCK = pygame.time.Clock()


class Player:
    def __init__(self):
        self.rect = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (100, 100, 100, 100))

player = Player()


flag = 1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if flag == 1:
                    pygame.mouse.set_visible(False)
                    flag = 0
                elif flag ==0:
                    pygame.mouse.set_visible(True)
                    flag = 1
            if event.key == pygame.K_1:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if event.key == pygame.K_2:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if event.type == pygame.MOUSEBUTTONDOWN:
           if player.rect.collidepoint(pygame.mouse.get_pos()):
               print("Mouse clicked on the Player")

        if event.type == pygame.MOUSEBUTTONUP:
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse released on the Player")



    pygame.display.update()
    FPS_CLOCK.tick(30)