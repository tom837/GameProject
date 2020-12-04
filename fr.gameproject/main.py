#importation des libs
import pygame
import sys
import gameClass.game
#initialisation du jeu 
gameClass.game.init()


Continue = True
#boucle de rendering
while Continue:

    #boucle des event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False

pygame.exit()
sys.exit()
