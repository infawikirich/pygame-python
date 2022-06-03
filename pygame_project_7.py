"""

This pygame project render text on the screen

"""
# import pygame module
import pygame

# initialize the pygame module
pygame.init()

# set the window title
pygame.display.set_caption('Text Rendering')

# set the window size
screen = pygame.display.set_mode((640, 480))

# load the fonts
font = pygame.font.SysFont('Times new Roman', 72)

# render the text in new surface
text = font.render('Hello, Pygame', True, (158, 16, 16))

# set the flag and game loop
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(text, (320 - text.get_width()//2, 240 - text.get_height()//2))

    # update the screen
    pygame.display.flip()

