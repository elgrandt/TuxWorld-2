import element
import pygame

class luz(element.element):
    def __init__(self,x,y,size_x,size_y,luminocidad,name):
        self.luminocidad_original = luminocidad
        self.luminocidad = luminocidad * 10
        if self.luminocidad < 0:
            self.prendida = False
            self.luminocidad *= -1
        else:
            self.prendida = True
        self.size = [size_x,size_y]
        size = [self.size[0]*50,self.size[1]*50]
        surface = pygame.Surface(size)
        if self.prendida:
            surface.fill((255,255,0))
        else:
            surface.fill((0,0,0))
        surface.set_alpha(self.luminocidad)
        self.element(x, y, name, "Luz", [], surface)