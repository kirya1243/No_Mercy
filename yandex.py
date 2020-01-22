import pygame
import sys
import os
from random import choice

# import time
# start_time = time.time()


pygame.mixer.init()
# pygame.mixer_music.load('data/sounds/Black Magic.mp3')
# pygame.mixer_music.load('data/sounds/Corrupted Keep.mp3')
# pygame.mixer_music.load('data/sounds/menu.mp3')
setting = open('data/tools/music.ini', encoding='utf-8').read()
if setting == 'on':
    pygame.mixer_music.set_volume(0.1)
else:
    pygame.mixer_music.set_volume(0)


# sound_1_min = pygame.mixer.Sound('data/sounds/game/1_min.wav') НЕТ ЕЩЁ
# sound_1_min.set_volume(1) НЕТ ЕЩЁ
sound_5_min = pygame.mixer.Sound('data/sounds/game/5_min.wav')
sound_5_min.set_volume(1)
sound_button_press = pygame.mixer.Sound('data/sounds/game/button_press.wav')
sound_button_press.set_volume(1)
sound_button_press_game = pygame.mixer.Sound('data/sounds/game/button_press_game.wav')
sound_button_press_game.set_volume(1)
sound_button_press_map = pygame.mixer.Sound('data/sounds/game/button_press_map.wav')
sound_button_press_map.set_volume(1)
sound_start_game = pygame.mixer.Sound('data/sounds/game/start_game.wav')
sound_start_game.set_volume(1)
# sound_end_round = pygame.mixer.Sound('data/sounds/game/end_round.wav') НЕТ ЕЩЁ
# sound_end_round.set_volume(1) НЕТ ЕЩЁ
sound_start_round = pygame.mixer.Sound('data/sounds/game/start_round.wav')
sound_start_round.set_volume(1)

# sound_beg = pygame.mixer.Sound('data/sounds/hero/beg.wav')
# sound_beg.set_volume(1)
sound_change_weapon = pygame.mixer.Sound('data/sounds/hero/change_weapon.wav')
sound_change_weapon.set_volume(1)
# sound_death = pygame.mixer.Sound('data/sounds/hero/death.wav')
# sound_death.set_volume(1)
sound_hit = pygame.mixer.Sound('data/sounds/hero/hit.wav')
sound_hit.set_volume(0.3)
# sound_jump_down = pygame.mixer.Sound('data/sounds/hero/jump_down.wav')
# sound_jump_down.set_volume(1)
# sound_jump_up = pygame.mixer.Sound('data/sounds/hero/jump_up.wav')
# sound_jump_up.set_volume(1)
sound_railgun_shot = pygame.mixer.Sound('data/sounds/hero/railgun_shot.wav')
sound_railgun_shot.set_volume(0.3)
print(sound_railgun_shot.get_length())
sound_respawn = pygame.mixer.Sound('data/sounds/hero/respawn.wav')
sound_respawn.set_volume(1)
sound_rifle_shot = pygame.mixer.Sound('data/sounds/hero/rifle_shot.wav')
sound_rifle_shot.set_volume(0.3)

sound_gain_end = pygame.mixer.Sound('data/sounds/items/gain_end.wav')
sound_gain_end.set_volume(1)
sound_health_25_get = pygame.mixer.Sound('data/sounds/items/health_25_get.wav')
sound_health_25_get.set_volume(1)
sound_health_25_spawn = pygame.mixer.Sound('data/sounds/items/health_25_spawn.wav')
sound_health_25_spawn.set_volume(1)
sound_health_50_get = pygame.mixer.Sound('data/sounds/items/health_50_get.wav')
sound_health_50_get.set_volume(1)
sound_health_50_spawn = pygame.mixer.Sound('data/sounds/items/health_50_spawn.wav')
sound_health_50_spawn.set_volume(1)
sound_protection_get = pygame.mixer.Sound('data/sounds/items/protection_get.wav')
sound_protection_get.set_volume(1)
sound_protection_soon = pygame.mixer.Sound('data/sounds/items/protection_soon.wav')
sound_protection_soon.set_volume(1)
sound_protection_spawn = pygame.mixer.Sound('data/sounds/items/protection_spawn.wav')
sound_protection_spawn.set_volume(1)
sound_quad_get = pygame.mixer.Sound('data/sounds/items/quad_get.wav')
sound_quad_get.set_volume(1)
sound_quad_soon = pygame.mixer.Sound('data/sounds/items/quad_soon.wav')
sound_quad_soon.set_volume(1)
sound_quad_spawn = pygame.mixer.Sound('data/sounds/items/quad_spawn.wav')
sound_quad_spawn.set_volume(1)
sound_weapon_get = pygame.mixer.Sound('data/sounds/items/weapon_get.wav')
sound_weapon_get.set_volume(1)
sound_weapon_spawn = pygame.mixer.Sound('data/sounds/items/weapon_spawn.wav')
sound_weapon_spawn.set_volume(1)


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
    filename = "data/tools/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


pygame.init()
pygame.mouse.set_visible(False)
size = 1200, 540
screen = pygame.display.set_mode(size)
pygame.display.set_caption('INSTA KVEIK 2D')
pygame.display.set_icon(pygame.image.load("data/images/icon.jpg"))

sizem = 1200, 540
screenm = pygame.display.set_mode(sizem)


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


class Menu:
    def __init__(self, punkts=[0, 0, 'Punkt', (250, 250, 30), (250, 250, 30), 0]):
        self.punkts = punkts
        self.startlvl = False

    def render(self, holst, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                holst.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                holst.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        pygame.event.clear()
        done = True
        if not pygame.mixer_music.get_busy():
            setting = open('data/tools/music.ini', encoding='utf-8').read()
            if setting == 'on':
                pygame.mixer_music.set_volume(0.1)
            else:
                pygame.mixer_music.set_volume(0)
            pygame.mixer_music.load('data/sounds/menu.mp3')
            pygame.mixer_music.play(-1)
        font_menu = pygame.font.SysFont('Arial', 50)
        font_text = pygame.font.SysFont('Arial', 40)
        punkt = 0
        text1 = font_text.render("INSTA KVEIK 2D v1", True, (240, 0, 0))
        screenm.blit(text1, (442, 480))
        while done:
            # print('MENU', "-— %s seconds —-" % (time.time() - start_time))
            self.render(screenm, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sound_button_press.play()
                    pygame.time.wait(600)
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    # if e.key == pygame.K_ESCAPE:
                    #     sound_button_press.play()
                    #     pygame.time.wait(600)
                    #     sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                    if e.key == pygame.K_RETURN:
                        if punkt == 0:
                            sound_button_press_game.play()
                            pygame.time.wait(600)
                            screenm.blit(load_image("images/map.png"), (0, 0))
                            level.levelf()
                            done = False
                        elif punkt == 1:
                            sound_button_press.play()
                            pygame.time.wait(600)
                            pass  # ВИДЕО-ОБУЧАЛКА
                        elif punkt == 2:
                            sound_button_press.play()
                            pygame.time.wait(600)
                            sys.exit()
            screen.blit(screenm, (0, 0))
            pygame.display.flip()


punkts = [(465, 90, 'НАЧАТЬ БОЙ', (128, 128, 128), (255, 255, 255), 0),
          (485, 160, 'ОБУЧЕНИЕ', (128, 128, 128), (255, 255, 255), 1),
          (522, 230, 'ВЫЙТИ', (128, 128, 128), (255, 255, 255), 2)]
game = Menu(punkts)


class Level:
    def __init__(self, punktsmap=[0, 0, 'Punkt', (250, 250, 30), (250, 250, 30), 0]):
        self.punkts = punktsmap
        self.levelmap = ''

    def render(self, holst, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                holst.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                holst.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def levelf(self):
        pygame.event.clear()
        done = True
        karta1 = pygame.transform.scale(load_image("images/level_1.png"), (540, 243))
        karta2 = pygame.transform.scale(load_image("images/level_2.png"), (540, 243))
        screenm.blit(karta1, (40, 150))
        screenm.blit(karta2, (620, 150))
        font_text = pygame.font.SysFont('Arial', 30)
        text1 = font_text.render("Царство чёрной магии", 1, (128, 128, 128))
        screenm.blit(text1, (180, 410))
        text1 = font_text.render("Измерение обречённых", 1, (128, 128, 128))
        screenm.blit(text1, (750, 410))
        font_menu = pygame.font.SysFont('Arial', 70)
        punkt = 0
        while done:
            # print('LEVEL', "-— %s seconds —-" % (time.time() - start_time))
            self.render(screenm, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sound_button_press.play()
                    pygame.time.wait(600)
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sound_button_press.play()
                        pygame.time.wait(600)
                        screenm.blit(load_image("images/menu.png"), (0, 0))
                        game.menu()
                        done = False
                    if e.key == pygame.K_LEFT:
                        if punkt > 0:
                            sound_button_press_map.play()
                            pygame.time.wait(200)
                            pygame.event.clear()
                            punkt -= 1
                    if e.key == pygame.K_RIGHT:
                        if punkt < len(self.punkts) - 1:
                            sound_button_press_map.play()
                            pygame.time.wait(200)
                            pygame.event.clear()
                            punkt += 1
                    if e.key == pygame.K_RETURN:
                        if punkt == 0:
                            self.levelmap = 'level_1'
                            screenm.blit(load_image('images/level_1.png'), (0, 0))
                            pygame.mixer_music.stop()
                            sound_start_game.play()
                            pygame.time.wait(3000)
                            game.startlvl = True
                            done = False
                        elif punkt == 1:
                            self.levelmap = 'level_2'
                            screenm.blit(load_image('images/level_2.png'), (0, 0))
                            pygame.mixer_music.stop()
                            sound_start_game.play()
                            pygame.time.wait(3000)
                            game.startlvl = True
                            done = False
            screen.blit(screenm, (0, 0))
            pygame.display.flip()


punktsmap = [[100, 30, 'The Longest Yard', (128, 128, 128), (255, 255, 255), 0],
             [700, 30, 'Corrupted Keep', (128, 128, 128), (255, 255, 255), 1]]
level = Level(punktsmap)

sizep = 1200, 540
# screenp = pygame.display.set_mode(sizem)
screenm.blit(load_image("images/menu.png"), (0, 0))


class Pause:
    def __init__(self, punktsp=[0, 0, 'Punkt', (250, 250, 30), (250, 250, 30), 0]):
        self.punkts = punktsp
        self.startlvl = False

    def render(self, holst, font, num_punkt):
        screenm.blit(load_image("images/menu.png"), (0, 0))
        for i in self.punkts:
            if num_punkt == i[5]:
                holst.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                holst.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def pause(self):
        done = True
        if pygame.mixer.music.get_busy:
            pygame.mixer.music.pause()
        game.startlvl = False
        font_pause = pygame.font.SysFont('Arial', 50)
        font_text = pygame.font.SysFont('Arial', 40)
        text1 = font_text.render("ПАУЗА", True, (240, 0, 0))

        punkt = 0
        i = punktsp[1]
        setting = open('data/tools/music.ini', encoding='utf-8').read()
        if setting == 'on':
            i[2] = 'МУЗЫКА ВЫКЛ'
            i[0] = 450
        else:
            i[2] = 'МУЗЫКА ВКЛ'
            i[0] = 470
        while done:
            # print('PAUSE', "-— %s seconds —-" % (time.time() - start_time))
            self.render(screenm, font_pause, punkt)
            screenm.blit(text1, (543, 480))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sound_button_press.play()
                    pygame.time.wait(600)
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.mixer.music.unpause()
                        done = False
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                    if e.key == pygame.K_RETURN:
                        if punkt == 0:
                            pygame.mixer.music.unpause()
                            done = False
                        elif punkt == 1:
                            sound_button_press.play()
                            pygame.time.wait(500)
                            setting = open('data/tools/music.ini', encoding='utf-8').read()
                            if setting == 'on':
                                open('data/tools/music.ini', 'w').close()
                                setting = open('data/tools/music.ini', 'a', encoding='utf-8')
                                setting.write('off')
                                setting.close()
                                i[2] = 'МУЗЫКА ВКЛ'
                                i[0] = 470
                                self.render(screenm, font_pause, punkt)
                            else:
                                open('data/tools/music.ini', 'w').close()
                                setting = open('data/tools/music.ini', 'a', encoding='utf-8')
                                setting.write('on')
                                setting.close()
                                i[2] = 'МУЗЫКА ВЫКЛ'
                                i[0] = 450
                                self.render(screenm, font_pause, punkt)
                        elif punkt == 2:
                            pygame.mixer_music.stop()
                            sound_button_press.play()
                            pygame.time.wait(600)
                            screenm.blit(load_image("images/menu.png"), (0, 0))
                            game.startlvl = True
                            game.menu()
                            done = False
            screen.blit(screenm, (0, 0))
            pygame.display.flip()


punktsp = [[455, 80, 'ПРОДОЛЖИТЬ', (128, 128, 128), (255, 255, 255), 0],
           [470, 150, 'МУЗЫКА ВКЛ', (128, 128, 128), (255, 255, 255), 1],
           [439, 220, 'ПОКИНУТЬ БОЙ', (128, 128, 128), (255, 255, 255), 2]]
pause = Pause(punktsp)

weapons = ['RIFLE']
weapons1 = ['RIFLE']


class Raul(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48, 80))
        self.image = pygame.image.load("data/images/Raul/rifle/Raul_r0.png").convert_alpha()
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False
        self.stay = True
        self.viewSide = 'r'
        self.stayR = ["Raul_r0.png", "Raul_r1.png", "Raul_r2.png", "Raul_r3.png", "Raul_r4.png", "Raul_r5.png"]
        self.stayL = ["Raul_l0.png", "Raul_l1.png", "v_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
        self.begR = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]
        self.begL = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]
        self.sChMarker = 1
        self.rChMarker = 1
        self.lChMarker = 1

    def update(self, left, right, up, platforms):
        if left and not right:
            self.viewSide = 'l'
            self.stay = False
        if right and not left:
            self.viewSide = 'r'
            self.stay = False
        if self.stay:
            self.rChMarker = 1
            self.lChMarker = 1
            self.begR = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]
            self.begL = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]
            if self.sChMarker == 6:
                self.sChMarker = 1
            else:
                self.sChMarker += 1
            if (self.viewSide == 'l' and self.sChMarker == 1) and weapons[0] == 'RIFLE':
                self.image = pygame.image.load("data/images/Raul/rifle/" + self.stayL[0]).convert_alpha()
                self.stayL.insert(6, self.stayL[0])
                del self.stayL[0]
            elif (self.viewSide == 'l' and self.sChMarker == 1) and weapons[0] == 'RAIL':
                self.image = pygame.image.load("data/images/Raul/railgun/" + self.stayL[0]).convert_alpha()
                self.stayL.insert(6, self.stayL[0])
                del self.stayL[0]
            elif (self.viewSide == 'r' and self.sChMarker == 1) and weapons[0] == 'RIFLE':
                self.image = pygame.image.load("data/images/Raul/rifle/" + self.stayR[0]).convert_alpha()
                self.stayR.insert(6, self.stayR[0])
                del self.stayR[0]
            elif (self.viewSide == 'r' and self.sChMarker == 1) and weapons[0] == 'RAIL':
                self.image = pygame.image.load("data/images/Raul/railgun/" + self.stayR[0]).convert_alpha()
                self.stayR.insert(6, self.stayR[0])
                del self.stayR[0]
        else:
            self.sChMarker = 1
            self.stayR = ["Raul_r0.png", "Raul_r1.png", "Raul_r2.png", "Raul_r3.png", "Raul_r4.png", "Raul_r5.png"]
            self.stayL = ["Raul_l0.png", "Raul_l1.png", "Raul_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
            if self.viewSide == 'l':
                self.rChMarker = 1
                if self.lChMarker == 1:
                    if weapons[0] == 'RIFLE':
                        self.image = pygame.image.load("data/images/Raul/rifle/" + self.begL[0]).convert_alpha()
                    else:
                        self.image = pygame.image.load("data/images/Raul/railgun/" + self.begL[0]).convert_alpha()
                    self.begL.insert(4, self.begL[0])
                    del self.begL[0]
                if self.lChMarker == 4:
                    self.lChMarker = 1
                else:
                    self.lChMarker += 1
            elif self.viewSide == 'r':
                self.lChMarker = 1
                if self.rChMarker == 1:
                    if weapons[0] == 'RIFLE':
                        self.image = pygame.image.load("data/images/Raul/rifle/" + self.begR[0]).convert_alpha()
                    else:
                        self.image = pygame.image.load("data/images/Raul/railgun/" + self.begR[0]).convert_alpha()
                    self.begR.insert(4, self.begR[0])
                    del self.begR[0]
                if self.rChMarker == 4:
                    self.rChMarker = 1
                else:
                    self.rChMarker += 1
            if left and not right:
                self.xvel = -MOVE_SPEED
            elif right and not left:
                self.xvel = MOVE_SPEED

        if not (left or right):
            self.stay = True
            self.xvel = 0
        if up:
            if self.onGround:
                # sound_jump_up.fadeout()
                # if sound_jump_up.get_num_channels() < 1:
                #     sound_jump_up.play()
                # print(sound_jump_up.get_raw())
                self.yvel = -JUMP_POWER
        if not self.onGround:
            self.yvel += GRAVITY
        self.onGround = False
        if not (not (self.rect.x + self.xvel > 0) or not (1152 > self.rect.x + self.xvel)):
            self.rect.x += self.xvel
        elif self.rect.x <= 10:
            self.rect.x = 0
        elif self.rect.x >= 1142:
            self.rect.x = 1152
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for pl1 in platforms:
            if pygame.sprite.collide_rect(self, pl1):
                if xvel > 0:
                    self.rect.right = pl1.rect.left
                if xvel < 0:
                    self.rect.left = pl1.rect.right
                if yvel > 0:
                    self.rect.bottom = pl1.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl1.rect.bottom
                    self.yvel = 0


class Dima(pygame.sprite.Sprite):
    def __init__(self, x1, y1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48, 80))
        self.image = pygame.image.load("data/images/Dima/rifle/Dima_l0.png").convert_alpha()
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
        self.onGround = False
        self.stay = True
        self.viewSide = 'l'
        self.stayR = ["Dima_r0.png", "Dima_r1.png", "Dima_r2.png", "Dima_r3.png", "Dima_r4.png", "Dima_r5.png"]
        self.stayL = ["Dima_l0.png", "Dima_l1.png", "Dima_l2.png", "Dima_l3.png", "Dima_l4.png", "Dima_l5.png"]
        self.begR = ["Dima_r1b.png", "Dima_r2b.png", "Dima_r3b.png", "Dima_r2b.png"]
        self.begL = ["Dima_l1b.png", "Dima_l2b.png", "Dima_l3b.png", "Dima_l2b.png"]
        self.sChMarker = 1
        self.rChMarker = 1
        self.lChMarker = 1

    def update(self, left, right, up, platforms):
        if left and not right:
            self.viewSide = 'l'
            self.stay = False
        if right and not left:
            self.viewSide = 'r'
            self.stay = False
        if self.stay:
            self.rChMarker = 1
            self.lChMarker = 1
            self.begR = ["Dima_r1b.png", "Dima_r2b.png", "Dima_r3b.png", "Dima_r2b.png"]
            self.begL = ["Dima_l1b.png", "Dima_l2b.png", "Dima_l3b.png", "Dima_l2b.png"]
            if self.sChMarker == 6:
                self.sChMarker = 1
            else:
                self.sChMarker += 1
            if (self.viewSide == 'l' and self.sChMarker == 1) and weapons1[0] == 'RIFLE':
                self.image = pygame.image.load("data/images/Dima/rifle/" + self.stayL[0]).convert_alpha()
                self.stayL.insert(6, self.stayL[0])
                del self.stayL[0]
            elif (self.viewSide == 'l' and self.sChMarker == 1) and weapons1[0] == 'RAIL':
                self.image = pygame.image.load("data/images/Dima/railgun/" + self.stayL[0]).convert_alpha()
                self.stayL.insert(6, self.stayL[0])
                del self.stayL[0]
            elif (self.viewSide == 'r' and self.sChMarker == 1) and weapons1[0] == 'RIFLE':
                self.image = pygame.image.load("data/images/Dima/rifle/" + self.stayR[0]).convert_alpha()
                self.stayR.insert(6, self.stayR[0])
                del self.stayR[0]
            elif (self.viewSide == 'r' and self.sChMarker == 1) and weapons1[0] == 'RAIL':
                self.image = pygame.image.load("data/images/Dima/railgun/" + self.stayR[0]).convert_alpha()
                self.stayR.insert(6, self.stayR[0])
                del self.stayR[0]
        else:
            self.sChMarker = 1
            self.stayR = ["Dima_r0.png", "Dima_r1.png", "Dima_r2.png", "Dima_r3.png", "Dima_r4.png", "Dima_r5.png"]
            self.stayL = ["Dima_l0.png", "Dima_l1.png", "Dima_l2.png", "Dima_l3.png", "Dima_l4.png", "Dima_l5.png"]
            if self.viewSide == 'l':
                self.rChMarker = 1
                if self.lChMarker == 1:
                    if weapons1[0] == 'RIFLE':
                        self.image = pygame.image.load("data/images/Dima/rifle/" + self.begL[0]).convert_alpha()
                    else:
                        self.image = pygame.image.load("data/images/Dima/railgun/" + self.begL[0]).convert_alpha()
                    self.begL.insert(4, self.begL[0])
                    del self.begL[0]
                if self.lChMarker == 4:
                    self.lChMarker = 1
                else:
                    self.lChMarker += 1
            elif self.viewSide == 'r':
                self.lChMarker = 1
                if self.rChMarker == 1:
                    if weapons1[0] == 'RIFLE':
                        self.image = pygame.image.load("data/images/Dima/rifle/" + self.begR[0]).convert_alpha()
                    else:
                        self.image = pygame.image.load("data/images/Dima/railgun/" + self.begR[0]).convert_alpha()
                    self.begR.insert(4, self.begR[0])
                    del self.begR[0]
                if self.rChMarker == 4:
                    self.rChMarker = 1
                else:
                    self.rChMarker += 1
            if left and not right:
                self.xvel = -MOVE_SPEED
            elif right and not left:
                self.xvel = MOVE_SPEED

        if not (left or right):
            self.stay = True
            self.xvel = 0
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
        if not self.onGround:
            self.yvel += GRAVITY
        self.onGround = False
        if not (not (self.rect.x + self.xvel > 0) or not (1152 > self.rect.x + self.xvel)):
            self.rect.x += self.xvel
        elif self.rect.x <= 10:
            self.rect.x = 0
        elif self.rect.x >= 1142:
            self.rect.x = 1152
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for pl1 in platforms:
            if pygame.sprite.collide_rect(self, pl1):
                if xvel > 0:
                    self.rect.right = pl1.rect.left
                if xvel < 0:
                    self.rect.left = pl1.rect.right
                if yvel > 0:
                    self.rect.bottom = pl1.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl1.rect.bottom
                    self.yvel = 0


hero = Raul(5, 520)
hero1 = Dima(1147, 520)
leftP = rightP = upP = False
leftP1 = rightP1 = upP1 = False
gains = []
gains1 = []
bullets = []
bullets1 = []

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
sprite_group.add(hero1)
platforms = []

MOVE_SPEED = 10
JUMP_POWER = 20
GRAVITY = 2
speed = 10
hp1 = 200
hp = 200
counter, text = 180, '3:00'.rjust(3)

flshoot = True
kshoot = 0
kpshoot = 0
railshoot = 0
flshoot1 = True
kshoot1 = 0
kpshoot1 = 0
railshoot1 = 0
flhealth = False


class Snaryad:
    def __init__(self, x1, y1, facing0):
        self.x = x1
        self.y = y1
        self.facing = facing0
        self.vel = 30 * facing0

    def draw(self):
        screen.blit(load_image("images/bullet.png"), (self.x, self.y))


class Snaryad1:
    def __init__(self, x1, y1, facing2):
        self.x = x1
        self.y = y1
        self.facing1 = facing2
        self.vel1 = 30 * facing2

    def draw(self):
        screen.blit(load_image("images/bullet1.png"), (self.x, self.y))


class SnaryadRail:
    def __init__(self, x1, y1, facing0):
        self.x = x1
        self.y = y1
        self.facing = facing0
        self.vel = 70 * facing0

    def draw(self):
        screen.blit(load_image("images/bullet_rail.png"), (self.x, self.y))


punkts = [(470, 90, 'НОВЫЙ БОЙ', (128, 128, 128), (255, 255, 255), 0),
          (485, 160, 'ОБУЧЕНИЕ', (128, 128, 128), (255, 255, 255), 1),
          (522, 230, 'ВЫЙТИ', (128, 128, 128), (255, 255, 255), 2)]
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
font1 = pygame.font.SysFont('Consolas', 50)
font2 = pygame.font.SysFont('Consolas', 700)
font3 = pygame.font.SysFont('Consolas', 25)
# itemss = [[30, 290, 30, 30, "images/25HP.png", False, 10, 0],
#           [1140, 290, 30, 30, "images/25HP.png", False, 10, 1],
#           [30, 90, 30, 30, "images/50HP.png", False, 10, 2],
#           [1140, 90, 30, 30, "images/50HP.png", False, 10, 3]]
itemss = []
spawns = []
railshot_draw = []


def DrawWindow():
    screen.blit(load_image('images/' + level.levelmap + '.png'), (0, 0))

    for bullet in bullets:
        bullet.draw()

    for bullet1 in bullets1:
        bullet1.draw()

    screen.blit(load_image("images/Raul/head.png"), (0, 5))
    screen.blit(load_image("images/Dima/head.png"), (1170, 5))
    screen.fill(pygame.Color('red'), pygame.Rect(35, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(35, 10, hp, 20))
    if hp > 0:
        if hp >= 155:
            screen.blit(font3.render(str(hp), True, (255, 255, 255)), (190, 9))
        else:
            screen.blit(font3.render(str(hp), True, (255, 255, 255)), (hp + 35, 9))
    elif hp <= 0:
        screen.blit(font3.render('ВОЗРАЖДЕНИЕ', True, (255, 255, 255)), (40, 8))

    screen.fill(pygame.Color('red'), pygame.Rect(965, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(965 + 200 - hp1, 10, hp1, 20))
    if hp1 > 0:
        if hp1 >= 155:
            screen.blit(font3.render(str(hp1), True, (255, 255, 255)), (967, 9))
        else:
            screen.blit(font3.render(str(hp1), True, (255, 255, 255)), (1120 - hp1, 9))
    elif hp1 <= 0:
        screen.blit(font3.render('ВОЗРАЖДЕНИЕ', True, (255, 255, 255)), (987, 8))

    # screen.blit(load_image("images/spawn.png"), (3, 500))
    # screen.blit(load_image("images/spawn.png"), (1137, 500))
    for i in spawns:
        screen.blit(load_image('images/spawn.png'), (i[0], i[1]))

    if len(gains) > 0:
        for i in gains:
            if i[0] == 'QUAD':
                gain = pygame.transform.scale(load_image("images/quad.png"), (20, 20))
            else:
                gain = pygame.transform.scale(load_image("images/protection.png"), (20, 20))
            screen.blit(gain, (240, 10))
            screen.blit(font3.render(str(i[1]), True, (255, 255, 255)), (265, 8))

    if len(gains1) > 0:
        for i in gains1:
            if i[0] == 'QUAD':
                gain = pygame.transform.scale(load_image("images/quad.png"), (20, 20))
            else:
                gain = pygame.transform.scale(load_image("images/protection.png"), (20, 20))
            screen.blit(gain, (905, 10))
            screen.blit(font3.render(str(i[1]), True, (255, 255, 255)), (930, 8))

    if len(railshot_draw) > 0:
        for i in railshot_draw:
            if i[2] > 0:
                if i[1] == -1:
                    pygame.draw.line(screen, (136, 6, 206), (0, i[3]), (i[0], i[3]), 5)
                elif i[1] == 1:
                    pygame.draw.line(screen, (136, 6, 206), (i[0], i[3]), (1200, i[3]), 5)

    sprite_group.draw(screen)

    for i in itemss:
        if i[5]:
            screen.blit(load_image(i[4]), (i[0], i[1]))

    if text.split(':')[0] == '0':
        screen.blit(font1.render(text, True, (255, 0, 0)), (555, 10))
    else:
        screen.blit(font1.render(text, True, (255, 255, 255)), (555, 10))

    pygame.display.flip()


# itemss = [[30, 290, 30, 30, "images/25HP.png", False, 10, 0],
#           [1140, 290, 30, 30, "images/25HP.png", False, 10, 1],
#           [30, 90, 30, 30, "images/50HP.png", False, 10, 2],
#           [1140, 90, 30, 30, "images/50HP.png", False, 10, 3]]
game.menu()
x, y = 0, 0
for row in load_level(level.levelmap + '.txt'):
    for col in row:
        if col == '#':
            pl = PlatformMetal(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        elif col == '%':
            pl = PlatformStone(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        elif col == '0':
            pl = PlatformHidden(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        elif col == '+':
            itemss.append([x + 15, y - 20, 30, 30, "images/50HP.png", False, 15, '50HP'])
        elif col == '-':
            itemss.append([x + 15, y - 20, 30, 30, "images/25HP.png", False, 10, '25HP'])
        elif col == 'r':
            itemss.append([x, y - 20, 41, 14, "images/railgun_r.png", False, 20, 'RAIL'])
        elif col == 'l':
            itemss.append([x, y - 20, 41, 14, "images/railgun_l.png", False, 20, 'RAIL'])
        elif col == 'g':
            itemss.append([x, y - 25, 40, 40, "images/quad.png", False, 80, 'GAIN', 'QUAD'])
        elif col == 'S':
            spawns.append([x, y])
        x += 20
    y += 20
    x = 0

running = True
while running:
    clock.tick(25)
    if game.startlvl:
        if level.levelmap == 'level_1':
            pygame.mixer_music.load('data/sounds/Black Magic.mp3')
        else:
            pygame.mixer_music.load('data/sounds/Corrupted Keep.mp3')
        setting = open('data/tools/music.ini', encoding='utf-8').read()
        if setting == 'on':
            pygame.mixer_music.set_volume(0.2)
        else:
            pygame.mixer_music.set_volume(0)
        pygame.mixer_music.play()
        sound_start_round.play()
        for i in range(9):
            screenm.blit(load_image('images/' + level.levelmap + '.png'), (0, 0))
            if i == 6:
                screenm.blit(font2.render('3', True, (255, 255, 255)), (400, -30))
            elif i == 7:
                screenm.blit(font2.render('2', True, (255, 255, 255)), (400, -30))
            elif i == 8:
                screenm.blit(font2.render('1', True, (255, 255, 255)), (400, -30))
            pygame.display.flip()
            pygame.time.delay(1130)
        sprite_group.empty()
        kshoot, kshoot1 = 0, 0
        sound_respawn.play()
        platforms = []
        x, y = 0, 0
        itemss = []
        spawns = []
        for row in load_level(level.levelmap + '.txt'):
            for col in row:
                if col == '#':
                    pl = PlatformMetal(x, y)
                    sprite_group.add(pl)
                    platforms.append(pl)
                elif col == '%':
                    pl = PlatformStone(x, y)
                    sprite_group.add(pl)
                    platforms.append(pl)
                elif col == '0':
                    pl = PlatformHidden(x, y)
                    sprite_group.add(pl)
                    platforms.append(pl)
                elif col == '+':
                    itemss.append([x + 15, y - 20, 30, 30, "images/50HP.png", False, 15, '50HP'])
                elif col == '-':
                    itemss.append([x + 15, y - 20, 30, 30, "images/25HP.png", False, 10, '25HP'])
                elif col == 'r':
                    itemss.append([x, y - 20, 41, 14, "images/railgun_r.png", False, 20, 'RAIL'])
                elif col == 'l':
                    itemss.append([x, y - 20, 41, 14, "images/railgun_l.png", False, 20, 'RAIL'])
                elif col == 'g':
                    itemss.append([x, y - 25, 40, 40, "images/quad.png", False, 80, 'GAIN', 'QUAD'])
                elif col == 'S':
                    spawns.append([x, y])
                x += 20
            y += 20
            x = 0

        hero = Raul(5, 520)
        hero1 = Dima(1147, 520)
        sprite_group.add(hero)
        sprite_group.add(hero1)
        leftP = rightP = upP = False
        leftP1 = rightP1 = upP1 = False
        hp1 = 200
        hp = 200
        counter, text = 180, '3:00'.rjust(3)
        weapons = ['RIFLE']
        weapons1 = ['RIFLE']
        gains = []
        gains1 = []
        bullets = []
        bullets1 = []
        railshot_draw = []
        game.startlvl = False
        hero.update(leftP, rightP, upP, platforms)
        hero1.update(leftP1, rightP1, upP1, platforms)
        pygame.event.clear()
    if not game.startlvl:
        setting = open('data/tools/music.ini', encoding='utf-8').read()
        if setting == 'on':
            pygame.mixer_music.set_volume(0.2)
        else:
            pygame.mixer_music.set_volume(0)
        # print(clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sound_button_press.play()
                pygame.time.wait(600)
                running = False
            if event.type == pygame.USEREVENT:
                counter -= 1
                # itemss = [[30, 290, 30, 30, "images/25HP.png", False, 10, 0],
                #           [1140, 290, 30, 30, "images/25HP.png", False, 10, 1],
                #           [30, 90, 30, 30, "images/50HP.png", False, 10, 2],
                #           [1140, 90, 30, 30, "images/50HP.png", False, 10, 3]]
                # elif col == '+':
                #     itemss.append([x + 15, y - 20, 30, 30, "images/50HP.png", False, 10, '50HP'])
                # elif col == '-':
                #     itemss.append([x + 15, y - 20, 30, 30, "images/25HP.png", False, 10, '25HP'])
                # elif col == 'r':
                #     itemss.append([x, y - 20, 41, 14, "images/railgun_r.png", False, 30, 'RAIL'])
                # elif col == 'l':
                #     itemss.append([x, y - 20, 41, 14, "images/railgun_l.png", False, 30, 'RAIL'])
                # elif col == 'g':
                #     itemss.append([x, y - 20, 41, 16, "images/rifle_r.png", False, 80, 'GAIN'])
                if counter >= 0:
                    if len(gains) > 0:
                        for i in gains:
                            i[1] -= 1
                            if i[1] == 10:
                                sound_gain_end.play()
                            if i[1] == 0:
                                gains.remove(i)
                    if len(gains1) > 0:
                        for i in gains1:
                            i[1] -= 1
                            if i[1] == 10:
                                sound_gain_end.play()
                            if i[1] == 0:
                                gains1.remove(i)
                    if len(railshot_draw) > 0:
                        for i in railshot_draw:
                            i[2] -= 1
                            if i[2] == 0:
                                railshot_draw.remove(i)
                    for i in itemss:
                        if not i[5] and i[7] != 'GAIN':
                            i[6] -= 1
                            if i[6] == 0:
                                i[5] = True
                                if i[7] == '50HP':
                                    i[6] = 30
                                    sound_health_50_spawn.play()
                                elif i[7] == '25HP':
                                    i[6] = 15
                                    sound_health_25_spawn.play()
                                elif i[7] == 'RAIL':
                                    i[6] = 40
                                    sound_weapon_spawn.play()
                        elif i[7] == 'GAIN':
                            i[6] -= 1
                            if i[6] == 0:
                                if i[8] == 'QUAD':
                                    sound_quad_spawn.play()
                                else:
                                    sound_protection_spawn.play()
                                i[5] = True
                            elif i[6] == 10:
                                if i[8] == 'QUAD':
                                    sound_quad_soon.play()
                                else:
                                    sound_protection_soon.play()
                            elif i[6] == -40:
                                i[6] = 40
                                i[5] = False
                                if i[8] == 'QUAD':
                                    i[8] = 'PROT'
                                    i[4] = 'images/protection.png'
                                else:
                                    i[8] = 'QUAD'
                                    i[4] = 'images/quad.png'
                    seconds = counter
                    minutes = 0
                    while seconds >= 60:
                        seconds -= 60
                        minutes += 1
                    if len(str(seconds)) == 1:
                        seconds = '0' + str(seconds)
                    round_time = '{}:{}'.format(minutes, seconds)
                    text = round_time.rjust(3)
                    if round_time == '5:00':
                        sound_5_min.play()
                    # if round_time == '1:00':
                    #     sound_1_min.play()
                    if railshoot != 0:
                        railshoot -= 1
                    if railshoot1 != 0:
                        railshoot1 -= 1
                    if hp < 0:
                        hp = 0
                    if hp1 < 0:
                        hp1 = 0

                if counter == 0:
                    pygame.mixer_music.stop()
                    # sound_1_min.stop() НЕТ ЕЩЁ
                    sound_5_min.stop()
                    sound_button_press.stop()
                    sound_button_press_game.stop()
                    sound_button_press_map.stop()
                    sound_start_game.stop()
                    # sound_end_round.stop() НЕТ ЕЩЁ
                    sound_start_round.stop()
                    # sound_beg.stop()
                    sound_change_weapon.stop()
                    # sound_death.stop()
                    sound_hit.stop()
                    # sound_jump_down.stop()
                    # sound_jump_up.stop()
                    # sound_railgun_shot.stop()
                    sound_respawn.stop()
                    sound_rifle_shot.stop()
                    sound_gain_end.stop()
                    sound_health_25_get.stop()
                    sound_health_25_spawn.stop()
                    sound_health_50_get.stop()
                    sound_health_50_spawn.stop()
                    sound_protection_get.stop()
                    sound_protection_soon.stop()
                    sound_protection_spawn.stop()
                    sound_quad_get.stop()
                    sound_quad_soon.stop()
                    sound_quad_spawn.stop()
                    sound_weapon_get.stop()
                    sound_weapon_spawn.stop()
                    screenm.blit(load_image("images/menu.png"), (0, 0))
                    game.menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # sound_1_min.stop() НЕТ ЕЩЁ
                    sound_5_min.stop()
                    sound_button_press.stop()
                    sound_button_press_game.stop()
                    sound_button_press_map.stop()
                    sound_start_game.stop()
                    # sound_end_round.stop() НЕТ ЕЩЁ
                    sound_start_round.stop()
                    # sound_beg.stop()
                    sound_change_weapon.stop()
                    # sound_death.stop()
                    sound_hit.stop()
                    # sound_jump_down.stop()
                    # sound_jump_up.stop()
                    # sound_railgun_shot.stop()
                    sound_respawn.stop()
                    sound_rifle_shot.stop()
                    sound_gain_end.stop()
                    sound_health_25_get.stop()
                    sound_health_25_spawn.stop()
                    sound_health_50_get.stop()
                    sound_health_50_spawn.stop()
                    sound_protection_get.stop()
                    sound_protection_soon.stop()
                    sound_protection_spawn.stop()
                    sound_quad_get.stop()
                    sound_quad_soon.stop()
                    sound_quad_spawn.stop()
                    sound_weapon_get.stop()
                    sound_weapon_spawn.stop()
                    screenm.blit(load_image("images/menu.png"), (0, 0))
                    pause.pause()
                if event.key == pygame.K_e:
                    if len(weapons) > 1:
                        sound_change_weapon.play()
                        weapons.reverse()
                if event.key == pygame.K_a:
                    leftP = True
                if event.key == pygame.K_d:
                    rightP = True
                if event.key == pygame.K_w:
                    upP = True
                if event.key == pygame.K_LEFT:
                    leftP1 = True
                if event.key == pygame.K_RIGHT:
                    rightP1 = True
                if event.key == pygame.K_UP:
                    upP1 = True
                if event.key == pygame.K_KP1:
                    if len(weapons1) > 1:
                        sound_change_weapon.play()
                        weapons1.reverse()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    leftP = False
                if event.key == pygame.K_d:
                    rightP = False
                if event.key == pygame.K_w:
                    upP = False
                if event.key == pygame.K_LEFT:
                    leftP1 = False
                if event.key == pygame.K_RIGHT:
                    rightP1 = False
                if event.key == pygame.K_UP:
                    upP1 = False

        for bullet in bullets:
            if 1300 > bullet.x > -100:
                if bullet.__class__.__name__ != 'SnaryadRail':
                    bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

            if bullet.__class__.__name__ != 'SnaryadRail':
                if hero1.rect.x + 48 >= bullet.x >= hero1.rect.x and hero1.rect.y + 80 >= bullet.y >= hero1.rect.y:
                    sound_hit.play()
                    damage = 6
                    if len(gains) > 0:
                        for i in gains:
                            if i[0] == 'QUAD':
                                damage = damage * 4
                    if len(gains1) > 0:
                        for i in gains1:
                            if i[0] == 'PROT':
                                damage = damage // 3
                    if str(hp1 - damage)[0] == '-':
                        hp1 = 0
                    else:
                        hp1 -= damage
                    bullets.pop(bullets.index(bullet))
            else:
                do_hit = 0
                if bullet.facing == -1:
                    for i in range(-100, bullet.x):
                        if hero1.rect.x == i and hero1.rect.y + 80 >= bullet.y >= hero1.rect.y:
                            do_hit = 1
                elif bullet.facing == 1:
                    for i in range(bullet.x, 1300):
                        if hero1.rect.x == i and hero1.rect.y + 80 >= bullet.y >= hero1.rect.y:
                            do_hit = 1
                if do_hit == 1:
                    sound_hit.play()
                    damage = 69
                    if len(gains) > 0:
                        for i in gains:
                            if i[0] == 'QUAD':
                                damage = damage * 4
                    if len(gains1) > 0:
                        for i in gains1:
                            if i[0] == 'PROT':
                                damage = damage // 3
                    if str(hp1 - damage)[0] == '-':
                        hp1 = 0
                    else:
                        hp1 -= damage
                bullets.pop(bullets.index(bullet))
                railshot_draw.append([bullet.x, bullet.facing, 2, bullet.y])

        if kshoot == 7:
            flshoot = False
            kpshoot = 0
            kshoot = 0
        if kpshoot == 30:
            flshoot = True
        if hero.viewSide == "r":
            facing = 1
        elif hero.viewSide == "l":
            facing = -1
        if hero1.viewSide == "r":
            facing1 = 1
        elif hero1.viewSide == "l":
            facing1 = -1
        if counter % 10 == 0:
            flhealth = True

        for bullet1 in bullets1:
            if 1300 > bullet1.x > -100:
                if bullet1.__class__.__name__ != 'SnaryadRail':
                    bullet1.x += bullet1.vel1
                # elif bullet1.__class__.__name__ == 'SnaryadRail':
                #     bullet1.x += bullet1.vel
            else:
                bullets1.pop(bullets1.index(bullet1))

            if bullet1.__class__.__name__ != 'SnaryadRail':
                if hero.rect.x + 48 >= bullet1.x >= hero.rect.x and hero.rect.y + 80 >= bullet1.y >= hero.rect.y:
                    sound_hit.play()
                    damage = 6
                    if len(gains1) > 0:
                        for i in gains1:
                            if i[0] == 'QUAD':
                                damage = damage * 4
                    if len(gains) > 0:
                        for i in gains:
                            if i[0] == 'PROT':
                                damage = damage // 3
                    if str(hp - damage)[0] == '-':
                        hp = 0
                    else:
                        hp -= damage
                    bullets1.pop(bullets1.index(bullet1))
            else:
                do_hit = 0
                if bullet1.facing == -1:
                    for i in range(-100, bullet1.x):
                        if hero.rect.x == i and hero.rect.y + 80 >= bullet1.y >= hero.rect.y:
                            do_hit = 1
                elif bullet1.facing == 1:
                    for i in range(bullet1.x, 1300):
                        if hero.rect.x == i and hero.rect.y + 80 >= bullet1.y >= hero.rect.y:
                            do_hit = 1
                if do_hit == 1:
                    sound_hit.play()
                    damage = 69
                    if len(gains1) > 0:
                        for i in gains1:
                            if i[0] == 'QUAD':
                                damage = damage * 4
                    if len(gains) > 0:
                        for i in gains:
                            if i[0] == 'PROT':
                                damage = damage // 3
                    if str(hp - damage)[0] == '-':
                        hp = 0
                    else:
                        hp -= damage
                bullets1.pop(bullets1.index(bullet1))
                railshot_draw.append([bullet1.x, bullet1.facing, 2, bullet1.y])

        if kshoot1 == 7:
            flshoot1 = False
            kpshoot1 = 0
            kshoot1 = 0
        if kpshoot1 == 30:
            flshoot1 = True

        for item in itemss:
            if (hero.rect.x + 48 >= item[0] >= hero.rect.x and hero.rect.y + 80 >= item[1] >= hero.rect.y) and item[5]:
                if item[7] == '25HP':
                    if hp <= 175:
                        sound_health_25_get.play()
                        hp += 25
                        item[5] = False
                    elif hp < 200 and hp > 175:
                        sound_health_25_get.play()
                        hp = 200
                        item[5] = False
                elif item[7] == '50HP':
                    if hp <= 150:
                        sound_health_50_get.play()
                        hp += 50
                        item[5] = False
                    elif hp < 200 and hp > 150:
                        sound_health_50_get.play()
                        hp = 200
                        item[5] = False
                elif item[7] == 'RAIL':
                    if len(weapons) == 1:
                        sound_weapon_get.play()
                        weapons.append('RAIL')
                        item[5] = False
                elif item[7] == 'GAIN':
                    if item[8] == 'QUAD':
                        sound_quad_get.play()
                        gains.append(['QUAD', 30])
                        item[5] = False
                    elif item[8] == 'PROT':
                        sound_protection_get.play()
                        gains.append(['PROT', 30])
                        item[5] = False

            elif (hero1.rect.x + 48 >= item[0] >= hero1.rect.x and hero1.rect.y + 80 >= item[1] >= hero1.rect.y) and item[5]:
                if item[7] == '25HP':
                    if hp1 <= 175:
                        sound_health_25_get.play()
                        hp1 += 25
                        item[5] = False
                    elif hp1 < 200 and hp1 > 175:
                        sound_health_25_get.play()
                        hp1 = 200
                        item[5] = False
                elif item[7] == '50HP':
                    if hp1 <= 150:
                        sound_health_50_get.play()
                        hp1 += 50
                        item[5] = False
                    elif hp1 < 200 and hp1 > 150:
                        sound_health_50_get.play()
                        hp1 = 200
                        item[5] = False
                elif item[7] == 'RAIL':
                    if len(weapons1) == 1:
                        sound_weapon_get.play()
                        weapons1.append('RAIL')
                        item[5] = False
                elif item[7] == 'GAIN':
                    if item[8] == 'QUAD':
                        gains1.append(['QUAD', 30])
                        item[5] = False
                    elif item[8] == 'PROT':
                        gains1.append(['PROT', 30])
                        item[5] = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if hero.viewSide == "r" and flshoot:
                if weapons[0] == 'RIFLE':
                    sound_rifle_shot.play()
                    bullets.append(Snaryad(hero.rect.x + 48, hero.rect.y + 32, facing))
                    kshoot += 1
                else:
                    if railshoot == 0:
                        sound_railgun_shot.play()
                        railshoot = 2
                        bullets.append(SnaryadRail(hero.rect.x + 48, hero.rect.y + 32, facing))
            elif hero.viewSide == "l" and flshoot:
                if weapons[0] == 'RIFLE':
                    sound_rifle_shot.play()
                    bullets.append(Snaryad(hero.rect.x - 5, hero.rect.y + 32, facing))
                    kshoot += 1
                else:
                    if railshoot == 0:
                        sound_railgun_shot.play()
                        railshoot = 2
                        bullets.append(SnaryadRail(hero.rect.x - 5, hero.rect.y + 32, facing))

        if keys[pygame.K_KP0]:
            if hero1.viewSide == "r" and flshoot1:
                if weapons1[0] == 'RIFLE':
                    sound_rifle_shot.play()
                    bullets1.append(Snaryad1(hero1.rect.x + 48, hero1.rect.y + 32, facing1))
                    kshoot1 += 1
                else:
                    if railshoot1 == 0:
                        sound_railgun_shot.play()
                        railshoot1 = 2
                        bullets1.append(SnaryadRail(hero1.rect.x + 48, hero1.rect.y + 32, facing1))

            elif hero1.viewSide == "l" and flshoot1:
                if weapons1[0] == 'RIFLE':
                    sound_rifle_shot.play()
                    bullets1.append(Snaryad1(hero1.rect.x - 5, hero1.rect.y + 32, facing1))
                    kshoot1 += 1
                else:
                    if railshoot1 == 0:
                        sound_railgun_shot.play()
                        railshoot1 = 2
                        bullets1.append(SnaryadRail(hero1.rect.x - 5, hero1.rect.y + 32, facing1))

        if keys[pygame.K_F1]:
            hp1 = 200
            hp = 200

        kpshoot += 1
        kpshoot1 += 1
        if not game.startlvl:
            DrawWindow()
        hero.update(leftP, rightP, upP, platforms)
        hero1.update(leftP1, rightP1, upP1, platforms)
        for bullet in bullets:
            bullet.draw()
        for bullet in bullets1:
            bullet.draw()
# завершение работы:
pygame.quit()
