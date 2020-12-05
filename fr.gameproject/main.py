#importation des libs
import pygame
import sys
from gameClass.game import Game
from gameClass.screen import gameScreen
#initialisation du jeu 
game = Game()
screen = gameScreen()
Continue = True
#boucle de rendering
while Continue:

    #boucle des event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
    screen.blit(game.player.image, game.player.rect)
pygame.quit()
sys.exit()
