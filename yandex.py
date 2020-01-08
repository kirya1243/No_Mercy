import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


size = width, height = 960, 540
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)

all_sprites = pygame.sprite.Group()
player_image = load_image("creature.png")
player = pygame.sprite.Sprite(all_sprites)
player.image = player_image
player.rect = player.image.get_rect()
x, y = 0, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            y -= 10
        elif key[pygame.K_DOWN]:
            y += 10
        elif key[pygame.K_LEFT]:
            x -= 10
        elif key[pygame.K_RIGHT]:
            x += 10
        player.rect.x = x
        player.rect.y = y
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
