import pygame,utils.pfunctions
from extra_data.fonts import font1
pygame.font.init()

def boton(Tboton = (0,0), text = "", centrado = True, ancho_borde = [1,1,1,1], color_boton = (255,255,255), color_letra = (0,0,0), color_borde = (0,0,0)):
    Sboton = pygame.Surface(Tboton)
    Sboton.fill(color_boton)
    Sboton = utils.pfunctions.add_border(Sboton, ancho_borde[0], ancho_borde[1], ancho_borde[2], ancho_borde[3], color_borde)
    Stext = font1.render(text,1,color_letra)
    Ttext = Stext.get_size()
    if centrado == True:
        Ptext = (Tboton[0]/2-Ttext[0]/2, Tboton[1]/2-Ttext[1]/2)
    else:
        Ptext = (3, Tboton[1]/2-Ttext[1]/2)
    Sboton.blit(Stext,Ptext)
    return Sboton