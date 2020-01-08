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
v = 5
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
screen.blit(load_image("Raul_r0.png"), (x, y))
raul = "Raul_r0.png"
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                y -= 10
                screen.fill((255, 255, 255))
                screen.blit(load_image(raul), (x, y))
            if event.key == 274:
                y += 10
                screen.fill((255, 255, 255))
                screen.blit(load_image(raul), (x, y))
            if event.key == 275:
                x += 10
                raul = "Raul_r0.png"
                screen.fill((255, 255, 255))
                screen.blit(load_image(raul), (x, y))
            if event.key == 276:
                x -= 10
                raul = "Raul_l0.png"
                screen.fill((255, 255, 255))
                screen.blit(load_image(raul), (x, y))
    if raul[6] == "0":
        raul = raul[:6] + '1' + raul[6 + 1:]
    elif raul[6] == "1":
        screen.blit(load_image(raul), (x, y))
        raul = raul[:6] + '2' + raul[6 + 1:]
    elif raul[6] == "2":
        screen.blit(load_image(raul), (x, y))
        raul = raul[:6] + '3' + raul[6 + 1:]
    elif raul[6] == "3":
        screen.blit(load_image(raul), (x, y))
        raul = raul[:6] + '4' + raul[6 + 1:]
    elif raul[6] == "4":
        screen.blit(load_image(raul), (x, y))
        raul = raul[:6] + '5' + raul[6 + 1:]
    elif raul[6] == "5":
        screen.blit(load_image(raul), (x, y))
        raul = raul[:6] + '0' + raul[6 + 1:]
    pygame.display.flip()
# завершение работы:
pygame.quit()