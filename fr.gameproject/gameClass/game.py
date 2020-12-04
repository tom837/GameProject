import sys
import pygame

def init():
    print("hello world")
    pygame.init()

    #initialisation des variable de paramètre 
    size = width, height = 1080, 720

    #initialisation de la fenêtre
    pygame.display.set_caption("NSI Project")
    screen = pygame.display.set_mode(size)
    