import pygame, element, extra_data.images as img,utils.checkpoint as check

class meta(element.element):
    def __init__(self,x,y,long,vertical,NAME):
        imagen = pygame.Surface((50*long,20))
        im = img.meta
        self.long = long
        for q in range(0,long*50,50):
            im = pygame.transform.rotate(im,180)
            imagen.blit(im,(q,0))
        if vertical == "Vertical":
            self.original_vertical = "Vertical"
            imagen = pygame.transform.rotate(imagen,90)
        elif vertical == "Horizontal":
            self.original_vertical = "Horizontal"
        self.checked = False
        self.lchecked = False
        self.element(x, y, NAME, "Meta", [], imagen)
    def plu(self,events,up):
        if self.checked and not self.lchecked:
            self.lchecked = True
            check.grabar(up.level_name, "", up.my_player)
            return ["restart game"]