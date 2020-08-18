import utils.pfunctions as pfunctions
import pygame,time

class boton_menu():
    def __init__(self,name,ub,color,cant_bot,tamY):
        tam = pfunctions.ubuntu_bold_graph.render(name, 1, (0,0,0)).get_size()
        tam = (tam[0]+30,tamY)
        self.Tbot_men = (160,26)
        self.color = color
        self.name = name
        self.ubic = ub
        self.Tbot = tam
        self.pos = (self.ubic,0)
        self.hover = False
        self.pressed = False
        self.nbot = 0
        self.menu = pygame.Surface((self.Tbot_men[0],self.Tbot_men[1]*cant_bot))
        self.Tmenu = (self.Tbot_men[0]+8,self.Tbot_men[1]*cant_bot+8)
        self.Pmenu = (self.pos[0],self.Tbot[1])
        self.menu.fill((211,211,211))
        self.menu = pfunctions.add_border(self.menu, 2, 2, 2, 2, (150,150,150))
        self.Pbotones = []
        self.Nbotones = []
        self.Cbotones = []
        self.hover_menu = []
        self.cant_bot = cant_bot
        self.LM = 0
        self.LM2 = 0
        self.enviado = False
    def graphic_update(self,pantalla):
        Tletra = 18
        if self.hover == False:
            self.boton = pfunctions.boton(self.Tbot, self.name, True, [0,0,0,0], self.color, (0,0,0), (0,0,0), Tletra)
        else:
            self.boton = pfunctions.boton(self.Tbot, self.name, True, [1,1,1,1], self.color, (0,0,0), (100,100,100), Tletra)
        pantalla.blit(self.boton,self.pos)
        if self.pressed == True:
            self.Mgraphic_update(pantalla)
    def logic_update(self,events):
        mouse = events.get_mouse()
        pressed = mouse.get_pressed()
        pos = mouse.get_position()
        devolver = None
        if self.pressed == True:
            devolver = self.Mlogic_update(events)
        if pos[0] > self.pos[0] and pos[1] > self.pos[1] and pos[0] < self.pos[0]+self.Tbot[0] and pos[1] < self.pos[1]+self.Tbot[1]:
            self.hover = True
            if pressed[0]:
                if not self.pressed and time.time() > self.LM2+0.3:
                    self.pressed = True
                    self.LM2 = time.time()
                elif time.time() > self.LM2+0.3:
                    self.pressed = False
        else:
            self.hover = False
            if pressed[0]:
                self.pressed = False
        return devolver
    def agregar_boton_menu(self,texto,color):
        test = pfunctions.ubuntu_bold_graph.render(texto, 1, (0,0,0))
        if test.get_size()[0] > self.Tbot_men[0]:
            self.Tbot_men = [test.get_size()[0]+20,self.Tbot_men[1]]
        self.Tmenu = (self.Tbot_men[0]+8,self.Tbot_men[1]*self.cant_bot+8)
        self.bot_men = pfunctions.boton(self.Tbot_men, texto, False, [1,1,1,1], color, (0,0,0), (0,0,0), 18)
        Pboton = (4,self.nbot*self.Tbot_men[1]+4)
        self.Pbotones.append(Pboton)
        self.Nbotones.append(texto)
        self.Cbotones.append(color)
        self.hover_menu.append(False)
        self.menu.blit(self.bot_men,Pboton)
        self.nbot += 1
    def Mgraphic_update(self,pantalla):
        self.menu = pygame.Surface((self.Tbot_men[0]+8,self.Tbot_men[1]*self.cant_bot+8))
        self.menu.fill((211,211,211))
        self.menu = pfunctions.add_border(self.menu, 2, 2, 2, 2, (150,150,150))
        for q in range(len(self.Nbotones)):
            texto = self.Nbotones[q]
            pos = self.Pbotones[q]
            color = self.Cbotones[q]
            hover_menu = self.hover_menu[q]
            if hover_menu:
                self.bot_men = pfunctions.boton(self.Tbot_men, texto, False, [1,1,1,1], (211,211,211), (0,0,0), (0,0,0), 18)
            else:
                self.bot_men = pfunctions.boton(self.Tbot_men, texto, False, [0,0,0,0], (211,211,211), (0,0,0), (0,0,0), 18)
            self.menu.blit(self.bot_men,pos)
        pantalla.blit(self.menu,(self.pos[0],self.pos[1]+self.Tbot[1]))
    def Mlogic_update(self,events):
        mouse = events.get_mouse()
        pressed = mouse.get_pressed()
        pos = mouse.get_position()
        devolver = None
        if pos[0] > self.Pmenu[0] and pos[0] < self.Pmenu[0]+self.Tmenu[0] and pos[1] > self.Pmenu[1] and pos[1] < self.Pmenu[1]+self.Tmenu[1]:
            self.hover_menu = []
            for q in range(len(self.Pbotones)):
                pose = (self.Pmenu[0]+self.Pbotones[q][0],self.Pmenu[1]+self.Pbotones[q][1])
                if pos[0] > pose[0] and pos[0] < pose[0]+self.Tbot_men[0] and pos[1] > pose[1] and pos[1] < pose[1]+self.Tbot_men[1]:
                    self.hover_menu.append(True)
                    tim = time.time()
                    if pressed[0] and tim > self.LM+0.3:
                        self.LM = tim
                        self.enviado = q
                        devolver =  "Enviado"
                else:
                    self.hover_menu.append(False)
        else:
            self.hover_menu = []
            for q in range(len(self.Pbotones)):
                self.hover_menu.append(False)
        return devolver