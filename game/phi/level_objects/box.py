import pygame
import element,random
from game.phi.level_objects import moneda,vidas_extra
from game.phi.level_objects.enemies import enemy
import extra_data.images as images

class box(element.element):
    def __init__(self,pos,name):
        self.element(pos[0],pos[1],name,"Box",["Box","Wall"],images.caja)
        self.es_caja = True
    def convertir(self,phi):
        self.es_caja = False
        rand = random.randrange(4)
        new_pos = (self._x,self._y)
        for q in phi.objetos:
            if q.TYPE == "jugador":
                if q.principal:
                    Ppos = (q._x,q._y)
                    Psize = (q.W,q.H)
                    while Ppos[0]+Psize[0] > new_pos[0] and Ppos[0] < new_pos[0] + self.W:
                        new_pos = (new_pos[0]+10,new_pos[1])
                    while Ppos[1]+Psize[1] > new_pos[1] and Ppos[1] < new_pos[1] + self.H:
                        new_pos = (new_pos[0],new_pos[1]+10)
        if rand == 0:
            phi.agregar_moneda(new_pos,self.NAME+" coin")
        elif rand == 1 or rand == 2:
            rand2 = random.randrange(2)+1
            phi.agregar_enemigo(self.NAME+" enemy",rand2,new_pos)
        elif rand == 3:
            rand2 = random.randrange(4)
            if rand2 == 1:
                phi.agregar_vida_extra(new_pos,self.NAME+" life")
            else:
                self.convertir(phi)
        self.permitido_act = False