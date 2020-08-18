import pygame
import utils.pfunctions as pf
import utils.button as ub
import extra_data.fonts as font
import extra_data.images as img
import datetime
from extra_data.styles import op
from utils.help import help

class tim:
    def __init__(self):
        self.mcs = 0
        self.ms = 0
        self.s = 0
        self.m = 0
        self.h = 0
        self.inst = datetime.datetime.now()
    def update(self):
        dt = datetime.datetime.now()

        dif =  dt - self.inst

        self.ms += (dif.days * 24 * 60 * 60 + dif.seconds) * 100 + dif.microseconds / 10000.0
        
        while (self.ms >= 100):
            self.ms -= 100
            self.s += 1
        while (self.s >= 60):
            self.s -= 60
            self.m += 1
        while (self.m >= 60):
            self.m -= 60
            self.h += 1
        while (self.h >= 24):
            self.h -= 60
        
        
        
        self.inst = dt
def get_energy_surface(energy,maxx,dim):
    w,h = dim
    
    surface = pygame.surface.Surface(dim,pygame.SRCALPHA,32)
    
    frac = float ( energy ) / float ( maxx )
    
    lon = int ( frac * w )
    
    color = ( 255 - int( 255 * frac ) , 0 + int (255 * frac) , 0 )

    surface_life = pygame.surface.Surface((lon,h))
    
    surface_life.fill(color)
    
    surface.blit(surface_life,(0,0))
    
    return surface
    
class bar:
    def __init__(self):
        
        self.lw,self.lh = pygame.display.get_surface().get_size()
        
        self.resize()
        
        self.life = 0
        
        self.energy = 4
        
        self.money = 0

        self.disks = 5

        self.time = tim()
        
        self.tuximg = pygame.transform.scale(img.tux.adelante.positions[0],(30,40))
        self.moneyimg = pygame.transform.scale(img.moneda,(30,30))
        self.diskimg = pygame.transform.scale(img.disco,(30,30))
        self.escudoimg = pygame.transform.scale(img.escudo, (50,50))
        self.invimg = pygame.transform.scale(img.invulnerable, (50,50))

        self.hover_comprar1 = False
        self.hover_comprar2 = False
        self.ayudas = []
        self.ayudas.append(help("Indicador de vidas restantes"))
        self.ayudas.append(help("Indicador de monedas recolectadas"))
        self.ayudas.append(help("Indicador de discos restantes para disparar con la tecla espacio"))
        self.ayudas.append(help("Al comprar se activa un escudo que lo hace invulnerable solo hasta que lo toque algun enemigo"))
        self.ayudas.append(help("Al comprar se activa un escudo que lo hace invulnerable por un tiempo determinado"))
        self.ayudas.append(help("Energia restante para perder la proxima vida vida"))
    def graphic_update(self,pantalla):
        
        texto_life = font.ubuntu_bold_graph.render("x " + str(self.life),0,(244,250,88))
        texto_money = font.ubuntu_bold_graph.render("x "+str(self.money),0,(244,250,88))
        
        texto_energy = font.ubuntu_bold_graph.render("Energy: ",0,(255,255,255))
        
        texto_discos = font.ubuntu_bold_graph.render("x " + str(self.disks),0,(244,250,88))

        msad = ""
        if (self.time.ms < 10):
            msad = "0"
        sad = ""
        if (self.time.s < 10):
            sad = "0"
        mad = ""
        if (self.time.m < 10):
            mad = "0"
        texto_time = font.ubuntu_bold_graph.render(str(self.time.h) + " : "+mad+str(self.time.m) + " : " + sad+ str(self.time.s)+ " : "+msad+str(int(self.time.ms)),0,(255,255,255))
        
        surface_energy_dim = (pygame.display.get_surface().get_size()[0]-200,30)
        surface_energy = get_energy_surface(self.energy,4,surface_energy_dim)
        
        texto_escudos = font.ubuntu_bold_graph.render("x $20",1,(255,255,255))
        texto_invuln = font.ubuntu_bold_graph.render("x $40",1,(255,255,255))
        
        if self.hover_comprar1:
            font.ubuntu_bold_graph.set_underline(True)
        texto_comprar = font.ubuntu_bold_graph.render("Comprar",1,(0,255,255))
        font.ubuntu_bold_graph.set_underline(False)
        
        if self.hover_comprar2:
            font.ubuntu_bold_graph.set_underline(True)
        texto_comprar2 = font.ubuntu_bold_graph.render("Comprar",1,(0,255,255))
        font.ubuntu_bold_graph.set_underline(False)
        
        self.texto_comprar = texto_comprar
        
        self.resize()
        
        self.SURFACE.blit(texto_energy,(10,10+texto_life.get_size()[1]+10))
        
        pos_energy = (20+texto_energy.get_size()[0],10+texto_time.get_size()[1]+10)
        self.SURFACE.blit(surface_energy,pos_energy)
        
        self.SURFACE.blit(texto_time,(self.lw / 2 - texto_time.get_size()[0] / 2,10)) 
        
        pos_surface = (0,pygame.display.get_surface().get_size()[1] - 100 )
        pantalla.blit(self.SURFACE,pos_surface)
        
        pos_global_energy = (pos_surface[0]+pos_energy[0],pos_surface[1]+pos_energy[1])
        
        #Vidas
        pos_vidas = (pygame.display.get_surface().get_size()[0]-100,30)
        pantalla.blit(self.tuximg,pos_vidas)
        pantalla.blit(texto_life,(pygame.display.get_surface().get_size()[0]-100+self.tuximg.get_size()[0]+10,30+self.tuximg.get_size()[1]/2))
    
        #Monedas
        pos_money = (pygame.display.get_surface().get_size()[0]-100,80)
        pantalla.blit(self.moneyimg,pos_money)
        pantalla.blit(texto_money,(pygame.display.get_surface().get_size()[0]-100+self.moneyimg.get_size()[0]+10,70+self.moneyimg.get_size()[1]/2))
    
        #Discos
        pos_disk = (pygame.display.get_surface().get_size()[0]-100,90+self.moneyimg.get_size()[1])
        pantalla.blit(self.diskimg,pos_disk)
        pantalla.blit(texto_discos,(pygame.display.get_surface().get_size()[0]-100+self.diskimg.get_size()[0]+10,80+self.moneyimg.get_size()[1]+self.diskimg.get_size()[1]/2))        

        #Escudos
        pos_escudo = (15,pygame.display.get_surface().get_size()[1] - 130 - self.escudoimg.get_size()[1]/2)
        pantalla.blit(self.escudoimg, pos_escudo)
        pantalla.blit(texto_escudos, (15 + self.escudoimg.get_size()[0] + 5,pygame.display.get_surface().get_size()[1] - 130 - (texto_escudos.get_size()[1]*2+10)/2))
        self.pos_comprar1 = (15 + self.escudoimg.get_size()[0] + 5, pygame.display.get_surface().get_size()[1] - 130 - (texto_comprar.get_size()[1]*2+10)/2 + texto_comprar.get_size()[1] + 10)
        pantalla.blit(texto_comprar, self.pos_comprar1)
        
        #Invulneravilidad
        pos_inv = (15 + self.escudoimg.get_size()[0] + 5 + texto_comprar.get_size()[0] + 15, pygame.display.get_surface().get_size()[1] - 130 - self.invimg.get_size()[1]/2)
        pantalla.blit(self.invimg, pos_inv)
        pantalla.blit(texto_invuln, (15 + self.escudoimg.get_size()[0] + 5 + texto_comprar.get_size()[0] + 15 + self.invimg.get_size()[0] + 5,pygame.display.get_surface().get_size()[1] - 130 - (texto_invuln.get_size()[1]*2+10)/2))
        self.pos_comprar2 = (15 + self.escudoimg.get_size()[0] + 5 + texto_comprar.get_size()[0] + 15 + self.invimg.get_size()[0] + 5, pygame.display.get_surface().get_size()[1] - 130 - (texto_comprar.get_size()[1]*2+10)/2 + texto_comprar.get_size()[1] + 10)
        pantalla.blit(texto_comprar2, self.pos_comprar2)

        #Ayudas
        self.ayudas[0].cambiar_valores(pos_vidas,self.tuximg.get_size())
        self.ayudas[1].cambiar_valores(pos_money,self.moneyimg.get_size())
        self.ayudas[2].cambiar_valores(pos_disk,self.diskimg.get_size())
        self.ayudas[3].cambiar_valores(pos_escudo,self.escudoimg.get_size())
        self.ayudas[4].cambiar_valores(pos_inv,self.invimg.get_size())
        self.ayudas[5].cambiar_valores(pos_global_energy,surface_energy.get_size())
        
        for q in self.ayudas:
            q.graphic_update(pantalla)
    def logic_update(self,events,ti,UP):
        self.time = ti
        x,y = events.get_mouse().get_position()
        pressed = events.get_mouse().get_pressed()[0]
        jugador = None
        for obj in UP.phi.objetos:
            if obj.TYPE == "jugador":
                jugador = obj
        if x > self.pos_comprar1[0] and x < self.pos_comprar1[0] + self.texto_comprar.get_size()[0] and y > self.pos_comprar1[1] and y < self.pos_comprar1[1] + self.texto_comprar.get_size()[1]:
            self.hover_comprar1 = True
            if pressed and jugador != None:
                if jugador.plata > 20:
                    if not jugador.escudo_activado:
                        jugador.activar_escudo(10000,True)
                        jugador.sumar_monedas(-20)
        else:
            self.hover_comprar1 = False
        if x > self.pos_comprar2[0] and x < self.pos_comprar2[0] + self.texto_comprar.get_size()[0] and y > self.pos_comprar2[1] and y < self.pos_comprar2[1] + self.texto_comprar.get_size()[1]:
            self.hover_comprar2 = True
            if pressed and jugador != None:
                if jugador.plata > 40:
                    if not jugador.escudo_activado:
                        jugador.activar_escudo(15)
                        jugador.sumar_monedas(-40)
        else:
            self.hover_comprar2 = False
        
        for q in self.ayudas:
            q.profile = UP.phi.my_player
            q.logic_update(events)
    def resize(self):
        self.lw,self.lh = pygame.display.get_surface().get_size()
        self.SURFACE = pygame.surface.Surface((pygame.display.get_surface().get_size()[0], 100),pygame.SRCALPHA,32)
        
        background = pygame.surface.Surface(self.SURFACE.get_size())
        
        background.fill(op("bar","color",(0,0,0)))
        
        background.set_alpha(op("bar","transparencia"))
        
        self.SURFACE.blit(background,(0,0))
        
        pf.add_border(self.SURFACE, 1 , 1 , 1 ,1 , (0,0,0) )