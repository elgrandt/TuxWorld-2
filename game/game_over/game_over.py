from extra_data.fonts import font2
from utils.pfunctions import boton_redondo
import pygame
from extra_data.styles import op

class looser:
    def __init__(self,text):
        self.text = text
        self.hover1 = False
        self.hover2 = False
        self.PbotR = (1000,1000)
        self.PbotS = (1000,1000)
        self.fin = 0
    def graphic_update(self,pantalla):
        self.generar_game_over(pantalla)
        pantalla.fill((255,255,255))
        Tpantalla = pantalla.get_size()
        Tover = self.game_over.get_size()
        self.pos = (Tpantalla[0]/2-Tover[0]/2, Tpantalla[1]/2-Tover[1]/2)
        pantalla.blit(self.game_over,self.pos)
        self.Tbot = (200,50)
        self.PbotR = (Tpantalla[0]/2-self.Tbot[0]/2,self.pos[1]-100-self.Tbot[1])
        self.PbotS = (Tpantalla[0]/2-self.Tbot[0]/2,self.pos[1]+self.game_over.get_size()[1]+100)
        if self.hover1 == False:
            color1 = op("game_over","color_boton",(255,0,0))
        else:
            color1 = op("game_over","color_boton_hover",(0,0,255))
        if self.hover2 == False:
            color2 = op("game_over","color_boton",(255,0,0))
        else:
            color2 = op("game_over","color_boton_hover",(0,0,255))
        boton_redondo(pantalla, self.PbotR, self.Tbot, 10, "Reiniciar", True, 4, color1,(0,255,0))
        boton_redondo(pantalla, self.PbotS, self.Tbot, 10, "Salir", True, 4, color2,(0,255,0))
    def logic_update(self,events):
        mouse = events.get_mouse()
        pos = mouse.get_position()
        pressed = mouse.get_pressed()
        if pos[0] > self.PbotR[0] and pos[0] < self.PbotR[0]+self.Tbot[0] and pos[1] > self.PbotR[1] and pos[1] < self.PbotR[1]+self.Tbot[1]:
            self.hover1 = True
            if pressed[0]:
                self.fin = 2
                return "restart game"
        else:
            self.hover1 = False
        
        if pos[0] > self.PbotS[0] and pos[0] < self.PbotS[0]+self.Tbot[0] and pos[1] > self.PbotS[1] and pos[1] < self.PbotS[1]+self.Tbot[1]:
            self.hover2 = True
            if pressed[0]:
                self.fin = 1
                return "exit"
        else:
            self.hover2 = False
    def generar_game_over(self,pantalla):
        self.gameover1 = []
        test = font2.render(self.text,1,(0,0,255))
        lineas = []
        linea_act = ""
        for q in range(len(self.text)):
            linea_act += self.text[q]
            if q != len(self.text)-1:
                test1 = linea_act + self.text[q+1]
                test2 = font2.render(test1,1,(0,0,0))
                if test2.get_size()[0] > pantalla.get_size()[0]:
                    lineas.append(linea_act)
                    linea_act = ""
        if linea_act != "":
            lineas.append(linea_act)
        escrito = pygame.Surface((pantalla.get_size()[0],(test.get_size()[1]+10)*len(lineas)))
        escrito.fill((255,255,255))
        y_act = 0
        for q in lineas:
            act = font2.render(q,1,op("game_over","color_mensaje",(0,0,255)))
            escrito.blit(act,(pantalla.get_size()[0]/2-act.get_size()[0]/2, y_act))
            y_act += act.get_size()[1]+10
        self.game_over = escrito