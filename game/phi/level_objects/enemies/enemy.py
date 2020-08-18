from game.phi.level_objects.element import element
import extra_data.images as imagenes
from random import randrange as ran
from math import sin,cos,radians
import utils.pfunctions as pf

class reEnemy(element):
    def __init__(self,X,Y,NAME,TYPE,mobile=True,direccion = "Random", limite0 = -10000, limite1 = -10000,limite2 = 10000, limite3 = 10000):
        TYPE = int(TYPE)
        self.mobile = mobile
        self.angle = ran(0,360)
        self._TYPE = TYPE
        self.direccion = direccion
        self.dirh = 1
        self.dirv = 1
        self.limites = [limite0, limite1, limite2, limite3]
        if TYPE == 1:
            self.type1()
        elif TYPE == 2:
            self.type2()
        tags = ["Enemy","Wall","Mobile"]
        self.element(X, Y, NAME, "Enemy", tags, self.surface)
    def type1(self):
        self.speed = 0.5
        self.potencia = 1
        self.surface = imagenes.test_enemigo
    def type2(self):
        self.speed = 0.7
        self.potencia = 3
        self.surface = imagenes.enemigo2
    def avanzar(self):
        if self.direccion == "Random":
            self._x +=  sin( radians(float(self.angle)))  * float(self.speed)
            self._y +=  cos( radians(float(self.angle)))  * float(self.speed)
        elif self.direccion == "Horizontal":
            self._x += float(self.speed)*self.dirh
        elif self.direccion == "Vertical":
            self._y += float(self.speed)*self.dirv
        if int(self._x) < self.limites[0] or int(self._x) > self.limites[2]:
            self.dirh *= -1
        if int(self._y) < self.limites[1] or int(self._y) > self.limites[3]:
            self.dirv *= -1
    def plu(self,events,UP):
        if self.potencia <= 0:
            self.permitido_act = False
        if self.mobile:
            self.avanzar()
            for x in range(len(UP.objetos)):
                for y in range(len(UP.objetos[x].TAGS)):
                    if (UP.objetos[x].TAGS[y] == "Wall" or UP.objetos[x].TAGS[y] == "Enemy"):
                        det = pf.colicion_detection(self,UP.objetos[x])
                        for z in range(len(det)):
                            if (det[z] == 1):
                                self.angle = 360-self.angle
                                self.avanzar()
                            elif (det[z] == 2):
                                self.angle = 360-self.angle
                                self.avanzar()
                            elif (det[z] == 3):
                                self.angle -= self.angle * 2 + 180
                                self.avanzar()
                            elif (det[z] == 4):
                                self.angle -= self.angle * 2 + 180
                                self.avanzar()