import pygame
import os
import pygame.mouse
from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from pygame.image import load
from Platforms import Platform, PlatformHidden


pygame.mixer.init()
pygame.mixer_music.load('data/sounds/Black Magic.mp3')
pygame.mixer_music.set_volume(0.3)
pygame.mixer_music.play(-1)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


pygame.init()
size = 1200, 540
screen = pygame.display.set_mode(size)
screen.blit(load_image("level_1.jpg"), (0, 0))


class Raul(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((48, 80))
        self.image = load("data/Raul_r0.png").convert_alpha()
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False
        self.stay = True
        self.viewSide = 'r'
        self.stayR = ["Raul_r0.png", "Raul_r1.png", "Raul_r2.png", "Raul_r3.png", "Raul_r4.png", "Raul_r5.png"]
        self.stayL = ["Raul_l0.png", "Raul_l1.png", "v_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
        self.begR = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]
        self.begL = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]
        self.sChMarker = 1
        self.rChMarker = 1
        self.lChMarker = 1

    def update(self, left, right, up, platforms):
        if left and not right:
            self.viewSide = 'l'
            self.stay = False
        if right and not left:
            self.viewSide = 'r'
            self.stay = False
        if self.stay:
            self.rChMarker = 1
            self.lChMarker = 1
            self.begR = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]
            self.begL = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]
            if self.sChMarker == 6:
                self.sChMarker = 1
            else:
                self.sChMarker += 1
            if self.viewSide == 'l' and self.sChMarker == 1:
                self.image = load("data/" + self.stayL[0]).convert_alpha()
                self.stayL.insert(6, self.stayL[0])
                del self.stayL[0]
            elif self.viewSide == 'r' and self.sChMarker == 1:
                self.image = load("data/" + self.stayR[0]).convert_alpha()
                self.stayR.insert(6, self.stayR[0])
                del self.stayR[0]
        else:
            self.sChMarker = 1
            self.stayR = ["Raul_r0.png", "Raul_r1.png", "Raul_r2.png", "Raul_r3.png", "Raul_r4.png", "Raul_r5.png"]
            self.stayL = ["Raul_l0.png", "Raul_l1.png", "Raul_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
            if self.viewSide == 'l':
                self.rChMarker = 1
                if self.lChMarker == 1:
                    self.image = load("data/" + self.begL[0]).convert_alpha()
                    self.begL.insert(4, self.begL[0])
                    del self.begL[0]
                if self.lChMarker == 4:
                    self.lChMarker = 1
                else:
                    self.lChMarker += 1
            elif self.viewSide == 'r':
                self.lChMarker = 1
                if self.rChMarker == 1:
                    self.image = load("data/" + self.begR[0]).convert_alpha()
                    self.begR.insert(4, self.begR[0])
                    del self.begR[0]
                if self.rChMarker == 4:
                    self.rChMarker = 1
                else:
                    self.rChMarker += 1
            if left and not right:
                self.xvel = -MOVE_SPEED
            elif right and not left:
                self.xvel = MOVE_SPEED

        if not (left or right):
            self.stay = True
            self.xvel = 0
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
        if not self.onGround:
            self.yvel += GRAVITY
        self.onGround = False
        if self.rect.x + self.xvel > 0 and self.rect.x + self.xvel < 1152:
            self.rect.x += self.xvel
        elif self.rect.x <= 10:
            self.rect.x = 0
        elif self.rect.x >= 1142:
            self.rect.x = 1152
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0


class Dima(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((48, 80))
        self.image = load("data/Dima_l0.png").convert_alpha()
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False
        self.stay = True
        self.viewSide = 'l'
        self.stayR = ["Dima_r0.png", "Dima_r1.png", "Dima_r2.png", "Dima_r3.png", "Dima_r4.png", "Dima_r5.png"]
        self.stayL = ["Dima_l0.png", "Dima_l1.png", "Dima_l2.png", "Dima_l3.png", "Dima_l4.png", "Dima_l5.png"]
        self.begR = ["Dima_r1b.png", "Dima_r2b.png", "Dima_r3b.png", "Dima_r2b.png"]
        self.begL = ["Dima_l1b.png", "Dima_l2b.png", "Dima_l3b.png", "Dima_l2b.png"]
        self.sChMarker = 1
        self.rChMarker = 1
        self.lChMarker = 1

    def update(self, left, right, up, platforms):
        if left and not right:
            self.viewSide = 'l'
            self.stay = False
        if right and not left:
            self.viewSide = 'r'
            self.stay = False
        if self.stay:
            self.rChMarker = 1
            self.lChMarker = 1
            self.begR = ["Dima_r1b.png", "Dima_r2b.png", "Dima_r3b.png", "Dima_r2b.png"]
            self.begL = ["Dima_l1b.png", "Dima_l2b.png", "Dima_l3b.png", "Dima_l2b.png"]
            if self.sChMarker == 6:
                self.sChMarker = 1
            else:
                self.sChMarker += 1
            if self.viewSide == 'l' and self.sChMarker == 1:
                self.image = load("data/" + self.stayL[0]).convert_alpha()
                self.stayL.insert(6, self.stayL[0])
                del self.stayL[0]
            elif self.viewSide == 'r' and self.sChMarker == 1:
                self.image = load("data/" + self.stayR[0]).convert_alpha()
                self.stayR.insert(6, self.stayR[0])
                del self.stayR[0]
        else:
            self.sChMarker = 1
            self.stayR = ["Dima_r0.png", "Dima_r1.png", "Dima_r2.png", "Dima_r3.png", "Dima_r4.png", "Dima_r5.png"]
            self.stayL = ["Dima_l0.png", "Dima_l1.png", "Dima_l2.png", "Dima_l3.png", "Dima_l4.png", "Dima_l5.png"]
            if self.viewSide == 'l':
                self.rChMarker = 1
                if self.lChMarker == 1:
                    self.image = load("data/" + self.begL[0]).convert_alpha()
                    self.begL.insert(4, self.begL[0])
                    del self.begL[0]
                if self.lChMarker == 4:
                    self.lChMarker = 1
                else:
                    self.lChMarker += 1
            elif self.viewSide == 'r':
                self.lChMarker = 1
                if self.rChMarker == 1:
                    self.image = load("data/" + self.begR[0]).convert_alpha()
                    self.begR.insert(4, self.begR[0])
                    del self.begR[0]
                if self.rChMarker == 4:
                    self.rChMarker = 1
                else:
                    self.rChMarker += 1
            if left and not right:
                self.xvel = -MOVE_SPEED
            elif right and not left:
                self.xvel = MOVE_SPEED

        if not (left or right):
            self.stay = True
            self.xvel = 0
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
        if not self.onGround:
            self.yvel += GRAVITY
        self.onGround = False
        if self.rect.x + self.xvel > 0 and self.rect.x + self.xvel < 1152:
            self.rect.x += self.xvel
        elif self.rect.x <= 10:
            self.rect.x = 0
        elif self.rect.x >= 1142:
            self.rect.x = 1152
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0


hero = Raul(5, 520)
hero1 = Dima(1147, 520)
leftP = rightP = upP = False
leftP1 = rightP1 = upP1 = False

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
sprite_group.add(hero1)
platfroms = []

x, y = 0, 0
for row in load_level('level_1.txt'):
    for col in row:
        if col == '#':
            pl = Platform(x, y)
            sprite_group.add(pl)
            platfroms.append(pl)
        elif col == '0':
            pl = PlatformHidden(x, y)
            sprite_group.add(pl)
            platfroms.append(pl)
        x += 20
    y += 20
    x = 0

MOVE_SPEED = 10
JUMP_POWER = 20
GRAVITY = 2
speed = 10
damage = 0
damage1 = 0


flshoot = True
kshoot = 0
kpshoot = 0
flshoot1 = True
kshoot1 = 0
kpshoot1 = 0


class Snaryad:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 30 * facing

    def draw(self):
        screen.blit(load_image("bullet.png"), (self.x, self.y))


class Snaryad1:
    def __init__(self, x, y, facing1):
        self.x = x
        self.y = y
        self.facing1 = facing1
        self.vel1 = 30 * facing1

    def draw(self):
        screen.blit(load_image("bullet1.png"), (self.x, self.y))


def DrawWindow():
    screen.blit(load_image("level_1.jpg"), (0, 0))

    for bullet in bullets:
        bullet.draw()

    for bullet1 in bullets1:
        bullet1.draw()

    screen.fill(pygame.Color('red'), pygame.Rect(25, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(25, 10, 200 - damage1, 20))
    screen.fill(pygame.Color('red'), pygame.Rect(975, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(975 + damage, 10, 200 - damage, 20))


    sprite_group.draw(screen)

    pygame.display.flip()


clock = pygame.time.Clock()
bullets = []
bullets1 = []
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                leftP = True
            if event.key == pygame.K_d:
                rightP = True
            if event.key == pygame.K_w:
                upP = True
            if event.key == pygame.K_LEFT:
                leftP1 = True
            if event.key == pygame.K_RIGHT:
                rightP1 = True
            if event.key == pygame.K_UP:
                upP1 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                leftP = False
            if event.key == pygame.K_d:
                rightP = False
            if event.key == pygame.K_w:
                upP = False
            if event.key == pygame.K_LEFT:
                leftP1 = False
            if event.key == pygame.K_RIGHT:
                rightP1 = False
            if event.key == pygame.K_UP:
                upP1 = False

    for bullet in bullets:
        if 1300 > bullet.x > -100:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

        if hero1.rect.x + 48 >= bullet.x >= hero1.rect.x and hero1.rect.y + 80 >= bullet.y >= hero1.rect.y:
            damage += 5
            bullets.pop(bullets.index(bullet))

    if kshoot == 10:
        flshoot = False
        kpshoot = 0
        kshoot = 0
    if kpshoot == 30:
        flshoot = True
    if hero.viewSide == "r":
        facing = 1
    elif hero.viewSide == "l":
        facing = -1
    if hero1.viewSide == "r":
        facing1 = 1
    elif hero1.viewSide == "l":
        facing1 = -1

    for bullet1 in bullets1:
        if 1300 > bullet1.x > -100:
            bullet1.x += bullet1.vel1
        else:
            bullets1.pop(bullets1.index(bullet1))

        if hero.rect.x + 48 >= bullet1.x >= hero.rect.x and hero.rect.y + 80 >= bullet1.y >= hero.rect.y:
            damage1 += 5
            bullets1.pop(bullets1.index(bullet1))

    if kshoot1 == 10:
        flshoot1 = False
        kpshoot1 = 0
        kshoot1 = 0
    if kpshoot1 == 30:
        flshoot1 = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if hero.viewSide == "r" and flshoot:
            bullets.append(Snaryad(hero.rect.x + 48, hero.rect.y + 32, facing))
            kshoot += 1
        elif hero.viewSide == "l" and flshoot:
            bullets.append(Snaryad(hero.rect.x - 5, hero.rect.y + 32, facing))
            kshoot += 1

    if keys[pygame.K_KP0]:
        if hero1.viewSide == "r" and flshoot1:
            bullets1.append(Snaryad1(hero1.rect.x + 48, hero1.rect.y + 32, facing1))
            kshoot1 += 1
        elif hero1.viewSide == "l" and flshoot1:
            bullets1.append(Snaryad1(hero1.rect.x - 5, hero1.rect.y + 32, facing1))
            kshoot1 += 1

    if keys[pygame.K_F1]:
        damage = 0
        damage1 = 0

    kpshoot += 1
    kpshoot1 += 1
    DrawWindow()
    hero.update(leftP, rightP, upP, platfroms)
    hero1.update(leftP1, rightP1, upP1, platfroms)
    for bullet in bullets:
        bullet.draw()
    for bullet in bullets1:
        bullet.draw()
# завершение работы:
pygame.quit()
