import pygame
import element
import extra_data.images as images
from utils.pfunctions import *

class bomb(element.element):
    def __init__(self,pos,name):
        self.Imagenes = images.cargar_bombas()
        
        self.element(pos[0],pos[1],name,"Dinamite",["Bomba","Wall"],self.Imagenes[0])
        self.explotando = False
        self.Surface_act = 0
        self.Last_time = 0
        self.UP = None
        self.FT = True
    def pgu(self,pantalla):
        
        
        a = self
        
        players = get_players(self.UP.objetos)
        
        for x in range(len(players)):
            b = players[x]
            colicion = colicion_detection(a,b)
            
            for y in range(len(colicion)):
                if (colicion[y] == ARRIBA):
                    self.activar()
            
        """
        if self.explotando and self.Last_time > 50:
            if self.FT:
                for q in range(len(self.UP.objetos)):
                    rango = 200
                    type = self.UP.objetos[q].TYPE
                    X,Y = self.UP.objetos[q]._x,self.UP.objetos[q]._y
                    W,H = self.UP.objetos[q].W,self.UP.objetos[q].H
                    if (X + W > self._x - rango and X < self._x + rango + self.W and Y + H > self._y - rango and Y < self._y + rango + self.H):
                        if type == "Enemy":
                            self.UP.objetos[q].potencia -= 1
                        elif type == "Moneda":
                            self.UP.objetos[q].permitido_act = False
                        elif type == "jugador":
                            self.UP.objetos[q].restar_energia(2)
                self.FT = False
            if self.Last_time == 60:
                self.Last_time = 50
                self.Surface_act += 1
                if self.Surface_act < 10:
                    self.surface = self.Imagenes[self.Surface_act]
                else:
                    self.permitido_act = False
                    self.explotando = False
        if self.explotando and self.Last_time < 50:
            self.surface = self.Imagenes[1]
            self.Surface_act = 1
        if self.explotando:
            self.Last_time += 1
        """

    def activar(self):
        pass
    
    def plu(self,events,UP):
        self.UP = UP