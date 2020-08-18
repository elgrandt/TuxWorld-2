import pygame
from game.phi.level_objects.element import element
import extra_data.images as img

class esquina(element):
    def __init__(self,X,Y,NAME,DIR):
        image = img.esquina
        self._dir = DIR
        if DIR == 0:
            pass
        elif DIR == 1:
            image = pygame.transform.rotate(image, 90)
        elif DIR == 2:
            image = pygame.transform.rotate(image, 180)
        elif DIR == 3:
            image = pygame.transform.rotate(image, 270)
        self.element(X, Y, NAME, "Wall", ["Wall","SWall","Esquina"], image)
        self.ubic = "Abajo"