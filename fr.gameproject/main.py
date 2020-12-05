#importation des libs
import pygame
import sys
import gameClass.game
import gameClass.screen
import gameClass.Entity.player
#initialisation du jeu 
gameClass.game.init()

screen = gameClass.screen.gameScreen()
player = gameClass.Entity.player.Player()

Continue = True
#boucle de rendering
while Continue:

    #boucle des event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
    screen.update()
pygame.quit()
sys.exit()
