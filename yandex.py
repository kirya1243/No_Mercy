import pygame  # подключаем библиотеки
import sys
import os
from random import choice


pygame.mixer.init()  # подключение музыки
pygame.mixer_music.load('data/sounds/Black Magic.mp3')
pygame.mixer_music.load('data/sounds/Corrupted Keep.mp3')
pygame.mixer_music.load('data/sounds/menu.mp3')
setting = open('data/tools/music.ini', encoding='utf-8').read()
if setting == 'on':
    pygame.mixer_music.set_volume(0.1)
else:
    pygame.mixer_music.set_volume(0)


sound_1_min = pygame.mixer.Sound('data/sounds/game/1_min.wav')
sound_1_min.set_volume(1)
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
sound_end_round = pygame.mixer.Sound('data/sounds/game/end_round.wav')
sound_end_round.set_volume(1)
sound_start_round = pygame.mixer.Sound('data/sounds/game/start_round.wav')
sound_start_round.set_volume(1)

sound_change_weapon = pygame.mixer.Sound('data/sounds/hero/change_weapon.wav')
sound_change_weapon.set_volume(1)
sound_death = pygame.mixer.Sound('data/sounds/hero/death.wav')
sound_death.set_volume(1)
sound_hit = pygame.mixer.Sound('data/sounds/hero/hit.wav')
sound_hit.set_volume(0.3)
sound_railgun_shot = pygame.mixer.Sound('data/sounds/hero/railgun_shot.wav')
sound_railgun_shot.set_volume(0.3)
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


def load_image(name, colorkey=None):  # функция загрузки фото
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):  # функция загрузки фото
    filename = "data/tools/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


pygame.init()
pygame.mouse.set_visible(False)  # делаем курсор невидимым
size = 1200, 540  # устанавливаем размеры игрового поля и создаём его
screen = pygame.display.set_mode(size)
pygame.display.set_caption('INSTA KVEIK 2D')  # меняем название проекта и иконку
pygame.display.set_icon(pygame.image.load("data/images/icon.jpg"))

sizem = 1200, 540  # создаём основное окно в котором мы будем работать
screenm = pygame.display.set_mode(sizem)


class PlatformMetal(pygame.sprite.Sprite):  # 3 класса создающих спрайты платформ
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


class Menu:  # класс главного меню игры
    def __init__(self, punkts=[0, 0, 'Punkt', (250, 250, 30), (250, 250, 30), 0]):
        self.punkts = punkts  # список пунктов меню
        self.startlvl = False  # переменная обозначающая начало игры

    def render(self, holst, font, num_punkt):  # функция реализующая изменение цвета выбранного пункта
        for i in self.punkts:
            if num_punkt == i[5]:
                holst.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                holst.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):  # функция реализующая само меню
        pygame.event.clear()
        done = True
        if not pygame.mixer_music.get_busy():  # музыка в главном меню
            setting = open('data/tools/music.ini', encoding='utf-8').read()
            if setting == 'on':
                pygame.mixer_music.set_volume(0.1)
            else:
                pygame.mixer_music.set_volume(0)
            pygame.mixer_music.load('data/sounds/menu.mp3')
            pygame.mixer_music.play(-1)
        font_menu = pygame.font.SysFont('Arial', 50)  # шрифты для текстов
        font_text = pygame.font.SysFont('Arial', 40)
        punkt = 0  # изначально выбран первый пункт в меню
        text1 = font_text.render("INSTA KVEIK 2D v1", True, (230, 5, 5))  # название игры печатаемое снизу
        screenm.blit(text1, (457, 480))
        while done:
            self.render(screenm, font_menu, punkt)  # вызов функции подсветки пункта
            pygame.event.clear(pygame.K_UP, pygame.K_DOWN)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:  # закрытие окна при нажатии на крестик в правом верхнем углу
                    sound_button_press.play()
                    pygame.time.delay(600)
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:  # переключение между пунктами вверх
                        if punkt > 0:  # если пункт не первый
                            punkt -= 1
                    if e.key == pygame.K_DOWN:  # переключение между пунктами вниз
                        if punkt < len(self.punkts) - 1:  # если пункт не последний
                            punkt += 1
                    if e.key == pygame.K_RETURN:  # при нажатии ENTER открываем выбранный пункт
                        if punkt == 0:  # если это первый пункт
                            sound_button_press_game.play()
                            pygame.time.delay(600)
                            screenm.blit(load_image("images/map.png"), (0, 0))  # открытие окна с ывбором карты
                            level.levelf()  # открытие окна с ывбором карты
                            done = False  # закрытие меню
                        elif punkt == 1:  # если это второй пункт
                            sound_button_press.play()
                            pygame.time.delay(600)
                            os.startfile(os.getcwd() + '/data/tools/instruction.mp4')  # включение обучающего видео
                        elif punkt == 2:  # если это последний пункт
                            sound_button_press.play()
                            pygame.time.delay(600)
                            sys.exit()  # закрытие окна
            screen.blit(screenm, (0, 0))
            pygame.display.flip()


punkts = [(465, 90, 'НАЧАТЬ БОЙ', (128, 128, 128), (255, 255, 255), 0),  # создаём список пунктов меню
          (485, 160, 'ОБУЧЕНИЕ', (128, 128, 128), (255, 255, 255), 1),
          (522, 230, 'ВЫЙТИ', (128, 128, 128), (255, 255, 255), 2)]
game = Menu(punkts)


class Level:  # класс выбора карты
    def __init__(self, punktsmap=[0, 0, 'Punkt', (250, 250, 30), (250, 250, 30), 0]):
        self.punkts = punktsmap  # список пунктов для окна с выбором карты
        self.levelmap = ''  # название выбранной карты

    def render(self, holst, font, num_punkt):  # функция реализующая изменение цвета выбранного пункта
        for i in self.punkts:
            if num_punkt == i[5]:
                holst.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                holst.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def levelf(self):  # функция реализующая сам выбор карты
        pygame.event.clear()
        done = True
        karta1 = pygame.transform.scale(load_image("images/level_1.png"), (540, 243))  # создаём переменные содержащие
        karta2 = pygame.transform.scale(load_image("images/level_2.png"), (540, 243))  # миниатюрные фоны уровней
        screenm.blit(karta1, (40, 150))   # выводим их на экран
        screenm.blit(karta2, (620, 150))
        font_text = pygame.font.SysFont('Arial', 30)  # шрифты для текстов
        font_menu = pygame.font.SysFont('Arial', 70)
        text1 = font_text.render("Царство чёрной магии", 1, (128, 128, 128))  # создание надписей под фонами карт
        text1 = font_text.render("Измерение обречённых", 1, (128, 128, 128))
        screenm.blit(text1, (750, 410))  # вывод этих надписей на экран
        screenm.blit(text1, (180, 410))
        punkt = 0  # изначально выбран левый пункт
        while done:
            self.render(screenm, font_menu, punkt)  # вызов функции подсветки пункта
            for e in pygame.event.get():
                if e.type == pygame.QUIT:  # закрытие окна при нажатии на крестик в правом верхнем углу
                    sound_button_press.play()
                    pygame.time.delay(600)
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:  # возвращение в главное меню при нажатии кнлавиши ESCAPE
                        sound_button_press.play()
                        pygame.time.delay(600)
                        screenm.blit(load_image("images/menu.png"), (0, 0))
                        game.menu()
                        done = False  # закрытие окна с выбором карты
                    if e.key == pygame.K_LEFT:  # переключение между пунктами влево
                        if punkt > 0:  # если это не левый пункт
                            sound_button_press_map.play()
                            pygame.time.delay(200)
                            pygame.event.clear()
                            punkt -= 1
                    if e.key == pygame.K_RIGHT:  # переключение между пунктами вправо
                        if punkt < len(self.punkts) - 1:  # если это не правый пункт
                            sound_button_press_map.play()
                            pygame.time.delay(200)
                            pygame.event.clear()
                            punkt += 1
                    if e.key == pygame.K_RETURN:  # при нажатии ENTER выбираем эту карту
                        if punkt == 0:  # если это левая карта
                            self.levelmap = 'level_1'  # изменим название переменной на 'level_1'
                            screenm.blit(load_image('images/level_1.png'), (0, 0))  # загружаем картинку левой карты
                            pygame.mixer_music.stop()
                            sound_start_game.play()
                            pygame.time.delay(3000)
                            game.startlvl = True  # начинаем игру
                            done = False  # закрываем окно с выбором карты
                        elif punkt == 1:  # если это правая карта
                            self.levelmap = 'level_2'  # изменим название переменной на 'level_2'
                            screenm.blit(load_image('images/level_2.png'), (0, 0))  # загружаем картинку правой карты
                            pygame.mixer_music.stop()
                            sound_start_game.play()
                            pygame.time.delay(3000)
                            game.startlvl = True  # начинаем игру
                            done = False  # закрываем окно с выбором карты
            screen.blit(screenm, (0, 0))
            pygame.display.flip()


punktsmap = [[100, 30, 'The Longest Yard', (128, 128, 128), (255, 255, 255), 0],  # создаём список пунктов для окна с
             [700, 30, 'Corrupted Keep', (128, 128, 128), (255, 255, 255), 1]]    # выбором карты
level = Level(punktsmap)


class End:  # класс вывода результатов игры
    def __init__(self, punktsend=[0, 0, 'Punkt', (250, 250, 30), (250, 250, 30), 0]):
        self.punkts = punktsend  # список пунктов для окна итогов

    def render(self, holst, font, num_punkt):  # функция реализующая изменение цвета выбранного пункта
        for i in self.punkts:
            if num_punkt == i[5]:
                holst.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                holst.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def endf(self):  # функция реализующая сам вывод итогов
        pygame.event.clear()
        done = True
        font_score = pygame.font.Font('data/tools/MangaMaster.ttf', 350)  # шрифты для текстов
        font_end = pygame.font.SysFont('Arial', 40)
        font_end1 = pygame.font.SysFont('Arial', 60)
        text1 = font_score.render(str(raulscore), 1, (200, 0, 0))  # вывод результатов первого игрока
        screenm.blit(text1, (70, 50))
        text1 = font_score.render(str(dimascore), 1, (0, 0, 200))  # вывод результатов второго игрока
        screenm.blit(text1, (870, 50))
        if dimascore < raulscore:  # вывод текста при победе первого игрока
            text1 = font_end.render('ПЕРВЫЙ', 1, (220, 0, 0))
            screenm.blit(text1, (525, 90))
            text2 = font_end.render('ИГРОК', 1, (220, 0, 0))
            screenm.blit(text2, (543, 160))
            text3 = font_end.render('ПОБЕДИЛ', 1, (220, 0, 0))
            screenm.blit(text3, (517, 230))
        elif dimascore > raulscore:  # вывод текста при победе второго игрока
            text1 = font_end.render('ВТОРОЙ', 1, (0, 0, 255))
            screenm.blit(text1, (525, 90))
            text2 = font_end.render('ИГРОК', 1, (0, 0, 255))
            screenm.blit(text2, (543, 160))
            text3 = font_end.render('ПОБЕДИЛ', 1, (0, 0, 255))
            screenm.blit(text3, (517, 230))
        else:  # вывод текста при ничьей
            text2 = font_end1.render('НИЧЬЯ', 1, (0, 0, 255))
            screenm.blit(text2, (515, 160))
        punkt = 0  # изначально выбран левый пункт
        while done:
            self.render(screenm, font_end, punkt)  # вызов функции подсветки пункта

            for e in pygame.event.get():
                if e.type == pygame.QUIT:  # закрытие окна при нажатии на крестик в правом верхнем углу
                    sound_button_press.play()
                    pygame.time.delay(600)
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:  # переключение между пунктами влево
                        if punkt > 0:  # если это не левый пункт
                            sound_button_press_map.play()
                            pygame.time.delay(200)
                            pygame.event.clear()
                            punkt -= 1
                    if e.key == pygame.K_RIGHT:  # переключение между пунктами влево
                        if punkt < len(self.punkts) - 1:  # если это не правый пункт
                            sound_button_press_map.play()
                            pygame.time.delay(200)
                            pygame.event.clear()
                            punkt += 1
                    if e.key == pygame.K_RETURN:  # при нажатии ENTER открываем выбранный пункт
                        if punkt == 0:  # открываем меню
                            pygame.mixer_music.stop()
                            screenm.blit(load_image("images/menu.png"), (0, 0))
                            game.menu()
                            done = False  # закрытие окна итогов
                        elif punkt == 1:  # открываем окно с выбором карты
                            pygame.mixer_music.stop()
                            sound_button_press_game.play()
                            pygame.time.delay(600)
                            screenm.blit(load_image("images/map.png"), (0, 0))
                            level.levelf()
                            done = False  # закрытие окна итогов
            screen.blit(screenm, (0, 0))
            pygame.display.flip()


punktsend = [[50, 40, 'В ГЛАВНОЕ МЕНЮ', (128, 128, 128), (255, 255, 255), 0],  # создаём список пунктов для окна итогов
             [900, 40, 'РЕВАНШ', (128, 128, 128), (255, 255, 255), 1]]
end = End(punktsend)
screenm.blit(load_image("images/menu.png"), (0, 0))


class Pause:  # класс паузы
    def __init__(self, punktsp=[0, 0, 'Punkt', (250, 250, 30), (250, 250, 30), 0]):
        self.punkts = punktsp  # список пунктов для окна паузы

    def render(self, holst, font, num_punkt):  # функция реализующая изменение цвета выбранного пункта
        screenm.blit(load_image("images/menu.png"), (0, 0))
        for i in self.punkts:
            if num_punkt == i[5]:
                holst.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                holst.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def pause(self):  # функция реализующая саму паузу
        done = True
        if pygame.mixer.music.get_busy:
            pygame.mixer.music.pause()
        game.startlvl = False  # остановка игры
        font_pause = pygame.font.SysFont('Arial', 50)  # шрифты для текстов
        font_text = pygame.font.SysFont('Arial', 40)
        text1 = font_text.render("ПАУЗА", True, (230, 5, 5))

        punkt = 0  # изначально выбран первый пункт
        i = punktsp[1]  # работа со вторым пунктом
        setting = open('data/tools/music.ini', encoding='utf-8').read()
        if setting == 'on':  # проверяем включена сейчас музыка или нет
            i[2] = 'МУЗЫКА ВЫКЛ'  # меняем надпися в меню паузы
            i[0] = 450
        else:
            i[2] = 'МУЗЫКА ВКЛ'  # меняем надпися в меню паузы
            i[0] = 470
        while done:
            self.render(screenm, font_pause, punkt)  # вызов функции подсветки пункта
            screenm.blit(text1, (543, 480))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:  # закрытие окна при нажатии на крестик в правом верхнем углу
                    sound_button_press.play()
                    pygame.time.delay(600)
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:  # возвращение в игру при нажатии кнлавиши ESCAPE
                        pygame.mixer.music.unpause()
                        done = False  # закрытие окна паузы
                    if e.key == pygame.K_UP:  # переключение между пунктами вверх
                        if punkt > 0:  # если пункт не первый
                            punkt -= 1
                    if e.key == pygame.K_DOWN:  # переключение между пунктами вниз
                        if punkt < len(self.punkts) - 1:  # если пункт не последний
                            punkt += 1
                    if e.key == pygame.K_RETURN:  # при нажатии ENTER открываем выбранный пункт
                        if punkt == 0:  # возвращение в игру
                            pygame.mixer.music.unpause()
                            done = False  # закрытие окна паузы
                        elif punkt == 1:
                            sound_button_press.play()
                            pygame.time.delay(500)
                            setting = open('data/tools/music.ini', encoding='utf-8').read()
                            if setting == 'on':  # переключаем музыку(ВКЛ/ВЫКЛ) и меняем надпись пункта на обратный
                                open('data/tools/music.ini', 'w').close()  # например, если музыка сейчас включена, то
                                setting = open('data/tools/music.ini', 'a', encoding='utf-8')  # на кнопке будет
                                setting.write('off')  # написано ВЫКЛ, то есть при нажатии на кнопку мы выключам музыку
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
                        elif punkt == 2:  # открываем меню
                            pygame.mixer_music.stop()
                            sound_button_press.play()
                            pygame.time.delay(600)
                            screenm.blit(load_image("images/menu.png"), (0, 0))
                            game.startlvl = True  # возвращаем все переменные в начальное состояние
                            game.menu()
                            done = False  # закрытие окна паузы
            screen.blit(screenm, (0, 0))
            pygame.display.flip()


punktsp = [[455, 80, 'ПРОДОЛЖИТЬ', (128, 128, 128), (255, 255, 255), 0],  # создаём список пунктов для окна паузы
           [470, 150, 'МУЗЫКА ВКЛ', (128, 128, 128), (255, 255, 255), 1],
           [439, 220, 'ПОКИНУТЬ БОЙ', (128, 128, 128), (255, 255, 255), 2]]
pause = Pause(punktsp)

weapons = ['RIFLE']  # список оружий первого игрока
weapons1 = ['RIFLE']  # список оружий второго игрока


class Raul(pygame.sprite.Sprite):  # спрайт первого игрока
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48, 80))
        self.image = pygame.image.load("data/images/Raul/rifle/Raul_r0.png").convert_alpha()
        self.xvel = 0  # скорость по х
        self.yvel = 0  # скорость по у
        self.rect = self.image.get_rect()
        self.rect.x = x  # координаты игрока
        self.rect.y = y
        self.onGround = False  # стоит ли персонаж на земле/платформе
        self.stay = True  # стоит ли персонаж
        self.viewSide = 'r'  # в какую сторону смотрит персонаж
        self.stayR = ["Raul_r0.png", "Raul_r1.png", "Raul_r2.png", "Raul_r3.png", "Raul_r4.png", "Raul_r5.png"]
        self.stayL = ["Raul_l0.png", "Raul_l1.png", "Raul_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
        self.begR = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]  # списки изображений для анимаций
        self.begL = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]
        self.sChMarker = 1  # маркер анимации дыхания
        self.rChMarker = 1  # маркер анимации бега направо
        self.lChMarker = 1  # маркер анимации бега налево

    def update(self, left, right, up, platforms):  # функция обновления состояния игрока
        if left and not right:  # в какую сторону сейчас смотрит
            self.viewSide = 'l'
            self.stay = False
        if right and not left:
            self.viewSide = 'r'
            self.stay = False
        if self.stay:  # если стоит
            self.rChMarker = 1
            self.lChMarker = 1
            self.begR = ["Raul_r1b.png", "Raul_r2b.png", "Raul_r3b.png", "Raul_r2b.png"]
            self.begL = ["Raul_l1b.png", "Raul_l2b.png", "Raul_l3b.png", "Raul_l2b.png"]
            if (self.viewSide == 'l' and self.sChMarker == 1) and weapons[0] == 'RIFLE':  # проверка стороны, в
                # которую повёрнут игрок, маркера анимации и выбранного оружия
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
        else:  # реализация анимации бега
            self.sChMarker = 1
            self.stayR = ["Raul_r0.png", "Raul_r1.png", "Raul_r2.png", "Raul_r3.png", "Raul_r4.png", "Raul_r5.png"]
            self.stayL = ["Raul_l0.png", "Raul_l1.png", "Raul_l2.png", "Raul_l3.png", "Raul_l4.png", "Raul_l5.png"]
            if self.viewSide == 'l':  # в какую сторону сейчас смотрит
                self.rChMarker = 1
                if self.lChMarker == 1:
                    if weapons[0] == 'RIFLE':  # проверка оружия
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
                self.xvel = -MOVE_SPEED  # движение влево
            elif right and not left:
                self.xvel = MOVE_SPEED  # движение вправо

        if not (left or right):
            self.stay = True
            self.xvel = 0
        if up:  # прыжок
            if self.onGround:
                self.yvel = -JUMP_POWER
        if not self.onGround:  # учитываем силу гравитации для более реалистичного прыжка
            self.yvel += GRAVITY
        self.onGround = False
        if not (not (self.rect.x + self.xvel > 0) or not (1152 > self.rect.x + self.xvel)):  # проыеряем что игрок не
            self.rect.x += self.xvel  # выходит за пределы карты
        elif self.rect.x <= 10:
            self.rect.x = 0
        elif self.rect.x >= 1142:
            self.rect.x = 1152
        self.collide(self.xvel, 0, platforms)  # вызов функции для проверки на столкновения по х
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)  # вызов функции для проверки на столкновения по у

    def collide(self, xvel, yvel, platforms):  # проверка на столкновения
        for pl1 in platforms:
            if pygame.sprite.collide_rect(self, pl1):
                if xvel > 0:  # справа
                    self.rect.right = pl1.rect.left
                if xvel < 0:  # слева
                    self.rect.left = pl1.rect.right
                if yvel > 0:  # снизу
                    self.rect.bottom = pl1.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:  # сверху
                    self.rect.top = pl1.rect.bottom
                    self.yvel = 0


class Dima(pygame.sprite.Sprite):  # спрайт второго игрока(класс симметричен классу первого, различны только изображения
    # для анимации и переменная отвечающая за сторону в которую изначально смотрит игрок
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


hero = Raul(5, 520)  # инициализируем первого игрока
hero1 = Dima(1147, 520)  # инициализируем второго игрока
leftP, rightP, upP = False, False, False
leftP1, rightP1, upP1 = False, False, False
gains = []  # списки улучшений и пуль каждого игрока
gains1 = []
bullets = []
bullets1 = []

sprite_group = pygame.sprite.Group()  # создаём группу спрайтов
sprite_group.add(hero)  # добавляем первого и второго игрока
sprite_group.add(hero1)
platforms = []  # список платформ

MOVE_SPEED = 10  # скорость передвижения игроков
JUMP_POWER = 20  # скорость прыжка
GRAVITY = 2  # сили гравитации
hp1 = 200  # количество жизней каждого игрока
hp = 200
counter, text = 300, '5:00'.rjust(3)  # счётчик времени

flshoot = True  # флаги разрешения стрельбы
kshoot = 0  # счётчик выпущинных патронов
kpshoot = 0  # таймер перезарядки
railshoot = 0  # переменная перезарядки для снайперской винтовки
flshoot1 = True
kshoot1 = 0
kpshoot1 = 0
railshoot1 = 0


class Snaryad:  # классы пуль, отвечающие за их отрисовку
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


clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

font1 = pygame.font.Font('data/tools/MangaMaster.ttf', 50)  # шрифты для цифр
font2 = pygame.font.Font('data/tools/MangaMaster.ttf', 700)
font3 = pygame.font.Font('data/tools/MangaMaster.ttf', 25)

itemss = []  # список аптечек и снайперских винтовок
spawns = []  # список спаунов
railshot_draw = []  # список следов от выстрелов из снайперских винтовок
rauldead = [False, 4, (0, 0)]  # списки для слежения - погиб ли игрок или нет?
dimadead = [False, 4, (0, 0)]
raulscore = 0  # счёт первого игрока
dimascore = 0  # счёт первого игрока


def DrawWindow():  # отрисовка уровня
    screen.blit(load_image('images/' + level.levelmap + '.png'), (0, 0))
    if rauldead[0]:  # отрисовка могилки при смерти
        screen.blit(load_image('images/grave.png'), rauldead[2])

    if dimadead[0]:
        screen.blit(load_image('images/grave.png'), dimadead[2])

    for bullet in bullets:  # прорисовка патронов
        bullet.draw()

    for bullet1 in bullets1:
        bullet1.draw()

    screen.blit(load_image("images/Raul/head.png"), (0, 5))  # иконки персонажей рядом с полосками здоровья
    screen.blit(load_image("images/Dima/head.png"), (1170, 5))
    screen.fill(pygame.Color('red'), pygame.Rect(35, 10, 200, 20))  # реализация полосок здоровья
    screen.fill(pygame.Color('green'), pygame.Rect(35, 10, hp, 20))
    if hp > 0:  # численное значение показывающие количество жизней
        if hp >= 155:
            screen.blit(font3.render(str(hp), True, (255, 255, 255)), (190, 5))
        else:
            screen.blit(font3.render(str(hp), True, (255, 255, 255)), (hp + 35, 5))
    elif hp <= 0:
        screen.blit(font3.render('ВОЗРОЖДЕНИЕ', True, (255, 255, 255)), (55, 4))

    screen.fill(pygame.Color('red'), pygame.Rect(965, 10, 200, 20))
    screen.fill(pygame.Color('green'), pygame.Rect(965 + 200 - hp1, 10, hp1, 20))
    if hp1 > 0:
        if hp1 >= 155:
            screen.blit(font3.render(str(hp1), True, (255, 255, 255)), (967, 5))
        else:
            screen.blit(font3.render(str(hp1), True, (255, 255, 255)), (1127 - hp1, 5))
    elif hp1 <= 0:
        screen.blit(font3.render('ВОЗРОЖДЕНИЕ', True, (255, 255, 255)), (989, 4))

    for i in spawns:  # отрисовка спаунов
        screen.blit(load_image('images/spawn.png'), (i[0], i[1]))

    if len(gains) > 0:  # отрисовки улучшений рядом с полосками жизней
        for i in gains:
            if i[0] == 'QUAD':
                gain = pygame.transform.scale(load_image("images/quad.png"), (20, 20))
            else:
                gain = pygame.transform.scale(load_image("images/protection.png"), (20, 20))
            screen.blit(gain, (240, 10))
            screen.blit(font3.render(str(i[1]), True, (255, 255, 255)), (265, 6))

    if len(gains1) > 0:
        for i in gains1:
            if i[0] == 'QUAD':
                gain = pygame.transform.scale(load_image("images/quad.png"), (20, 20))
            else:
                gain = pygame.transform.scale(load_image("images/protection.png"), (20, 20))
            screen.blit(gain, (905, 10))
            screen.blit(font3.render(str(i[1]), True, (255, 255, 255)), (930, 6))

    if len(railshot_draw) > 0:  # отрисовка следа от выстрела из снайперской винтовки
        for i in railshot_draw:
            if i[2] > 0:
                if i[1] == -1:
                    pygame.draw.line(screen, (136, 6, 206), (0, i[3]), (i[0], i[3]), 5)
                elif i[1] == 1:
                    pygame.draw.line(screen, (136, 6, 206), (i[0], i[3]), (1200, i[3]), 5)

    sprite_group.draw(screen)  # отрисовка спрайтов

    for i in itemss:  # отрисовка предметов
        if i[5]:
            screen.blit(load_image(i[4]), (i[0], i[1]))

    if text.split(':')[0] == '0':  # отрисовка времени и счёта
        screen.blit(font1.render(text, True, (255, 0, 0)), (555, 3))
    else:
        screen.blit(font1.render(text, True, (255, 255, 255)), (555, 3))
    if len(str(raulscore)) == 2:
        screen.blit(font1.render(str(raulscore), True, (255, 0, 0)), (480, 3))
    else:
        screen.blit(font1.render(str(raulscore), True, (255, 0, 0)), (500, 3))
    screen.blit(font1.render(str(dimascore), True, (0, 0, 255)), (670, 3))

    pygame.display.flip()


game.menu()  # вызов главного меню
x, y = 0, 0
for row in load_level(level.levelmap + '.txt'):  # проходимся по текстовому файлу и добавляем нужное в наши списки
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
    if game.startlvl:  # приведение всех переменных в начальное состояние перед началом игры
        if level.levelmap == 'level_1':
            pygame.mixer_music.load('data/sounds/Black Magic.mp3')
        else:
            pygame.mixer_music.load('data/sounds/Corrupted Keep.mp3')
        setting = open('data/tools/music.ini', encoding='utf-8').read()
        if setting == 'on':
            pygame.mixer_music.set_volume(0.3)
        else:
            pygame.mixer_music.set_volume(0)
        pygame.mixer_music.play()
        sound_start_round.play()
        for i in range(9):  # обратный отсчёт
            screenm.blit(load_image('images/' + level.levelmap + '.png'), (0, 0))
            if i == 6:
                screenm.blit(font2.render('3', True, (255, 255, 255)), (400, -140))
            elif i == 7:
                screenm.blit(font2.render('2', True, (255, 255, 255)), (400, -140))
            elif i == 8:
                screenm.blit(font2.render('1', True, (255, 255, 255)), (400, -140))
            pygame.display.flip()
            pygame.time.delay(1130)  # задержка перед началом
        sprite_group.empty()
        kshoot, kshoot1 = 0, 0
        sound_respawn.play()
        platforms = []
        x, y = 0, 0
        itemss = []
        spawns = []
        for row in load_level(level.levelmap + '.txt'):  # проходимся по текстовому файлу и добавляем нужное в наши списки
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
        rauldead = [False, 4, (0, 0)]
        dimadead = [False, 4, (0, 0)]
        leftP, rightP, upP = False, False, False
        leftP1, rightP1, upP1 = False, False, False
        hp1 = 200
        hp = 200
        counter, text = 300, '5:00'.rjust(3)
        weapons = ['RIFLE']
        weapons1 = ['RIFLE']
        gains = []
        gains1 = []
        bullets = []
        bullets1 = []
        railshot_draw = []
        raulscore = 0
        dimascore = 0
        game.startlvl = False
        hero.update(leftP, rightP, upP, platforms)
        hero1.update(leftP1, rightP1, upP1, platforms)
        pygame.event.clear()
    if not game.startlvl:
        setting = open('data/tools/music.ini', encoding='utf-8').read()
        if setting == 'on':
            pygame.mixer_music.set_volume(0.3)
        else:
            pygame.mixer_music.set_volume(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # закрытие окна при нажатии на крестик в правом верхнем углу
                sound_button_press.play()
                pygame.time.delay(600)
                running = False
            if event.type == pygame.USEREVENT:  # реализация таймера
                counter -= 1
                if counter >= 0:
                    if rauldead[0]:  # смерть первого персонажа
                        rauldead[1] -= 1
                        if rauldead[1] == 0:  # возрождение первого персонажа
                            hero.yvel = 0
                            hero.xvel = 0
                            hero.stay = True
                            hero.onGround = False
                            leftP, rightP, upP = False, False, False
                            i = choice(spawns)
                            if i[0] <= 600:
                                hero.viewSide = "r"
                            else:
                                hero.viewSide = "l"
                            x = i[0] + 6
                            y = i[1] + 20
                            sound_respawn.play()
                            hero.rect.x, hero.rect.y = x, y
                            hp = 200
                            rauldead = [False, 4, (0, 0)]
                    if dimadead[0]:  # смерть первого персонажа
                        dimadead[1] -= 1
                        if dimadead[1] == 0:  # возрождение первого персонажа
                            hero1.yvel = 0
                            hero1.xvel = 0
                            hero1.stay = True
                            hero1.onGround = False
                            leftP1, rightP1, upP1 = False, False, False
                            i = choice(spawns)
                            if i[0] <= 600:
                                hero1.viewSide = "r"
                            else:
                                hero1.viewSide = "l"
                            x = i[0] + 6
                            y = i[1] + 20
                            sound_respawn.play()
                            hero1.rect.x, hero1.rect.y = x, y
                            hp1 = 200
                            dimadead = [False, 4, (0, 0)]
                    if len(gains) > 0:  # таймеры улучшенийи
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
                    if len(railshot_draw) > 0:  # таймер отрисовки линии от выстрела
                        for i in railshot_draw:
                            i[2] -= 1
                            if i[2] == 0:
                                railshot_draw.remove(i)
                    for i in itemss:  # таймер предметов
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
                    if round_time == '1:00':
                        sound_1_min.play()
                    if railshoot != 0:
                        railshoot -= 1
                    if railshoot1 != 0:
                        railshoot1 -= 1
                    if hp < 0:  # жизни всегда >= 0
                        hp = 0
                    if hp1 < 0:
                        hp1 = 0

                if counter == 0:  # время закончилось
                    pygame.mixer_music.stop()
                    sound_end_round.play()
                    sound_1_min.stop()
                    sound_5_min.stop()
                    sound_button_press.stop()
                    sound_button_press_game.stop()
                    sound_button_press_map.stop()
                    sound_start_game.stop()
                    sound_start_round.stop()
                    sound_change_weapon.stop()
                    sound_death.stop()
                    sound_hit.stop()
                    sound_railgun_shot.stop()
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
                    end.endf()  # открытие окна иитогов
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # открытие паузы при нажатии на клавишу ESCAPE
                    sound_1_min.stop()
                    sound_5_min.stop()
                    sound_button_press.stop()
                    sound_button_press_game.stop()
                    sound_button_press_map.stop()
                    sound_start_game.stop()
                    sound_end_round.stop()
                    sound_start_round.stop()
                    sound_change_weapon.stop()
                    sound_death.stop()
                    sound_hit.stop()
                    sound_railgun_shot.stop()
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
                if not rauldead[0]:
                    if event.key == pygame.K_e:  # смена оружия(если оно не одно)
                        if len(weapons) > 1:
                            sound_change_weapon.play()
                            weapons.reverse()
                    if event.key == pygame.K_a:  # движение налево
                        leftP = True
                    if event.key == pygame.K_d:  # движение направо
                        rightP = True
                    if event.key == pygame.K_w:  # прыжок
                        upP = True
                if not dimadead[0]:
                    if event.key == pygame.K_LEFT:  # движение налево
                        leftP1 = True
                    if event.key == pygame.K_RIGHT:  # движение направо
                        rightP1 = True
                    if event.key == pygame.K_UP:  # прыжок
                        upP1 = True
                    if event.key == pygame.K_KP1:  # смена оружия(если оно не одно)
                        if len(weapons1) > 1:
                            sound_change_weapon.play()
                            weapons1.reverse()
            if event.type == pygame.KEYUP:  # реализация отжатий клавиш
                if not rauldead[0]:
                    if event.key == pygame.K_a:
                        leftP = False
                    if event.key == pygame.K_d:
                        rightP = False
                    if event.key == pygame.K_w:
                        upP = False
                if not dimadead[0]:
                    if event.key == pygame.K_LEFT:
                        leftP1 = False
                    if event.key == pygame.K_RIGHT:
                        rightP1 = False
                    if event.key == pygame.K_UP:
                        upP1 = False

        for bullet in bullets:  # работа с пулями
            if 1300 > bullet.x > -100:
                if bullet.__class__.__name__ != 'SnaryadRail':
                    bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

            if bullet.__class__.__name__ != 'SnaryadRail':  # если выстрел с винтовки
                if hero1.rect.x + 48 >= bullet.x >= hero1.rect.x and hero1.rect.y + 80 >= bullet.y >= hero1.rect.y:
                    sound_hit.play()
                    damage = 6  # урон от винтовки
                    if len(gains) > 0:
                        for i in gains:
                            if i[0] == 'QUAD':
                                damage = damage * 4  # увеличение урона при улучшении
                    if len(gains1) > 0:
                        for i in gains1:
                            if i[0] == 'PROT':
                                damage = damage // 3  # уменьшение получаемого урона при улучшении
                    if str(hp1 - damage)[0] == '-':
                        hp1 = 0
                    else:
                        hp1 -= damage
                    bullets.pop(bullets.index(bullet))  # пуля пропадает после попадания
            else:
                do_hit = 0  # флаг попадания из снайперской винтовки
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
                                damage = damage * 4  # увеличение урона при улучшении
                    if len(gains1) > 0:
                        for i in gains1:
                            if i[0] == 'PROT':
                                damage = damage // 3  # уменьшение получаемого урона при улучшении
                    if str(hp1 - damage)[0] == '-':
                        hp1 = 0
                    else:
                        hp1 -= damage
                bullets.pop(bullets.index(bullet))
                railshot_draw.append([bullet.x, bullet.facing, 2, bullet.y])  # отрисовка следа от выстрела
        if hp <= 0 and not rauldead[0]:  # смерть первого игрока обнуляем все оружия и улучшения
            rauldead = [True, 4, (hero.rect.x, hero.rect.y)]
            hero.rect.x = 2000
            hero.rect.y = 2000
            sound_death.play()
            gains = []
            weapons = ['RIFLE']
            dimascore += 1
            kshoot = 0
            railshoot = 0
        if hp1 <= 0 and not dimadead[0]:  # смерть второго игрока обнуляем все оружия и улучшения
            dimadead = [True, 4, (hero1.rect.x, hero1.rect.y)]
            hero1.rect.x = 2000
            hero1.rect.y = 2000
            sound_death.play()
            gains1 = []
            weapons1 = ['RIFLE']
            raulscore += 1
            kshoot1 = 0
            railshoot1 = 0
        if kshoot == 7:  # начало перезарядки при выстреле 7 патронов
            flshoot = False
            kpshoot = 0
            kshoot = 0
        if kpshoot == 30:  # конец перезарядки, разрешение стрельбы
            flshoot = True
        if hero.viewSide == "r":  # узнаём в какую сторону полетит пуля
            facing = 1
        elif hero.viewSide == "l":
            facing = -1
        if hero1.viewSide == "r":
            facing1 = 1
        elif hero1.viewSide == "l":
            facing1 = -1

        for bullet1 in bullets1:  # работа с пулями второго персонажа симметричная работе с первым
            if 1300 > bullet1.x > -100:
                if bullet1.__class__.__name__ != 'SnaryadRail':
                    bullet1.x += bullet1.vel1
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
                        sound_quad_get.play()
                        gains1.append(['QUAD', 30])
                        item[5] = False
                    elif item[8] == 'PROT':
                        sound_protection_get.play()
                        gains1.append(['PROT', 30])
                        item[5] = False

        keys = pygame.key.get_pressed()  # получаем список нажатых клавиш
        if keys[pygame.K_SPACE] and not rauldead[0]:  # стрельба первого игрока
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

        if keys[pygame.K_KP0] and not dimadead[0]:  # стрельба второго игрока
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
        # читы
        if keys[pygame.K_F1]:  # моментальное заполнение полосок здоровья
            hp1 = 200
            hp = 200
        if keys[pygame.K_F5]:  # спаун персонажей в изначальных позициях
            hero.yvel = 0
            hero.rect.x, hero.rect.y = 5, 440
            hero1.yvel = 0
            hero1.rect.x, hero1.rect.y = 1147, 440

        kpshoot += 1  # перезарядка
        kpshoot1 += 1
        if not game.startlvl:
            DrawWindow()
        hero.update(leftP, rightP, upP, platforms)  # обновляем состояния игроков
        hero1.update(leftP1, rightP1, upP1, platforms)
        for bullet in bullets:  # обновляем состояния пуль
            bullet.draw()
        for bullet in bullets1:
            bullet.draw()
# завершение работы:
pygame.quit()
