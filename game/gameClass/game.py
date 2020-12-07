import sys
import pygame
from entityClass.player import Player
import screen

class Game():
    
    def __init__(self):
        #générer le joueur
        self.player = Player()

