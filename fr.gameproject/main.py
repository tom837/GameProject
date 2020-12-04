#importation des libs
import pygame
import sys

#initialisation des libs
pygame.init()

#initialisation des variable de paramètre 
size = width, height = 1080, 720
Continue = True

#initialisation de la fenêtre
pygame.display.set_caption("NSI Project")
screen = pygame.display.set_mode(size)

#boucle de rendering
while Continue:

    #boucle des event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False

pygame.exit()
sys.exit()
