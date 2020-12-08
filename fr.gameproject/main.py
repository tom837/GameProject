#importation des libs
import sys
import pygame
import games.game
import games.screen
#super class entity de la super class Sprite de pygame

#initialisation du jeu 
game = games.game.Game()
screen = games.screen.GameScreen()
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
