import pygame, element
import extra_data.images as ei

class disk(element.element):
    def __init__(self,X,Y,DIRECCION,INDICE,NAME):
        self.indice = INDICE
        self.surface_original = ei.disco
        self.element(X,Y,NAME,"Disco",[],self.surface_original)
        self.activo = True
        self.UP = None
        self.direccion = DIRECCION
        self.velocidad = 7
        self.angle = 0
    def pgu(self,pantalla):
    	#self.angle += 10
    	if self.angle == 360:
    		self.angle = 0
    	self.surface = pygame.transform.rotate(self.surface_original,self.angle)
        if self.direccion == "ad":
            self._y -= self.velocidad
        elif self.direccion == "at":
            self._y += self.velocidad
        elif self.direccion == "de":
            self._x += self.velocidad
        elif self.direccion == "iz":
            self._x -= self.velocidad
        if self.UP != None:
            for q in range(len(self.UP.objetos)):
                if self.UP.objetos[q].TYPE != "Disco":
                    wall = False
                    for w in range(len(self.UP.objetos[q].TAGS)):
                        if self.UP.objetos[q].TAGS[w] == "Wall":
                            wall = True
                    if wall:
                        x,y = self._x,self._y
                        w,h = self.W,self.H
                        X,Y = self.UP.objetos[q]._x,self.UP.objetos[q]._y
                        W,H = self.UP.objetos[q].W,self.UP.objetos[q].H
                        if x + w > X and x < X + W and y + h > Y and y < Y + H:
                            type = self.UP.objetos[q].TYPE
                            if type == "Enemy":
                                self.UP.objetos[q].potencia -= 1
                            del self.UP.objetos[self.indice]
                            break
                    
    def plu(self,events,UP):
        self.UP = UP