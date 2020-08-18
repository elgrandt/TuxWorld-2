import pygame, extra_data.images as img
import extra_data.fonts as font
import utils.config_data as conf

class help:
    def __init__(self,texto,posicion=[0,0],tamano=[0,0],profile=None):
        self.Texto = texto
        self.Posicion_objeto = posicion
        self.Tamano_objeto = tamano
        self.Font = pygame.font.Font(font.font3,12)
        self.Imagenes = img.ayuda
        self.Enabled = False
        self.profile = profile
    def cambiar_valores(self,nueva_posicion,nuevo_tamano):
        self.Posicion_objeto = nueva_posicion
        self.Tamano_objeto = nuevo_tamano
    def graphic_update(self,Pantalla):
        if self.Enabled:
            self.Posicion = [self.Posicion_objeto[0],self.Posicion_objeto[1]]
            self.Size = [110,5]
            lineas = self.crear_lineas(self.Texto, self.Size[0])
            while len(lineas) > 6:
                self.Size[0] += 10
                lineas = self.crear_lineas(self.Texto, self.Size[0])
            for q in lineas:
                self.Size[1] += self.Font.render(q,1,(0,0,0)).get_size()[1] + 5
            
            Tpantalla = Pantalla.get_size()
            if self.Posicion[0] + self.Size[0] > Tpantalla[0] and self.Posicion[1] - self.Size[1] > 0:
                Posic = [self.Posicion_objeto[0],self.Posicion_objeto[1]]
                self.Imagen = self.Imagenes[1]
                self.Imagen = pygame.transform.scale(self.Imagen,(self.Size[0]+10,self.Size[1]+((12*self.Size[1])/100)))
                pos_y = 5
                for q in lineas:
                    render = self.Font.render(q,1,(0,0,0))
                    self.Imagen.blit(render,(self.Imagen.get_size()[0]/2-render.get_size()[0]/2, pos_y))
                    pos_y += render.get_size()[1] + 5
                Pantalla.blit(self.Imagen,(Posic[0]-self.Size[0],Posic[1]-self.Size[1]))
            elif self.Posicion[0] + self.Size[0] < Tpantalla[0] and self.Posicion[1] - self.Size[1] < 0:
                Posic = [self.Posicion_objeto[0]+self.Tamano_objeto[0],self.Posicion_objeto[1]+self.Tamano_objeto[1]]
                self.Imagen = self.Imagenes[2]
                self.Imagen = pygame.transform.scale(self.Imagen,(self.Size[0]+10,self.Size[1]+((12*self.Size[1])/100)))
                pos_y = ((12*self.Size[1])/100)+5
                for q in lineas:
                    render = self.Font.render(q,1,(0,0,0))
                    self.Imagen.blit(render,(self.Imagen.get_size()[0]/2-render.get_size()[0]/2, pos_y))
                    pos_y += render.get_size()[1] + 5
                Pantalla.blit(self.Imagen,(Posic[0],Posic[1]))
            elif self.Posicion[0] + self.Size[0] > Tpantalla[0] and self.Posicion[1] - self.Size[1] < 0:
                Posic = [self.Posicion_objeto[0], self.Posicion_objeto[1]+self.Tamano_objeto[1]]
                self.Imagen = self.Imagenes[3]
                self.Imagen = pygame.transform.scale(self.Imagen,(self.Size[0]+10,self.Size[1]+((12*self.Size[1])/100)))
                pos_y = ((12*self.Size[1])/100)+5
                for q in lineas:
                    render = self.Font.render(q,1,(0,0,0))
                    self.Imagen.blit(render,(self.Imagen.get_size()[0]/2-render.get_size()[0]/2, pos_y))
                    pos_y += render.get_size()[1] + 5
                Pantalla.blit(self.Imagen,(Posic[0]-self.Size[0],Posic[1]))
            else:
                Posic = [self.Posicion_objeto[0] + self.Tamano_objeto[0], self.Posicion_objeto[1]]
                self.Imagen = self.Imagenes[0]
                self.Imagen = pygame.transform.scale(self.Imagen,(self.Size[0]+10,self.Size[1]+((12*self.Size[1])/100)))
                pos_y = 5
                for q in lineas:
                    render = self.Font.render(q,1,(0,0,0))
                    self.Imagen.blit(render,(self.Imagen.get_size()[0]/2-render.get_size()[0]/2, pos_y))
                    pos_y += render.get_size()[1] + 5
                Pantalla.blit(self.Imagen,(Posic[0],Posic[1]-self.Size[1]))
    def crear_lineas(self,texto,ancho):
        if self.Font.render(texto,1,(0,0,0)).get_size()[0] > ancho:
            lineas = []
            palabras = []
            palabra = ""
            for q in texto:
                if q == " ":
                    palabras.append(palabra)
                    palabra = ""
                else:
                    palabra += q
            if palabra != "":
                palabras.append(palabra)
            end = False
            while not end:
                for q in range(len(palabras)):
                    test = ""
                    for w in range(q):
                        test += palabras[w] + " "
                    test2 = ""
                    for w in range(q+1):
                        test2 += palabras[w] + " "
                    n1 = self.Font.render(test,1,(0,0,0))
                    n2 = self.Font.render(test2,1,(0,0,0))
                    if n1.get_size()[0] <= ancho and n2.get_size()[0] >= ancho:
                        lineas.append(test)
                        for w in range(q):
                            del palabras[0]
                        break
                    if q == len(palabras)-1:
                        if len(palabras) > 0:
                            test = ""
                            for w in palabras:
                                test += w + " "
                            lineas.append(test)
                            end = True
            for q in range(len(lineas)):
                if lineas[q][len(lineas[q])-1] == " ":
                    lineas[q] = lineas[q][:len(lineas[q])-1]
            return lineas
        else:
            return [texto]
    def logic_update(self,Events):
        mouse = Events.get_mouse()
        x,y = mouse.get_position()
        configs = conf.obtener_data(self.profile)
        act = 1
        for q in configs:
            if q[0] == "Tutorial":
                act = q[1]
        if x > self.Posicion_objeto[0] and x < self.Posicion_objeto[0] + self.Tamano_objeto[0] and y > self.Posicion_objeto[1] and y < self.Posicion_objeto[1] + self.Tamano_objeto[1]:
            if not mouse.get_pressed()[0]:
                if act:
                    self.Enabled = True
            else:
                self.Enabled = False
        else:
            self.Enabled = False