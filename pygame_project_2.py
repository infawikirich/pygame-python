"""
    This program loads an image
"""

import pygame

# This is used to initialize all the required module of the pygame
pygame.init()

# set the color
white = (255, 255, 255)

# set the dimension of the game screen
height, width = 400, 400

display_surface = pygame.display.set_mode((height, width))

# set the pygame window name
pygame.display.set_caption('Image Rendering')

# creating a surface object, image is drawn on it
image = pygame.image.load(r'C:\Users\CBAS\Documents\Python Scripts\Pycharm\Pygame\Vision.png')

# infinite loop for the game
while True:
    display_surface.fill(white)
    display_surface.blit(image, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Draws the surface object to the screen
        pygame.display.update()
