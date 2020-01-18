import os
from pygame.sprite import Sprite, collide_rect
from pygame.image import load
from pygame import Surface



MOVE_SPEED = 10
JUMP_POWER = 20

GRAVITY = 2

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = load(fullname).convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Snaryad:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.screen = screen
        self.facing = facing
        self.vel = 30 * facing

    def draw(self):
        self.screen.blit(load_image("bullet.png"), (self.x, self.y))


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
        # self.stayMarker = True
        self.begR = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]
        self.begL = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]
        # self.kadr = 1
        self.sChMarker = 1
        self.bChMarker = 1

    def update(self, left, right, up, shoot, platforms):
        # if self.kadr == 31:
        #     self.kadr = 1
        if self.kshoot == 10:
            self.flshoot = False
            self.kpshoot = 0
            self.kshoot = 0
        if self.kpshoot == 30:
            self.flshoot = True
        if self.stay:
            self.bChMarker = 1
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
            # print(self.stayL, '\n', self.stayR, '\n')
        else:
            self.sChMarker = 1
            self.stayR = ["Raul_r0.png", "Raul_r1.png", "Raul_r2.png", "Raul_r3.png", "Raul_r4.png", "Raul_r5.png"]
            self.stayL = ["Raul_l0.png", "Raul_l1.png", "Raul_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
            if self.bChMarker == 4:
                self.bChMarker = 1
            else:
                self.bChMarker += 1
            if self.viewSide == 'l' and self.bChMarker == 1:
                self.image = load("data/" + self.begL[0]).convert_alpha()
                self.begL.insert(4, self.begL[0])
                del self.begL[0]
            elif self.viewSide == 'r' and self.bChMarker == 1:
                self.image = load("data/" + self.begR[0]).convert_alpha()
                self.begR.insert(4, self.begR[0])
                del self.begR[0]

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

        if left and not right:
            self.viewSide = 'l'
            self.stay = False
            self.xvel = -MOVE_SPEED
            # self.image = load("data/Raul_l1b.png").convert_alpha()

        if right and not left:
            self.viewSide = 'r'
            self.stay = False
            self.xvel = MOVE_SPEED
            # self.image = load("data/Raul_r1b.png").convert_alpha()

        if not(left or right):
            self.stay = True
            self.xvel = 0
            # if self.viewSide == 'l':
            #     self.image = load("data/Raul_l0.png").convert_alpha()
            # else:
            #     self.image = load("data/Raul_r0.png").convert_alpha()

        # if not self.stay:
        #     self.stayMarker = False
        # else:
        #     self.stayMarker = True

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

            #if x2 + 48 >= bullet.x >= x2 and y2 + 80 >= bullet.y >= y2:
                # damage += 5
                # bullets.pop(bullets.index(bullet))
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