import pygame
import glob
import utils.pfunctions as pf

ruta = "data/images/"
tux_world = pygame.image.load(ruta+"tux_world.png")
fondo_menu = pygame.image.load(ruta+"fondo_menu.png")
test_enemigo = pygame.image.load(ruta+"enemigos/windows.png")
test_enemigo = pygame.transform.scale(test_enemigo,(50,50))
enemigo2 = pygame.image.load(ruta+"enemigos/enemigo_x4.png")
moneda = pygame.image.load(ruta+"moneda.png")
caja = pygame.image.load(ruta+"Box/caja_cerrada.png")
caja = pygame.transform.scale(caja, (50, 50))
disco = pygame.image.load(ruta+"disco3.png")
disco = pygame.transform.scale(disco,(50,50))
test_background = pygame.Surface((50,50))
test_background.fill((0,133,255,0.98))
test_background = pf.add_border(test_background,2,2,2,2,(0, 0, 0))
test_bomba = pygame.image.load(ruta+"bombas/tnt_0.png")

def load_backgrounds():
    
    bks = glob.glob(ruta+"background/*.png")
    backgrounds = []
    for x in range(len(bks)):
        backgrounds.append(pygame.image.load(bks[x]))
    return backgrounds

def cargar_bombas():
    dmt = glob.glob(ruta+"bombas/*.png")
    dmt = sorted(dmt)
    bombas = []
    for x in dmt:
        print x
        bombas.append(pygame.image.load(x))
    
    return bombas

class pos:
    def __init__(self,positions):
        self.positions = positions

def r(image):
    return pygame.transform.flip(image,True,False)
class tuxc:
    def __init__(self):
        
        tuxs = []
        for x in sorted(glob.glob(ruta+"tux/*.png")):
            tuxs.append(pygame.transform.rotozoom(pygame.image.load(x),0,0.75))
            
        self.adelante = pos( [ tuxs[0] , tuxs[10] , tuxs[11] ] )
                                        
        self.atras = pos ( [ tuxs[1] , tuxs[2] , tuxs[3] ] )
        
        self.izquierda = pos ( [ r(tuxs[4]) , r(tuxs[5]) , r(tuxs[6]), r(tuxs[7]) , r(tuxs[8]), r(tuxs[9]) ] )
        
        self.derecha = pos ( [ tuxs[4] , tuxs[5] , tuxs[6] , tuxs[7] , tuxs[8] , tuxs[9] ] ) 


tux1 = pygame.image.load(ruta+"tux/tux1.png")
tux_azul = pygame.image.load(ruta+"Tux_azul.png")

tux = tuxc()

wall1 = pygame.image.load(ruta+"wall/paredTile.png")
esquina = pygame.image.load(ruta+"wall/esquina.png")

boton_presionado = pygame.image.load(ruta+"Boton/BotonPulsado.png")
boton_no_presionado = pygame.image.load(ruta+"Boton/BotonSinPulsar.png")
boton_presionado = pygame.transform.scale(boton_presionado,(50,50))
boton_no_presionado = pygame.transform.scale(boton_no_presionado,(50,50))

puerta = pygame.Surface((200,25))
puerta.fill((255,255,255))

puerta_test = pygame.image.load(ruta+"Puerta_test.jpg")

escudo = pygame.image.load(ruta+"Poderes/Escudo.png")
invulnerable = pygame.image.load(ruta+"Poderes/Invulnerable.png")

checkpoint_act = pygame.image.load(ruta+"Checkpoints/Activada.png")
checkpoint_sin_act = pygame.image.load(ruta+"Checkpoints/Sin activar.png")
checkpoint_act = pygame.transform.scale(checkpoint_act, (100,100))
checkpoint_sin_act = pygame.transform.scale(checkpoint_sin_act, (100,100))

teletransportador_in = pygame.image.load(ruta+"Teletransportador/Entrada.png")
teletransportador_out = pygame.image.load(ruta+"Teletransportador/Salida.png")

lampara = pygame.image.load(ruta+"lampara.png")

menu = pygame.transform.scale(pygame.image.load(ruta+"menu.png"),(90,90))

laser = pygame.image.load(ruta+"Laser.png")
laser = pygame.transform.scale(laser,(laser.get_size()[0] - 100, laser.get_size()[1] - 100))

ayuda = []
ayuda.append(pygame.image.load(ruta+"ayuda/IAB ayuda.png"))
ayuda.append(pygame.image.load(ruta+"ayuda/DAB ayuda.png"))
ayuda.append(pygame.image.load(ruta+"ayuda/IAR ayuda.png"))
ayuda.append(pygame.image.load(ruta+"ayuda/DAR ayuda.png"))

boton_configuracion_on = pygame.image.load(ruta+"Botones_config/Encendido.png")
boton_configuracion_off = pygame.image.load(ruta+"Botones_config/Apagado.png")

boton_configuracion_on = pygame.transform.scale(boton_configuracion_on,(boton_configuracion_on.get_size()[0],boton_configuracion_on.get_size()[1]-4))
boton_configuracion_off = pygame.transform.scale(boton_configuracion_off,(boton_configuracion_off.get_size()[0],boton_configuracion_off.get_size()[1]-4))
boton_configuracion = pygame.transform.scale(pygame.image.load(ruta+"Botones_config/conf.png"),(30,30))

meta = pygame.image.load(ruta+"meta.png")