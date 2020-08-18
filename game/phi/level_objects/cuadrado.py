#@PydevCodeAnalysisIgnore
import element
import pygame

class cuadrado(element.element):
    def __init__(self,x,y,name):
        sur = pygame.surface.Surface((200,200))
        sur.fill((124,234,234))
        self.element(x, y, name, "cuadrado", [], sur)