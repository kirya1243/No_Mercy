from pygame.sprite import Sprite
from pygame.image import load
# from random import randint


class PlatformMetal(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)

        self.texture = load('data/images/texture_metal.png')
        # self.rx = randint(0, 880)
        # self.ry = randint(0, 880)
        self.image = self.texture.subsurface((0, 0, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PlatformStone(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)

        self.texture = load('data/images/texture_stone.jpg')
        # self.rx = randint(0, 880)
        # self.ry = randint(0, 880)
        self.image = self.texture.subsurface((0, 0, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PlatformHidden(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('data/images/hidden.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y