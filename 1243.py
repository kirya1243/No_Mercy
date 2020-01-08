import pygame
import os
import pygame.mouse


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = 960, 540
x = 0
y = 460
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
screen.blit(load_image("Raul.png"), (x, y))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                y -= 10
                screen.fill((255, 255, 255))
                screen.blit(load_image("Raul.png"), (x, y))
            if event.key == 274:
                y += 10
                screen.fill((255, 255, 255))
                screen.blit(load_image("Raul.png"), (x, y))
            if event.key == 275:
                x += 10
                screen.fill((255, 255, 255))
                screen.blit(load_image("Raul.png"), (x, y))
            if event.key == 276:
                x -= 10
                screen.fill((255, 255, 255))
                screen.blit(load_image("Raul.png"), (x, y))
    pygame.display.flip()
# завершение работы:
pygame.quit()