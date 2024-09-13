import pygame
pygame.init()
pygame.mixer.music.load('tomp3.cc - Gabriel Henrique  Hallelujah Cover Acoustic.mp3')
pygame.mixer.music.play()
pygame.event.wait()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(100)
