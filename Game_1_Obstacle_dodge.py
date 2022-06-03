

import pygame, sys
import random, time
from pygame.locals import *   # this allows one to use functions and modules without appending pygame to it

# initialize the game
pygame.init()


# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()


# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
game_score = font_small.render("Your Score is", True, BLACK)

background = pygame.image.load("background_road.png")


# Setup a 300x300 pixel display with caption
size = SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED = 5
SCORE = 0
DISPLAYSURF = pygame.display.set_mode(size)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Collision Game")


# Creating Lines and Shapes
# pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (130, 170), 3)
# pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (170, 170), 3)
# pygame.draw.line(DISPLAYSURF, BLUE, (130, 170), (170, 170), 3)
# pygame.draw.circle(DISPLAYSURF, BLACK, (100, 50), 30)
# pygame.draw.circle(DISPLAYSURF, BLACK, (200, 50), 30)
# pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (110, 260, 80, 5), 4)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH -40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)


    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0, 5)


        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()

#Creating Spirites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


#Adding a new user event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)



#Game Loop
while True:

    # Cycle through all events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))


    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()


    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)


        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        DISPLAYSURF.blit(game_score, (40, 200))
        DISPLAYSURF.blit(scores, (200, 200))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()


    pygame.display.update()
    FramePerSec.tick(FPS)


