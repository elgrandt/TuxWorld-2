import pygame,utils.pfunctions as pfunctions
import level_objects as lo
from pygame.locals import *
from extra_data.images import tux1
import extra_data.images as img
import level_objects.vidas_extra as vida
import utils.checkpoint as chk

class cam:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.pantalla = pygame.display.get_surface()

class level_data:
    def __init__(self,lives):
        import game.bar as tim
        self.time = tim.tim()
        self.lives = 0
        
class phi:
    def __init__(self):
        self.playing = True
        self.my_player = "player1"
        self.objetos = []
        self.prosc = []
        self.limites = [(0,500),(0,500)]
        self.Tpared = img.wall1.get_size()
        self._CAM = cam()
        self.perdio = False
        self.level_name = ""
        self.level_author = ""
        self.level_description = ""
        self.FT = True
        self.rango_disferencia_camara = 250
    def auto_init(self,elements,prosc):
        self.objetos = elements
        self.prosc = prosc
    def agregar_vida_extra(self,pos,name):
        self.objetos.append(vida.vida(pos,name))
    def agregar_moneda(self,pos,name):
        self.objetos.append(lo.moneda.moneda(pos,name,1))
    def agregar_enemigo(self,name,TYPE,pos):
        self.objetos.append(lo.enemies.enemy.reEnemy(pos[0],pos[1], name, TYPE))
    def agregar_jugador(self,name,definitivo = True):
        if definitivo:
            self.my_player = name
        self.objetos.append(lo.jugador.jugador(100,100,name))
    def graphic_update(self,pantalla):
        for x in range(len(self.objetos)):
            self.objetos[x].graphic_update(pantalla)
    def logic_update(self,events):
        if self.FT:
            self.FT = False
            inf = chk.consultar(self.level_name,self.objetos,self.my_player)
            if inf != "Error":
                for x in range(len(self.objetos)):
                    if self.objetos[x].TYPE == "jugador":
                        if self.objetos[x].principal:
                            self.objetos[x]._x = inf[0]
                            self.objetos[x]._y = inf[1]
        existe = False
        existe_principal = False
        for q in self.objetos:
            if q.TYPE == "jugador":
                existe = True
                if q.principal:
                    existe_principal = True
                    break
        if existe and existe_principal:
            element = pfunctions.get_element(self.objetos, self.my_player)
            if element != None:
                pos = element.get_pos()
                Ttux = tux1.get_size()
                Tpantalla = pygame.display.get_surface().get_size()
                if pos[0] - self._CAM.X > Tpantalla[0]-Ttux[0]-self.rango_disferencia_camara:
                    self._CAM.X += element.speed
                if pos[0] - self._CAM.X < self.rango_disferencia_camara:
                    self._CAM.X -= element.speed
                if pos[1] - self._CAM.Y > Tpantalla[1]-Ttux[1]-self.rango_disferencia_camara:
                    self._CAM.Y += element.speed
                if pos[1] - self._CAM.Y < self.rango_disferencia_camara:
                    self._CAM.Y -= element.speed
            else:
                for q in self.objetos:
                    if q.TYPE == "jugador":
                        if q.principal:
                            self.my_player = q.NAME
        elif existe and not existe_principal:
            keys = events.get_keyboard()
            speed = 10
            if keys[pygame.K_UP]:
                self._CAM.Y -= speed
            if keys[pygame.K_DOWN]:
                self._CAM.Y += speed
            if keys[pygame.K_RIGHT]:
                self._CAM.X += speed
            if keys[pygame.K_LEFT]:
                self._CAM.X -= speed
        for x in range(len(self.objetos)-1,-1,-1):
            commands = self.objetos[x].logic_update(events,self)
            if (commands != None):
                for y in range(len(commands)):
                    if (commands[y] == "destroyme"):
                        del self.objetos[x]
                return commands[0]
                    
        if (events.get_keyboard()[pygame.K_r]):
            return "restart game"