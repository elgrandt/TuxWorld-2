import pygame,element
import extra_data.images as im

class button(element.element):
    def __init__(self,pos_x,pos_y,objeto,name,default="Disabled"):
        self.imagen_presionado = im.boton_presionado
        self.imagen_no_presionado = im.boton_no_presionado
        self.object = objeto
        pos = [pos_x,pos_y]
        self.default = default
        if default == "Disabled":
            self.presionado = False
        elif default == "Enabled":
            self.presionado = True
        else:
            print "Error interpretando el default"
            self.presionado = False
        if self.presionado:
            imagen = self.imagen_presionado
        else:
            imagen = self.imagen_no_presionado
        self.element(pos[0], pos[1], name, "Button", [0], imagen)
        self.LT = pygame.time.get_ticks()
        self.activado = True
    def plu(self,events,UP):
        if self.activado:
            if self.presionado:
                self.surface = self.imagen_presionado
                for obj in UP.objetos:
                    if obj.NAME == self.object:
                        obj.permitido_act = True
            else:
                self.surface = self.imagen_no_presionado
                for obj in UP.objetos:
                    if obj.NAME == self.object:
                        obj.permitido_act = False