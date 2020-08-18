import phi
import info
import com
from random import randrange
from utils import pfunctions as pf
import pygame
import menu.menu_configuracion as conf

class game:
    def __init__(self):
        import bar
        #PHI
        self.phi = phi.phi()
        self.Npiso = "piso"
        #Menu bar
        #self.menu = info.info_area()
        #self.menu.init()
        #Info bar
        self.info = bar.bar()
        self.tim = bar.tim()
        self.objetos_pantalla = []
        self.FT = True
    def graphic_update(self,pantalla):
        if self.FT:
            self.FT = False
            self.objetos_pantalla.append(conf.config(self.phi.my_player))
        self.phi.graphic_update(pantalla)
        #self.menu.graphic_update(pantalla)
        self.info.graphic_update(pantalla)
        for q in self.objetos_pantalla:
            q.graphic_update(pantalla)
    def logic_update(self,events):
        devolver = self.phi.logic_update(events)
        #self.menu.logic_update(events,self)
        update_my_player_menu = self.update_my_player_menu(events)
        if update_my_player_menu != None:
            devolver = update_my_player_menu
        self.tim.update()
        self.info.logic_update(events,self.tim,self)
        for q in self.objetos_pantalla:
            dev = q.logic_update(events,self)
            if dev != None:
                devolver = dev
        return devolver
    def update_my_player_menu(self,events):
        existe = False
        hay_jugadores = False
        for q in self.phi.objetos:
            if q.TYPE == "jugador":
                hay_jugadores = True
                if q.principal:
                    existe = True
                    break
        if existe:
            element = pf.get_element(self.phi.objetos, self.phi.my_player)
            if element != None:
                self.info.life = pf.get_element(self.phi.objetos, self.phi.my_player).life
                self.info.money = pf.get_element(self.phi.objetos, self.phi.my_player).plata
                self.info.energy = pf.get_element(self.phi.objetos, self.phi.my_player).energy
                self.info.disks = pf.get_element(self.phi.objetos, self.phi.my_player).discos
            else:
                for q in self.phi.objetos:
                    if q.TYPE == "jugador":
                        if q.principal:
                            self.phi.my_player = q.NAME
        else:
            if hay_jugadores:
                self.phi.playing = False
                key = events.get_keyboard()
                if key[pygame.K_UP]:
                    self.phi._CAM.Y -= 5
                if key[pygame.K_DOWN]:
                    self.phi._CAM.Y += 5
                if key[pygame.K_LEFT]:
                    self.phi._CAM.X -= 5
                if key[pygame.K_RIGHT]:
                    self.phi._CAM.X += 5
            else:
                return "game over"