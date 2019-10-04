import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(r'C:\Users\danie\Desktop\scripts-python\threedaysgrace.mp3')
pygame.mixer.music.play()
pygame.event.wait()