#importation des libs
import pygame
import sys
import gameClass.game
import gameClass.screen
#initialisation du jeu 
game = gameClass.game.Game()
screen = gameClass.screen.gameScreen()
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
