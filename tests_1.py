#Pour cette premire partie de projet le but été de se familiariser avec le module pygame et de comprendre son fonctionnement. 
#Nous avons donc pour l'instant seuleument réussi a crée la boucle qui fait tourner le jeux, crée la fenêtre de jeux et nous commencons a implementé les premiers sprite.

import pygame

#Initialise pygame
pygame.init ()

#Crée l'écran
screen = pygame.display.set_mode((800, 800))

#Crée un titre et des icones
pygame.display.set_caption("We Have NO Choice!?!")
icon = pygame.image.load('LOGO.png')
pygame.display.set_icon(icon)

#Joueur
playerImg =pygame.image.load('hero.png')
playerX = 400
playerY = 400
def player():
    screen.blit(playerimg,(playerX,playerY))


# Tourne le joue en boucle
running = True
while running:
    #Change la couleur de l'écran
    screen.fill((128,128,128))
    #Permet de fermez la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()


            
            
