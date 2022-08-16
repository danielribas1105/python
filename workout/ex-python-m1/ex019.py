import pygame
pygame.init()
pygame.mixer.music.load('ex-python/musictest.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
