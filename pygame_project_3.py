"""
This program uses pygame to draw a rectangle using the pygame.rect()

"""

# import the pygame module
import pygame

# initiliaze the game module
pygame.init()



# set the size of screen
screen = pygame.display.set_mode((400, 300))
done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # draw the rectangle in the loop. This will keep drawing the shape
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(200, 100, 100, 100))

    pygame.display.flip()

