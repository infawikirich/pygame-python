import sys

import pygame
from pygame.locals import *

pygame.init()

FramePerSec = pygame.time.Clock()

FPS = 60

# create a surface to
DISPLAYSURF = pygame.display.set_mode((600, 442))

# set colors
BLUE = 0, 0, 255

# define the velocity, and position of the body
x, y = 50, 350
vel = 10
m = 1

# define the width and height of the rectangle
width, height = 100, 20

# load a backgroud image
bg = pygame.image.load("bg.jpg")

# This variable shows that we have not jumped yet
isJump = False

# game loop
while True:

    DISPLAYSURF.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # check if a key is pressed
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_LEFT] and x > 0:
        x -= vel

    if pressed_keys[K_RIGHT] and (x + width) < 600:
        x += vel

    if isJump == False:  # still the body has not jumped

        # check if the spacebar is pressed
        if pressed_keys[pygame.K_SPACE]:
            # the body is jumped
            isJump = True

    if isJump:
        # calculate force (F). F = 1/2*mass*velocity^2.
        F = (1 / 2) * m * (vel ** 2)

        # change in the y co-ordinate
        y -= F

        # decreasing the velocity while going up and become negative while coming donwn
        vel -= 1

        # object reached its maximum height
        if vel < 0:
            # negative sign is added to counter negative velocity
            m -= 1

        # object reached its original state
        if vel == -11:
            # making isJump equal to false
            isJump = False

            # setting original values to v and m
            vel = 10
            m = 1
            y = 350

    # This ensures that the shape does not draw on the screen
    #DISPLAYSURF.fill((0, 0, 0))

    pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(x, y, width, height), width=0)

    pygame.display.update()

    FramePerSec.tick(FPS)
