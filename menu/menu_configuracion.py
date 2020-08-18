import pygame, extra_data.fonts as font, utils.pfunctions as pf
import extra_data.images as img
import utils.config_data as config_data

class config:
    def __init__(self,perfil):
        self.font = pygame.font.Font(font.font3,15)
        self.botones = []
        self.img_encendido = img.boton_configuracion_on
        self.img_apagado = img.boton_configuracion_off
        self.solto = True
        defaults = config_data.obtener_data(perfil)
        self.configs = []
        for q in range(len(defaults)):
            self.configs.append(defaults[q][0])
            if defaults[q][1]:
                imagen = self.img_encendido
            else:
                imagen = self.img_apagado
            self.botones.append([imagen,[0,0]])
        self.activo = False
        self.perfil = perfil
    def graphic_update(self,pantalla):
        self.boton = img.boton_configuracion
        self.Pboton = (pantalla.get_size()[0]-self.boton.get_size()[0]-5,5)
        pantalla.blit(self.boton,self.Pboton)
        if self.activo:
            self.Sfondo = [300,10]
            for q in self.configs:
                test = self.font.render(q,1,(0,0,0))
                if test.get_size()[0] > self.Sfondo[0]:
                    self.Sfondo[0] = test.get_size()[0]
                self.Sfondo[1] += test.get_size()[1] + 10
            self.fondo = pygame.Surface(self.Sfondo)
            self.fondo.fill((215,211,211))
            self.fondo = pf.add_border(self.fondo, 4, 4, 4, 4, (170,170,170))
            self.Pfondo = [pantalla.get_size()[0] - 5 - self.Sfondo[0],5 + self.boton.get_size()[1]]
            y_act = 10
            barra = pygame.Surface((self.Sfondo[0]-10,2))
            for q in range(len(self.configs)):
                render = self.font.render(self.configs[q],1,(0,0,0))
                self.fondo.blit(render,(10,y_act))
                if y_act != 10:
                    self.fondo.blit(barra,(5,y_act - 6))
                pos_boton = (self.Sfondo[0]-10-self.botones[q][0].get_size()[0],y_act + render.get_size()[1]/2 - self.botones[q][0].get_size()[1]/2)
                self.botones[q][1] = pos_boton
                self.fondo.blit(self.botones[q][0],pos_boton)
                y_act += render.get_size()[1] + 10
            
            pantalla.blit(self.fondo,self.Pfondo)
    def logic_update(self,events,up):
        mouse = events.get_mouse()
        x,y = mouse.get_position()
        for q in pygame.event.get():
            if q.type == pygame.MOUSEBUTTONUP:
                self.solto = True
        if self.activo:
            presiono = False
            if mouse.get_pressed()[0]:
                for w in range(len(self.botones)):
                    q = self.botones[w]
                    global_pos = self.Pfondo
                    if x > global_pos[0] + q[1][0] and x < global_pos[0] + q[1][0] + q[0].get_size()[0] and y > global_pos[1] + q[1][1] and y < global_pos[1] + q[1][1] + q[0].get_size()[1]:
                        if self.solto:
                            presiono = True
                            self.solto = False
                            if q[0] == self.img_apagado:
                                self.botones[w][0] = self.img_encendido
                            elif q[0] == self.img_encendido:
                                self.botones[w][0] = self.img_apagado
                            else:
                                print "Error"
                            dat = []
                            for q in range(len(self.botones)):
                                active = False
                                if self.botones[q][0] == self.img_apagado:
                                    active = 0
                                elif self.botones[q][0] == self.img_encendido:
                                    active = 1
                                else:
                                    print "Error 2"
                                dat.append([self.configs[q],active])
                            config_data.grabar_data(dat, self.perfil)
                if not presiono:
                    if not(x > self.Pfondo[0] and x < self.Pfondo[0] + self.Sfondo[0] and y > self.Pfondo[1] and y < self.Pfondo[1] + self.Sfondo[1]):
                        self.activo = False
        else:
            if mouse.get_pressed()[0]:
                if x > self.Pboton[0] and x < self.Pboton[0] + self.boton.get_size()[0] and y > self.Pboton[1] and y < self.Pboton[1] + self.boton.get_size()[1]:
                    if self.activo:
                        self.activo = False
                    else:
                        self.activo = True