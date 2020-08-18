import element
import pygame
import extra_data.images as img

class teletransportador(element.element):
    def __init__(self,x_in,y_in,x_out,y_out,name):
        self.pos_in = (x_in,y_in)
        self.pos_out = (x_out,y_out)
        self.name_in = name + " in"
        self.name_out = name + " out"
        self._out = teletransportador_out(self.pos_out[0],self.pos_out[1],self.name_out)
        self.element(self.pos_in[0], self.pos_in[1], self.name_in, "Teletransportador_in", [], img.teletransportador_in)
    def pgu(self,pantalla):
        self._out.graphic_update(pantalla)
    def plu(self,events,UP):
        self._out.logic_update(events, UP)

class teletransportador_out(element.element):
    def __init__(self,x,y,name):
        self.element(x, y, name, "Teletransportador_out", [], img.teletransportador_out)