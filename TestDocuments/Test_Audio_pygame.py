import pygame
pygame.mixer.init()
pygame.mixer.music.load("answerFileTest.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
pygame.mixer.music.stop()
