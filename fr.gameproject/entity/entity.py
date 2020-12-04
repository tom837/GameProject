import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.max_Heal = 100
        self.Heal = 100
        self.attack = 10
        self.velocity = 10
        self.image = pygame.image.load("assets/entity/entity_WIP.png")
        self.rect = self.image.get_rect()