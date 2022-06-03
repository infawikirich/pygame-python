# import pygame and its libraries
import sys

import pygame
from pygame.locals import *
import random
import time

# initialize the game
pygame.init()
vec = pygame.math.Vector2       # 2 for two dimensional

# set constants
HEIGHT , WIDTH = 450, 400
ACC, FRIC = 0.5, -0.12    # ACC is acceleration, FRIC is friction of the body
FPS = 60

FramePerSec = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platform Game")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 255, 40))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 360))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumping = False
        self.score = 0


    def move(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC


        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc


        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos



    def update(self):
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if player.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False


    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3


    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15





class PlatForm(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10), (random.randint(0, HEIGHT-30))))

        self.speed = random.randint(-1, 1)

        self.moving = True
        self.point = True

    def move(self):
        hits =self.rect.colliderect(player.rect)
        if self.moving == True:
            self.rect.move_ip(self.speed, 0)
            if hits:
                player.pos += (self.speed, 0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH


    def generateCoin(self):
        if (self.speed == 0):
            coins.add(Coin((self.rect.centerx, self.rect.centery - 50)))


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def update(self):
        if self.rect.colliderect(player.rect):
            player.score += 5
            self.kill()

def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 40) and (abs(platform.rect.bottom - entity.rect.top) < 40):
                return True
            C = False


def plat_gen():
    while len(platforms) < 6:
        width = random.randrange(50, 100)
        p = PlatForm()
        C = True

        while C:
            p = PlatForm()
            p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))

            C = check(p, platforms)

        p.generateCoin()
        platforms.add(p)
        all_sprites.add(p)




player = Player()
platform = PlatForm()

platform.moving = False
platform.point = False


platform.surf = pygame.Surface((WIDTH, 20))
platform.surf.fill((255, 0, 0))
platform.rect = platform.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))



# set up the sprites of the game
all_sprites = pygame.sprite.Group()
all_sprites.add(platform)
all_sprites.add(player)

platforms = pygame.sprite.Group()
platforms.add(platform)

coins = pygame.sprite.Group()

for x in range(random.randint(4, 5)):
    C = True
    pl = PlatForm()

    while C:
        pl = PlatForm()
        C = check(pl, platforms)
    pl.generateCoin()
    platforms.add(pl)
    all_sprites.add(pl)


# set the game loop
while True:
    player.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.cancel_jump()

    if player.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            DISPLAYSURF.fill((255, 0, 0))
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            sys.exit()

    if player.rect.top <= HEIGHT/3:
        player.pos.y += abs(player.vel.y)
        for plat in platforms:
            plat.rect.y += abs(player.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()


    plat_gen()
    DISPLAYSURF.fill((0, 0, 0))
    f = pygame.font.SysFont("Verdana", 20)
    g = f.render(str(player.score), True, (123, 255, 0))
    DISPLAYSURF.blit(g, (WIDTH/2, 10))


    for entity in all_sprites:
        DISPLAYSURF.blit(entity.surf, entity.rect)
        entity.move()

    for coin in coins:
        DISPLAYSURF.blit(coin.image, coin.rect)
        coin.update()


    pygame.display.update()
    FramePerSec.tick(FPS)