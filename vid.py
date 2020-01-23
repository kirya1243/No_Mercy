import os
import sys
import vlc
import pygame
import time
start_time = time.time()


def callback(self, player):
    pass
    # print("-— %s seconds —-" % (time.time() - start_time))

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.get_wm_info()
movie = os.path.expanduser('data/tools/video.mp4')
vlcInstance = vlc.Instance()
media = vlcInstance.media_new(movie)
player = vlcInstance.media_player_new()
em = player.event_manager()
em.event_attach(vlc.EventType.MediaPlayerTimeChanged, callback, player)
win_id = pygame.display.get_wm_info()['window']
player.set_hwnd(win_id)
player.set_media(media)
player.play()

while player.get_state() != vlc.State.Ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(2)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                player.stop()
            # if event.key == pygame.K_RETURN:
            #     player.play()


# sound_button_press.play()
#                             pygame.time.wait(600)
#                             pygame.mixer_music.pause()
#                             pygame.display.get_wm_info()
#                             movie = os.path.expanduser('data/tools/instruction.mp4')
#                             vlcInstance = vlc.Instance()
#                             media = vlcInstance.media_new(movie)
#                             player = vlcInstance.media_player_new()
#                             em = player.event_manager()
#                             em.event_attach(vlc.EventType.MediaPlayerTimeChanged, callback, player)
#                             win_id = pygame.display.get_wm_info()['window']
#                             player.set_hwnd(win_id)
#                             player.set_media(media)
#                             player.play()
#
#                             while player.get_state() != vlc.State.Ended:
#                                 for event in pygame.event.get():
#                                     if event.type == pygame.QUIT:
#                                         sys.exit(2)
#                                     if event.type == pygame.KEYDOWN:
#                                         if event.key == pygame.K_ESCAPE:
#                                             player.stop()
#                                             # player.get_state() = vlc.State.Ended
#                                             sound_button_press.play()
#                                             pygame.time.wait(600)
#                                             pygame.mixer_music.unpause()
#                                         if event.key == pygame.K_RETURN:
#                                             player.play()
#                             player.e
