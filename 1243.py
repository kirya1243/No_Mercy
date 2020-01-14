import pygame
import os
import pygame.mouse


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


pygame.init()
size = 1200, 540
x1 = 5
y1 = 455
x2 = 1147
y2 = 455
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
flstay1 = 0
jumpCount1 = 8
animCount1 = 0

screen = pygame.display.set_mode(size)
screen.blit(load_image("bg.jpg"), (0, 0))
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
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 30 * facing

    def draw(self):
        screen.blit(load_image("bullet.png"), (self.x, self.y))


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

    screen.blit(load_image(raul), (x1, y1))
    screen.blit(load_image(dima), (x2, y2))
    screen.fill(pygame.Color('red'), pygame.Rect(10, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(10, 10, 200 - damage1, 20))
    screen.fill(pygame.Color('red'), pygame.Rect(990, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(990 + damage, 10, 200 - damage, 20))
    pygame.display.flip()


clock = pygame.time.Clock()
bullets = []
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if 1200 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

        if x2 + 48 >= bullet.x >= x2 and y2 + 80 >= bullet.y >= y2:
            damage += 25
            bullets.pop(bullets.index(bullet))

    if kshoot == 3:
        flshoot = False
        kpshoot = 0
        kshoot = 0
    if kpshoot == 10:
        flshoot = True
    if lastMove == "right":
        facing = 1
    elif lastMove == "left":
        facing = -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if lastMove == "right" and flshoot:
            bullets.append(Snaryad(x1 + 48, y1 + 32, facing))
            kshoot += 1
        elif lastMove == "left" and flshoot:
            bullets.append(Snaryad(x1, y1 + 32, facing))
            kshoot += 1

    if keys[pygame.K_d] and x1 < 1147:
        x1 += speed
        right = True
        left = False
        stay = False
        lastMove = "right"
        flstay = 0
    elif keys[pygame.K_a] and x1 > 5:
        x1 -= speed
        right = False
        left = True
        stay = False
        lastMove = "left"
        flstay = 0
    else:
        stay = True
        right = False
        left = False
        animCount = 0
    if not (isJump):
        if keys[pygame.K_w]:
            isJump = True
            # raul = raul[:6] + '0' + raul[6 + 1:]
            stay = False
    else:
        if jumpCount >= -8:
            if jumpCount < 0:
                y1 += (jumpCount ** 2) / 2
            else:
                y1 -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 8

    if keys[pygame.K_RIGHT] and x2 < 1147:
        x2 += speed
        right1 = True
        left1 = False
        stay1 = False
        flstay1 = 0
    elif keys[pygame.K_LEFT] and x2 > 5:
        x2 -= speed
        right1 = False
        left1 = True
        stay1 = False
        flstay1 = 0
    else:
        stay1 = True
        right1 = False
        left1 = False
        animCount1 = 0
    if not (isJump1):
        if keys[pygame.K_UP]:
            isJump1 = True
            # raul = raul[:6] + '0' + raul[6 + 1:]
            stay1 = False
    else:
        if jumpCount1 >= -8:
            if jumpCount1 < 0:
                y2 += (jumpCount1 ** 2) / 2
            else:
                y2 -= (jumpCount1 ** 2) / 2
            jumpCount1 -= 1
        else:
            isJump1 = False
            jumpCount1 = 8
    kpshoot += 1
    DrawWindow()
# завершение работы:
pygame.quit()
