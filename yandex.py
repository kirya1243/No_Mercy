import pygame
import os
import pygame.mouse
from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from pygame.image import load
from Platforms import Platform, PlatformHidden


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
screen.blit(load_image("bg.jpg"), (0, 0))


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
        self.flshoot = True
        self.kshoot = 0
        self.kpshoot = 0
        self.viewSide = 'r'
        self.stayR = ["Raul_r0.png", "Raul_r1.png", "Raul_r2.png", "Raul_r3.png", "Raul_r4.png", "Raul_r5.png"]
        self.stayL = ["Raul_l0.png", "Raul_l1.png", "Raul_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
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

        bullets = []
        if shoot:
            if self.viewSide == "l" and self.flshoot:
                facing = -1
                bullets.append(Snaryad(self.rect.left + 25, self.rect.top + 32, facing))
                self.kshoot += 1
            elif self.viewSide == "r" and self.flshoot:
                facing = 1
                bullets.append(Snaryad(self.rect.right - 28, self.rect.top + 32, facing))
                self.kshoot += 1

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
        self.kpshoot += 1
        self.collide(0, self.yvel, platforms)
        for bullet in bullets:
            if 1300 > bullet.x > -100:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        for bullet in bullets:
            bullet.draw()

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
leftP = rightP = upP = shoot = False

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
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
x1 = 5
y1 = 430
x2 = 1147
y2 = 430
speed = 10
damage = 0
damage1 = 0

kdvij = 0
isJump = False
right = False
left = False
stay = True
shoot = False
flshoot = True
kshoot = 0
kpshoot = 0
flstay = 0
jumpCount = 8
animCount = 0
lastMove = "right"

kdvij1 = 0
isJump1 = False
right1 = False
left1 = False
stay1 = True
flshoot1 = True
kshoot1 = 0
kpshoot1 = 0
flstay1 = 0
jumpCount1 = 8
animCount1 = 0
lastMove1 = "left"

raul = "Raul_r0.png"
dima = "Raul_l0.png"
wright = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]
wleft = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]


class Snaryad:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 30 * facing

    def draw(self):
        screen.blit(load_image("bullet.png"), (self.x, self.y))


# class Snaryad1():
#     def __init__(self, x, y, facing1):
#         self.x = x
#         self.y = y
#         self.facing1 = facing1
#         self.vel1 = 30 * facing1
#
#     def draw(self):
#         screen.blit(load_image("bullet1.png"), (self.x, self.y))


def DrawWindow():
    global animCount, raul, kdvij, flstay, left, right, stay
    global animCount1, dima, kdvij1, flstay1, left1, right1, stay1
    screen.blit(load_image("bg.jpg"), (0, 0))

    for bullet in bullets:
        bullet.draw()

    for bullet1 in bullets1:
        bullet1.draw()

    screen.blit(load_image(raul), (x1, y1))
    screen.blit(load_image(dima), (x2, y2))
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                leftP = False
            if event.key == pygame.K_d:
                rightP = False
            if event.key == pygame.K_w:
                upP = False

    for bullet in bullets:
        if 1300 > bullet.x > -100:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

        if x2 + 48 >= bullet.x >= x2 and y2 + 80 >= bullet.y >= y2:
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

    # for bullet1 in bullets1:
    #     if 1300 > bullet1.x > -100:
    #         bullet1.x += bullet1.vel1
    #     else:
    #         bullets1.pop(bullets1.index(bullet1))
    #
    #     if x1 + 48 >= bullet1.x >= x1 and y1 + 80 >= bullet1.y >= y1:
    #         damage1 += 5
    #         bullets1.pop(bullets1.index(bullet1))

    # if kshoot1 == 10:
    #     flshoot1 = False
    #     kpshoot1 = 0
    #     kshoot1 = 0
    # if kpshoot1 == 30:
    #     flshoot1 = True
    if lastMove1 == "right":
        facing1 = 1
    elif lastMove1 == "left":
        facing1 = -1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if hero.viewSide == "r" and flshoot:
            bullets.append(Snaryad(hero.rect.x + 48, hero.rect.y + 32, facing))
            kshoot += 1
        elif hero.viewSide == "l" and flshoot:
            bullets.append(Snaryad(hero.rect.x - 5, hero.rect.y + 32, facing))
            kshoot += 1
    #
    # if keys[pygame.K_KP0]:
    #     if lastMove1 == "right" and flshoot1:
    #         bullets1.append(Snaryad1(x2 + 48, y2 + 32, facing1))
    #         kshoot1 += 1
    #     elif lastMove1 == "left" and flshoot1:
    #         bullets1.append(Snaryad1(x2, y2 + 32, facing1))
    #         kshoot1 += 1
    #
    if keys[pygame.K_F1]:
        damage = 0
        damage1 = 0
    #
    # if keys[pygame.K_d] and x1 < 1147:
    #     x1 += speed
    #     right = True
    #     left = False
    #     stay = False
    #     lastMove = "right"
    #     flstay = 0
    # elif keys[pygame.K_a] and x1 > 5:
    #     x1 -= speed
    #     right = False
    #     left = True
    #     stay = False
    #     lastMove = "left"
    #     flstay = 0
    # else:
    #     stay = True
    #     right = False
    #     left = False
    #     animCount = 0
    # if not (isJump):
    #     if keys[pygame.K_w]:
    #         isJump = True
    #         # raul = raul[:6] + '0' + raul[6 + 1:]
    #         stay = False
    # else:
    #     if jumpCount >= -8:
    #         if jumpCount < 0:
    #             y1 += (jumpCount ** 2) / 2
    #         else:
    #             y1 -= (jumpCount ** 2) / 2
    #         jumpCount -= 1
    #     else:
    #         isJump = False
    #         jumpCount = 8
    #
    # if keys[pygame.K_RIGHT] and x2 < 1147:
    #     x2 += speed
    #     right1 = True
    #     left1 = False
    #     stay1 = False
    #     lastMove1 = "right"
    #     flstay1 = 0
    # elif keys[pygame.K_LEFT] and x2 > 5:
    #     x2 -= speed
    #     right1 = False
    #     left1 = True
    #     stay1 = False
    #     lastMove1 = "left"
    #     flstay1 = 0
    # else:
    #     stay1 = True
    #     right1 = False
    #     left1 = False
    #     animCount1 = 0
    # if not (isJump1):
    #     if keys[pygame.K_UP]:
    #         isJump1 = True
    #         # raul = raul[:6] + '0' + raul[6 + 1:]
    #         stay1 = False
    # else:
    #     if jumpCount1 >= -8:
    #         if jumpCount1 < 0:
    #             y2 += (jumpCount1 ** 2) / 2
    #         else:
    #             y2 -= (jumpCount1 ** 2) / 2
    #         jumpCount1 -= 1
    #     else:
    #         isJump1 = False
    #         jumpCount1 = 8

    kpshoot += 1
    kpshoot1 += 1
    DrawWindow()
    hero.update (leftP, rightP, upP, platfroms)
    for bullet in bullets:
        bullet.draw()
# завершение работы:
pygame.quit()
