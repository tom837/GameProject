import pygame

#creation de l'objet gameScreen
class GameClass():
    #Initialisation de l'objet gameScreen

    def __init__(self):
        #La taille de l'écran 
        self.width = 720
        self.height = 1080
        self.size = (self.height,self.width) #La taille est de type tuple 

        #initialisation de l'écran 
        self.mode = pygame.display.set_mode(self.size)

        #configuration de l'écran 
        self.caption = pygame.display.set_caption("NSI Project")
        self.link = "fr.gameproject/assets/background_WIP.png"
        self.image = pygame.image.load(self.link)


    def update(self):
        self.blit(self.image,(0,0))

    #méthode pour la taille 
    def getSize(self):
        return self.size
    def setSize(self, newSize):
        assert type(newSize) == tuple
        self.size = newSize
        self.update()
    
    #méthode pour la hauteur de la fenêtre 
    def getHeight(self):
        return self.height
    def setHeight(self, nHeight):
        self.height=nHeight
        self.setSize((nHeight, self.width))
    
    #méthode pour la largeur de la genêtre 
    def getWidth(self):
        return self.width
    def setWidth(self, nWidth):
        self.width = nWidth
        self.setSize((self.height, nWidth))
    def blit(self, subject, rect):
        self.mode.blit(subject, rect)