import pygame
import element
import extra_data.images as images

class moneda(element.element):
    def __init__(self,pos,name,TYPE):
        if TYPE == 1:
            mon = images.moneda
            self.costo = 1
        self.element(pos[0],pos[1],name,"Moneda",["Moneda","Plata"],mon)
        
        self.ciclo = 0
        
    def plu(self,events,UP):
        
        self.ciclo += 1
        
        if (self.ciclo >= 40):
            self.ciclo = 0
            
        if (self.ciclo >= 20):
            self._y += 1
        else:
            self._y -= 1