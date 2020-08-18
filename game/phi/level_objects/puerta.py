import element
import pygame
import extra_data.images as img

class puerta(element.element):
    def __init__(self,x,y,direccion = "Horizontal", name = "", long = 4):
        puerta = pygame.transform.scale(img.puerta,(50*long,img.puerta.get_size()[1]))
        if direccion == "Vertical":
            puerta = pygame.transform.rotate(puerta,90)
        self.ant_open = False
        self.open = False
        self.direccion = direccion
        self.pos_original = (x,y)
        self.element(x, y, name, "Puerta", ["Wall"], puerta)
        self.abriendo_puerta = False
        self.cerrando_puerta = False
        self.long = long
    def pgu(self,pantalla):
        if self.open and not self.ant_open:
            self.ant_open = True
            self.cerrando_puerta = False
            self.abriendo_puerta = True
        elif not self.open and self.ant_open:
            self.ant_open = False
            self.abriendo_puerta = False
            self.cerrando_puerta = True
        if self.abriendo_puerta:
            if self.direccion == "Horizontal":
                if self._x < self.pos_original[0] + self.W:
                    self._x += 4
                else:
                    self.abriendo_puerta = False
            elif self.direccion == "Vertical":
                if self._y < self.pos_original[1] + self.H:
                    self._y += 4
                else:
                    self.abriendo_puerta = False
        if self.cerrando_puerta:
            if self.direccion == "Horizontal":
                if self._x > self.pos_original[0]:
                    self._x -= 4
                else:
                    self.cerrando_puerta = False
            elif self.direccion == "Vertical":
                if self._y > self.pos_original[1]:
                    self._y -= 4
                else:
                    self.cerrando_puerta = False
    def plu(self,events,up):
        jugador = None
        for obj in up.objetos:
            if obj.TYPE == "jugador":
                if obj.principal:
                    jugador = obj
        if jugador != None:
            if jugador._x + jugador.W > self._x - 100 and jugador._x < self._x + self.W + 100 and jugador._y + jugador.H > self._y - 100 and jugador._y < self._y + self.H + 100:
                if not self.open:
                        self.open = True
            else:
                if self.open:
                    self.open = False