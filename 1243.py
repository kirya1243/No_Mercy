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
size = 960, 540
x = 5
y = 455
speed = 10
kdvij = 0

isJump = False
stay = True
jumpCount = 8

screen = pygame.display.set_mode(size)
screen.blit(load_image("bg.jpg"), (0, 0))
raul = "Raul_r0.png"


def DrawWindow():
    screen.blit(load_image("bg.jpg"), (0, 0))
    screen.blit(load_image(raul), (x, y))
    pygame.display.flip()
# clock = pygame.time.Clock()
running = True
while running:
    # clock.tick(20)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < 907:
        x += speed
        raul = "Raul_r0.png"
        stay = False
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 5:
        x -= speed
        raul = "Raul_l0.png"
        stay = False
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            raul = raul[:6] + '0' + raul[6 + 1:]
            stay = False
    else:
        if jumpCount >= -8:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            stay = True
            jumpCount = 8

    if stay:
        if raul[6] == "0" and kdvij % 2 == 0:
            raul = raul[:6] + '1' + raul[6 + 1:]
        elif raul[6] == "1" and kdvij % 2 == 0:
            raul = raul[:6] + '2' + raul[6 + 1:]
        elif raul[6] == "2" and kdvij % 2 == 0:
            raul = raul[:6] + '3' + raul[6 + 1:]
        elif raul[6] == "3" and kdvij % 2 == 0:
            raul = raul[:6] + '4' + raul[6 + 1:]
        elif raul[6] == "4" and kdvij % 2 == 0:
            raul = raul[:6] + '5' + raul[6 + 1:]
        elif raul[6] == "5" and kdvij % 2 == 0:
            raul = raul[:6] + '0' + raul[6 + 1:]
        kdvij += 1

    stay = True
    DrawWindow()
# завершение работы:
pygame.quit()