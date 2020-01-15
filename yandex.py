import pygame
import os
import pygame.mouse
from Player import Player
from Platforms import Platform


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


def make_level(level, platform):
    x, y = 0, 0
    for row in level:
        for col in row:
            if col == '#':
                screen.blit(platform.img, (x, y))
            x += 30
        x = 0
        y += 30


pygame.init()
size = 1200, 540
screen = pygame.display.set_mode(size)
screen.blit(load_image("bg.jpg"), (0, 0))

hero = Player(55, 55)
leftP = rightP = upP = False

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
        x += 30
    y += 30
    x = 0


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


class Snaryad():
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 30 * facing

    def draw(self):
        screen.blit(load_image("bullet.png"), (self.x, self.y))


class Snaryad1():
    def __init__(self, x, y, facing1):
        self.x = x
        self.y = y
        self.facing1 = facing1
        self.vel1 = 30 * facing1

    def draw(self):
        screen.blit(load_image("bullet1.png"), (self.x, self.y))


def DrawWindow():
    global animCount, raul, kdvij, flstay, left, right, stay
    global animCount1, dima, kdvij1, flstay1, left1, right1, stay1
    screen.blit(load_image("bg.jpg"), (0, 0))

    if animCount + 1 >= 15:
        animCount = 0

    if right:
        raul = wright[animCount % 3]
        animCount += 1

    if left:
        raul = wleft[animCount % 3]
        animCount += 1

    if stay:
        if flstay == 0:
            raul = raul[:6] + '0.png'
            flstay = 1
        if raul[6] == "0" and kdvij % 3 == 0:
            raul = raul[:6] + '1' + raul[6 + 1:]
        elif raul[6] == "1" and kdvij % 3 == 0:
            raul = raul[:6] + '2' + raul[6 + 1:]
        elif raul[6] == "2" and kdvij % 3 == 0:
            raul = raul[:6] + '3' + raul[6 + 1:]
        elif raul[6] == "3" and kdvij % 3 == 0:
            raul = raul[:6] + '4' + raul[6 + 1:]
        elif raul[6] == "4" and kdvij % 3 == 0:
            raul = raul[:6] + '5' + raul[6 + 1:]
        elif raul[6] == "5" and kdvij % 3 == 0:
            raul = raul[:6] + '0' + raul[6 + 1:]
        kdvij += 1

    if isJump:
        if raul[5] == "r":
            raul = "Raul_r0.png"
        else:
            raul = "Raul_l0.png"

    if animCount1 + 1 >= 15:
        animCount1 = 0

    if right1:
        dima = wright[animCount1 % 3]
        animCount1 += 1

    if left1:
        dima = wleft[animCount1 % 3]
        animCount1 += 1

    if stay1:
        if flstay1 == 0:
            dima = dima[:6] + '0.png'
            flstay1 = 1
        if dima[6] == "0" and kdvij1 % 3 == 0:
            dima = dima[:6] + '1' + dima[6 + 1:]
        elif dima[6] == "1" and kdvij1 % 3 == 0:
            dima = dima[:6] + '2' + dima[6 + 1:]
        elif dima[6] == "2" and kdvij1 % 3 == 0:
            dima = dima[:6] + '3' + dima[6 + 1:]
        elif dima[6] == "3" and kdvij1 % 3 == 0:
            dima = dima[:6] + '4' + dima[6 + 1:]
        elif dima[6] == "4" and kdvij1 % 3 == 0:
            dima = dima[:6] + '5' + dima[6 + 1:]
        elif dima[6] == "5" and kdvij1 % 3 == 0:
            dima = dima[:6] + '0' + dima[6 + 1:]
        kdvij1 += 1

    if isJump1:
        if dima[5] == "r":
            dima = "Raul_r0.png"
        else:
            dima = "Raul_l0.png"

    for bullet in bullets:
        bullet.draw()

    for bullet1 in bullets1:
        bullet1.draw()

    screen.blit(load_image(raul), (x1, y1))
    screen.blit(load_image(dima), (x2, y2))
    screen.fill(pygame.Color('red'), pygame.Rect(10, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(10, 10, 200 - damage1, 20))
    screen.fill(pygame.Color('red'), pygame.Rect(990, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(990 + damage, 10, 200 - damage, 20))

    hero.update(leftP, rightP, upP, platfroms)
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
            if event.key == pygame.K_LEFT:
                leftP = True
            if event.key == pygame.K_RIGHT:
                rightP = True
            if event.key == pygame.K_UP:
                upP = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftP = False
            if event.key == pygame.K_RIGHT:
                rightP = False
            if event.key == pygame.K_UP:
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
    if lastMove == "right":
        facing = 1
    elif lastMove == "left":
        facing = -1

    for bullet1 in bullets1:
        if 1300 > bullet1.x > -100:
            bullet1.x += bullet1.vel1
        else:
            bullets1.pop(bullets1.index(bullet1))

        if x1 + 48 >= bullet1.x >= x1 and y1 + 80 >= bullet1.y >= y1:
            damage1 += 5
            bullets1.pop(bullets1.index(bullet1))

    if kshoot1 == 10:
        flshoot1 = False
        kpshoot1 = 0
        kshoot1 = 0
    if kpshoot1 == 30:
        flshoot1 = True
    if lastMove1 == "right":
        facing1 = 1
    elif lastMove1 == "left":
        facing1 = -1

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     if lastMove == "right" and flshoot:
    #         bullets.append(Snaryad(x1 + 48, y1 + 32, facing))
    #         kshoot += 1
    #     elif lastMove == "left" and flshoot:
    #         bullets.append(Snaryad(x1, y1 + 32, facing))
    #         kshoot += 1
    #
    # if keys[pygame.K_KP0]:
    #     if lastMove1 == "right" and flshoot1:
    #         bullets1.append(Snaryad1(x2 + 48, y2 + 32, facing1))
    #         kshoot1 += 1
    #     elif lastMove1 == "left" and flshoot1:
    #         bullets1.append(Snaryad1(x2, y2 + 32, facing1))
    #         kshoot1 += 1
    #
    # if keys[pygame.K_F1]:
    #     damage = 0
    #     damage1 = 0
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
# завершение работы:
pygame.quit()
