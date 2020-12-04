import pygame

class gameScreen():
    def __init__(self):
        self.width = 720
        self.height = 1080
        self.size = (self.height,self.width)
        self.mode = pygame.display.set_mode(self.size)
        self.caption = pygame.display.set_caption("NSI Project")
    
    def update(self):
        self.mode = pygame.display.set_mode(self.size)
    
    def getSize(self):
        return self.size
    def setSize(self, newSize):
        assert type(newSize) == tuple
        self.size = newSize
        self.update()
    
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width