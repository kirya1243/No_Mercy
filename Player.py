from pygame.sprite import Sprite, collide_rect
from pygame.image import load
from pygame import Surface

MOVE_SPEED = 8
JUMP_POWER = 10

GRAVITY = 0.4


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
        self.stayL = ["Raul_l0.png", "Raul_l1.png", "Raul_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
        # self.stayMarker = True
        self.begR = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]
        self.begL = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]
        # self.kadr = 1
        self.sChMarker = 1
        self.bChMarker = 1

    def update(self, left, right, up, platforms):
        # if self.kadr == 31:
        #     self.kadr = 1
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
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        # self.kadr += 1

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