import pygame

#super class entity de la super class Sprite de pygame
class Entity(pygame.sprite.Sprite):
    #initialisation de la fonction d'initialisation de l'objet entity
    def __init__(self):
        #initialisation de la super class a l'initialisation de l'objet entity
        super().__init__()
        
        #initialisation des variable de base de l'objet 
        self.max_Heal = 100
        self.Heal = 100
        self.attack = 10
        self.lvl=1
        self.velocity = 10
        self.image = pygame.image.load("assets/entity/entity_WIP.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 800
    
    ##système de mouvement 

    #pour aller vers la droite 
    def moveRight(self):
        self.rect.x += self.velocity
    #pour aller vers la gauche 
    def moveLeft(self):
        self.rect.x -= self.velocity
    #pour aller vers le haut
    def moveUp(self):
        self.rect.y += self.velocity
    #pour aller vers le bas
    def moveDown(self):
        self.rect.y -= self.velocity
    
    
