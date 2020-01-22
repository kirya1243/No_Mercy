import pygame
from random import choice


class PlatformMetal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.texture = pygame.image.load('data/images/texture_metal.png')
        self.angles = [90, 180, 270, 360]
        self.angle = choice(self.angles)
        self.texture_rotate = pygame.transform.rotate(self.texture, self.angle)
        self.image = self.texture_rotate.subsurface((0, 0, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PlatformStone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.texture = pygame.image.load('data/images/texture_stone.jpg')
        self.angles = [90, 180, 270, 360]
        self.angle = choice(self.angles)
        self.texture_rotate = pygame.transform.rotate(self.texture, self.angle)
        self.image = self.texture_rotate.subsurface((0, 0, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PlatformHidden(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/images/hidden.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y