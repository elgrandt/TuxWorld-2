from game.phi.level_objects.element import element
import pygame
import extra_data.images as img
import esquina

class wall(element):
    def wall(self,X,Y,NAME,surface,ad_at_iz_de):
        self.element(X,Y,NAME, "Wall", ["Wall","SWall"], surface)
        self.ubic = ad_at_iz_de
        
class clasic_wall(wall):
    def __init__(self,X,Y,NAME,lonx,lony,rotated,arriba = "Centro"):
        self._lonx = lonx
        self._lony = lony
        self._rotated = rotated
        
        imagen = img.wall1
        surface = pygame.surface.Surface((img.wall1.get_size()[0]*lonx,img.wall1.get_size()[1]*lony))
            
        for x in range(lonx):
            for y in range(lony):
                surface.blit(imagen,(x*img.wall1.get_size()[0],y*img.wall1.get_size()[1]))
        if rotated == True:
            surface = pygame.transform.rotate(surface,90)
        self.wall(X, Y, NAME, surface, arriba)
        