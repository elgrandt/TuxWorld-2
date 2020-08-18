import pygame,buttons,send,utils.pfunctions as pfunctions

class info_area:
    def __init__(self):
        self.tamY = 21
        self.color = (211,211,211)
        self.resize()
        self.clickeado = False
        self.datos = []
        self.lp = 0
    def agregar_boton(self,name,elementos):
        self.datos.append([name,elementos])
    def init(self):
        self.crear_botones()
    def crear_botones(self):
        self.botones = []
        for e in range(len(self.datos)):
            w = self.datos[e]
            name = w[0]
            botones = w[1]
            self.botones.append(buttons.boton_menu(name,self.lp,self.color,len(botones),self.tamY))
            self.lp = 0
            for r in range(e+1):
                self.lp += self.botones[r].Tbot[0]
            for q in botones:
                self.botones[len(self.botones)-1].agregar_boton_menu(q,(255,255,230))
    def resize(self):
        self.surface = pygame.surface.Surface((pygame.display.get_surface().get_size()[0],self.tamY))
        self.surface.fill(self.color)
        self.size = pygame.display.get_surface().get_size()
    def graphic_update(self,pantalla):
        pantalla.blit(self.surface,(0,0))
        for q in self.botones:
            q.graphic_update(pantalla)
    def logic_update(self,events,UP):
        self.UP = UP
        comando = None
        if self.size[0] != pygame.display.get_surface().get_size()[0] or self.size[1] != pygame.display.get_surface().get_size()[1]:
            self.resize()
        for w in range(len(self.botones)):
            q = self.botones[w]
            comando = q.logic_update(events)
            self.analizar_command(comando,w)
    def analizar_command(self,comando,boton):
        if comando != None:
            if comando == "Enviado":
                clickeado_menu = self.botones[boton].enviado
                name_bot = self.botones[boton].name
                name_bot_men = self.botones[boton].Nbotones[clickeado_menu]
                send.send(name_bot,name_bot_men,self)