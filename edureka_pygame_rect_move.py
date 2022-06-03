import sys

import pygame

pygame.init()

clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300))
is_blue = True
x, y = 30, 30

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
            is_blue = not is_blue


    # listen if a key is pressed
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3


    DISPLAYSURF.fill((0, 0, 0))
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)


    pygame.draw.rect(DISPLAYSURF, (0, 128, 255), pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    clock.tick(60)

