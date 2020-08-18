import pygame,extra_data.images as images
import element

class vida(element.element):
    def __init__(self,pos,NAME):
        imagen = pygame.transform.scale(images.tux_azul, (30, 40))
        self.element(pos[0],pos[1], NAME, "vida_extra", ["Vida"], imagen)