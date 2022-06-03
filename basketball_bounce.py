"""
    script file : basketball_bounce.py

    Purpose: This codes uses pygame to create a bouncing effect of

    Author: Mr. Asiamah

    Date: 06/06/21

"""

# import the pygame module
import pygame, sys

# set the module for use
pygame.init()

# set the display graphics for the surface and assign it to the screen
size = width, height = 720, 600
screen = pygame.display.set_mode(size)

black = (0, 0, 0)       # set the background color
speed = [2, 2]

# load the image
ball = pygame.image.load("C:\\Users\\CBAS\\Documents\\Python Scripts\\Pycharm\\Pygame\\basket_ball.png")

# set the retangular shape of the ball
ballrect = ball.get_rect()


# begin the game loop
while 1:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()