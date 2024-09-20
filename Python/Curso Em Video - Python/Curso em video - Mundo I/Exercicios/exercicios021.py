# FAÇA UM PROGRAMA QUE QUE ABRA E RAPRODUZA O AUDIO DE UMA ARQUIVO EM MP3
import pygame
pygame.init()
pygame.mixer.music.load('aula021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
 