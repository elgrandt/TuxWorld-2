import pygame
from extra_data.fonts import *
import string
pygame.font.init()

ARRIBA = 1
ABAJO = 2
DERECHA = 3
IZQUIERDA = 4

def add_border(surface,w1 = 1,w2 = 1,w3 = 1,w4 = 1,color = (0,0,0)):
    w,h = surface.get_size()
    
    b1 = pygame.surface.Surface((w,w1))
    b1.fill(color)
    b2 = pygame.surface.Surface((w2,h))
    b2.fill(color)
    b3 = pygame.surface.Surface((w,w3))
    b3.fill(color)
    b4 = pygame.surface.Surface((w4,h))
    b4.fill(color)
    
    surface.blit(b1,(0,0))
    surface.blit(b2,(w-w2,0))
    surface.blit(b3,(0,h-w3))
    surface.blit(b4,(0,0))
    
    return surface

def boton(Tboton = (0,0), text = "", centrado = True, ancho_borde = [1,1,1,1], color_boton = (255,255,255), color_letra = (0,0,0), color_borde = (0,0,0), Tletra = 30, transparencia = False):
    Sboton = pygame.Surface(Tboton)
    Sboton.fill(color_boton)
    if transparencia != False:
        Sboton.set_alpha(transparencia)
    Sboton = add_border(Sboton, ancho_borde[0], ancho_borde[1], ancho_borde[2], ancho_borde[3], color_borde)
    font1 = pygame.font.Font("data/fonts/Ubuntu-B.ttf",Tletra)
    Stext = font1.render(text,1,color_letra)
    Ttext = Stext.get_size()
    if centrado == True:
        Ptext = (Tboton[0]/2-Ttext[0]/2, Tboton[1]/2-Ttext[1]/2)
    else:
        Ptext = (3, Tboton[1]/2-Ttext[1]/2)
    Sboton.blit(Stext,Ptext)
    return Sboton

def rect(surface,pos,tam=(0,0),color=(0,0,0),radio=0,transparente=False, ancho = 1):
    if transparente == False:
        pygame.draw.rect(surface, color, (pos[0]+radio,pos[1],tam[0]-radio*2,tam[1]))
        pygame.draw.rect(surface, color, (pos[0],pos[1]+radio,tam[0],tam[1]-radio*2))
        pygame.draw.ellipse(surface, color, (pos[0],  pos[1],   radio*2,   radio*2))
        pygame.draw.ellipse(surface, color, (pos[0]+tam[0]-radio*2,  pos[1],   radio*2,   radio*2))
        pygame.draw.ellipse(surface, color, (pos[0],  pos[1]+tam[1]-radio*2,   radio*2,   radio*2))
        pygame.draw.ellipse(surface, color, (pos[0]+tam[0]-radio*2,  pos[1]+tam[1]-radio*2,   radio*2,   radio*2))
    else:
        pi = 3.14159265359
        radio1 = radio*2
        pygame.draw.arc(surface, color, (pos[0],pos[1],radio1,radio1), pi/2, pi,ancho)
        pygame.draw.arc(surface, color, (pos[0]+tam[0]-radio1,pos[1],radio1,radio1), 0, pi/2,ancho)
        pygame.draw.arc(surface, color, (pos[0],pos[1]+tam[1]-radio1,radio1,radio1), pi, 1.5*pi,ancho)
        pygame.draw.arc(surface, color, (pos[0]+tam[0]-radio1,pos[1]+tam[1]-radio1,radio1,radio1), 1.5*pi, 2*pi,ancho)
        pygame.draw.line(surface, color, (pos[0]+radio,pos[1]), (pos[0]+tam[0]-radio,pos[1]), ancho)
        pygame.draw.line(surface, color, (pos[0],pos[1]+radio), (pos[0],pos[1]+tam[1]-radio), ancho)
        pygame.draw.line(surface, color, (pos[0]+tam[0]-ancho+1,pos[1]+radio), (pos[0]+tam[0]-ancho+1,pos[1]+tam[1]-radio), ancho)
        pygame.draw.line(surface, color, (pos[0]+radio,pos[1]+tam[1]-ancho+1), (pos[0]+tam[0]-radio,pos[1]+tam[1]-ancho+1), ancho)

def boton_redondo(surface, pos, Tboton = (0,0), radio = 20, text = "", centrado = True, ancho_borde = 1, color_boton = (255,255,255), color_letra = (0,0,0), color_borde = (0,0,0),tamano_fuente = 20):
    rect(surface, pos, Tboton, color_boton, radio, False)
    rect(surface, pos, Tboton, color_borde, radio, True, ancho_borde)
    fuente = pygame.font.Font(font3,tamano_fuente)
    Stext = fuente.render(text,1,color_letra)
    Ttext = Stext.get_size()
    if centrado == True:
        Ptext = (Tboton[0]/2-Ttext[0]/2, Tboton[1]/2-Ttext[1]/2)
    else:
        Ptext = (3, Tboton[1]/2-Ttext[1]/2)
    surface.blit(Stext,(pos[0]+Ptext[0], pos[1]+Ptext[1]))

def get_element(lis,name):
    for x in range(len(lis)):
        if lis[x].NAME == name:
            return lis[x]

def get_size(lis,name):
    return get_element(lis, name).get_size()

def get_pos(lis,name):
    return get_element(lis, name).get_pos()

def get_element_type(lis,typ):
    devolver = []
    for q in lis:
        if q.TYPE == typ:
            devolver.append(q)
    if len(devolver) == 0:
        return None
    else:
        return devolver
    
def colicion_detection(element1,element2):
    lados = []
    if (element1._x >= element2._x and element1._x  <= element2._x + element2.W) or (element1._x + element1.W >= element2._x and element1._x + element1.W <= element2._x + element2.W):
        if (element1._y >= element2._y and element1._y <= element2._y + element2.H) or (element1._y + element1.H >= element2._y and element1._y + element1.H <= element2._y + element2.H):
            if (element1._x - element2._x < 30):
                lados.append(IZQUIERDA)
            if ((element2._x + element2.W) - (element1._x + element1.W ) < 30):
                lados.append(DERECHA)
            if (element1._y - element2._y < 30):
                lados.append(ARRIBA)
            if (element2._y + element2.H) - (element1._y + element1.H) < 30:
                lados.append(ABAJO)
    return lados

def Get_written(Pressed):
    Ret = []
    for q in range(len(Pressed)):
        if Pressed[q]:
            Name = pygame.key.name(q)
            if (q >= 65 and q <= 90) or (q >= 97 and q <= 122) or (q >= 48 and q <= 57):
                Ret.append(chr(q))
            elif q == 8:
                Ret.append("Backspace")
            elif q == 32:
                Ret.append(" ")
            elif q == 13:
                Ret.append("Enter")
            elif Name[:1] == "[":
                Ret.append(Name[1:2])
            else:
                if Name == "right shift" or Name == "left shift":
                    Shift_keys = [["0","="],["1","!"],["3","#"],["4","$"],["5","%"],["6","&"],["7","/"],["8","("],["9",")"]]
                    for l in range(len(string.ascii_lowercase)):
                        Shift_keys.append([string.ascii_lowercase[l],string.ascii_uppercase[l]])
                    Comp = False
                    Cant_pressed = 1
                    while Comp != True:
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                                Cant_pressed -= 1
                                if Cant_pressed == 0:
                                    Comp = True
                            elif event.type == pygame.KEYDOWN:
                                Cant_pressed += 1
                                Pressed2 = pygame.key.get_pressed()
                                for w in range(len(Pressed2)):
                                    if Pressed2[w]:
                                        Name2 = pygame.key.name(w)
                                        for e in Shift_keys:
                                            if Name2 == e[0]:
                                                Ret.append(e[1])
            break
    return Ret

class Input:
    def __init__(self,Surface,Title = "",Size = (1,1),Position = (0,0),Command = "",Color = (255,255,255)):
        self.Command = Command
        Title = Title + ":"
        self.Title = Title
        self.Size = Size
        self.Position = Position
        self.Color = Color
        comp = False
        size_act = 1
        while not comp:
            font_test = pygame.font.Font(font3,size_act)
            test = font_test.render("Test",1,(0,0,0))
            if test.get_size()[1] > self.Size[1]:
                comp = True
                size_act -= 3
            size_act += 1
        self.Font_size = size_act
        self.Font = pygame.font.Font(font3,self.Font_size)
        self.Stitle = self.Font.render(self.Title, 1, (0,0,255))
        self.Title_size = self.Stitle.get_size()
        self.Input = pygame.Surface(self.Size)
        self.Input.fill(self.Color)
        self.Input = add_border(self.Input,2,2,2,2,(0,0,0))
        self.Cursor = pygame.Surface((2,self.Size[1] - 6))
        self.Surface = Surface
        self.Cursor_active = False
        self.Last_time = 0
        self.Last_time2 = 0
        self.Written = ""
        self.Sended = False
        self.Selected = True
        self.Position_input = (self.Position[0] + 10, self.Position[1] + self.Title_size[1] + 13)
        self.Last_pressed = pygame.key.get_pressed()
        self.error = ""
    def publicar_error(self,error):
        self.error = error
    def graphic_update(self,pantalla):
        self.Font = pygame.font.Font(font3,self.Font_size)
        self.Stitle = self.Font.render(self.Title, 1, (0,0,255))
        self.Title_size = self.Stitle.get_size()
        self.Input = pygame.Surface(self.Size)
        self.Input.fill(self.Color)
        self.Input = add_border(self.Input,2,2,2,2,(0,0,0))
        self.Cursor = pygame.Surface((2,self.Size[1] - 6))
        Test = self.Font.render(self.Written, 1, (0,0,0))
        if Test.get_size()[0] > self.Size[0]-8:
            Text_act = self.Written
            while Test.get_size()[0] > self.Size[0]-8:
                Text_act = Text_act[1:]
                Test = self.Font.render(Text_act,1,(0,0,0))
            Text = Text_act
        else:
            Text = self.Written
        self.Swritten = self.Font.render(Text, 1, (0,0,0))
        self.Text_size = self.Swritten.get_size()
        self.Position_input = (self.Position[0] + 10, self.Position[1] + self.Title_size[1] + 13)
        self.Position_cursor = (self.Position_input[0]+6+self.Text_size[0],self.Position_input[1] + (self.Input.get_size()[1]/2 - self.Cursor.get_size()[1]/2))
        self.Surface.blit(self.Stitle,(self.Position[0] + 10,self.Position[1] + 10))
        self.Surface.blit(self.Input,self.Position_input)
        self.Surface.blit(self.Swritten,(self.Position_input[0]+4,self.Position_input[1]+(self.Input.get_size()[1]/2-self.Text_size[1]/2)))
        Time = pygame.time.get_ticks()
        if Time > self.Last_time + 300:
            self.Last_time = Time
            if self.Cursor_active:
                self.Cursor_active = False
            else:
                self.Cursor_active = True
        if self.Cursor_active and self.Selected:
            self.Surface.blit(self.Cursor,self.Position_cursor)
        self.text_error = self.Font.render(self.error,1,(255,255,0))
        self.Surface.blit(self.text_error,(self.Surface.get_size()[0]/2-self.text_error.get_size()[0]/2,self.Position_input[1]+self.Size[1]+10))
    def logic_update(self,events):
        if self.Selected:
            Pressed = events.get_keyboard()
            if Pressed != self.Last_pressed:
                self.Last_pressed = Pressed
                Written1 = Get_written(Pressed)
                for Written in Written1:
                    if Written == "Backspace":
                        self.Written = self.Written[:len(self.Written)-1]
                    elif Written == "Enter":
                        return [self.Written+self.Command]
                    else:
                        self.Written += Written
        mouse = events.get_mouse()
        if mouse.left:
            Pos = (mouse.x,mouse.y)
            Global_input_pos = self.Position_input
            if Pos[0] > Global_input_pos[0] and Pos[0] < Global_input_pos[0] + self.Input.get_size()[0] and Pos[1] > Global_input_pos[1] and Pos[1] < Global_input_pos[1] + self.Input.get_size()[1]:
                self.Selected = True
            else:
                self.Selected = False
        return []

class window:
    def __init__(self,tamano,color,titulo,buttons):
        self.tamano = tamano
        self.iniciado = False
        self.iniciado2 = False
        self.color = color
        self.titulo = titulo
        self.moviendo = False
        self.borrado = False
        self.buttons = buttons
    def graphic_update(self,pantalla):
        if not self.borrado:
            self.pantalla = pantalla
            self.iniciado2 = True
            if self.iniciado:
                self.fondo = pygame.Surface(self.tamano)
                self.fondo.fill(self.color)
                self.fondo = add_border(self.fondo,2,2,2,2,(0,0,0))
                
                self.Sparte_arriba = (self.tamano[0],30)
                self.parte_arriba = pygame.Surface(self.Sparte_arriba)
                self.parte_arriba.fill((80,212,238))
                self.parte_arriba = add_border(self.parte_arriba, 2, 2, 2, 2, (0,0,0))
                
                self.font = pygame.font.Font(font3,20)
                titulo = self.font.render(self.titulo,1,(0,0,0))
                self.parte_arriba.blit(titulo,(5,(self.parte_arriba.get_size()[1]/2-titulo.get_size()[1]/2)))
                
                self.Scruz = (20,20)
                self.Pcruz = (self.Sparte_arriba[0]-self.Scruz[0]-5,self.Sparte_arriba[1]/2-self.Scruz[1]/2)
                boton_redondo(self.parte_arriba, self.Pcruz, self.Scruz, self.Scruz[0]/2, "X", True, 2, (255,0,0), (0,0,0), (0,0,0), 12)
                
                self.fondo.blit(self.parte_arriba,(0,0))
                
                pantalla.blit(self.fondo,(self._x,self._y))
    def logic_update(self,events,UP):
        if not self.borrado:
            self.iniciado = True
            self.UP = UP
            self.events = events
            mouse = self.events.get_mouse()
            if self.iniciado2:
                x,y = mouse.get_position()
                if mouse.get_pressed()[0]:
                    if x > self._x and x < self._y+self.Sparte_arriba[0] and y > self._y and y < self._y+self.Sparte_arriba[1]:
                        if self.moviendo == False:
                            self.disferencia = (x-self._x,y-self._y)
                        self.moviendo = True
                    if self.moviendo:
                        self._x = x - self.disferencia[0]
                        self._y = y - self.disferencia[1]
                    if x > self._x + self.Pcruz[0] and x < self._x + self.Pcruz[0] + self.Scruz[0] and y > self._y + self.Pcruz[1] and y < self._y + self.Pcruz[1] + self.Scruz[1]:
                        self.borrado = True
                else:
                    self.moviendo = False
            else:
                self._x,self._y = mouse.get_position()


class link:
    def __init__(self,pos,texto,command,tamano=20):
        self.text = texto
        self.command = command
        self.pos = pos
        self.tamano = tamano
        self.hover = False
        self.iniciado = False
        self.clicked = False
    def graphic_update(self,pantalla):
        self.font = pygame.font.Font(font3,self.tamano)
        self.font.set_underline(False)
        if self.hover:
            self.font.set_underline(True)
        if not self.clicked:
            text = self.font.render(self.text,1,(0,0,255))
        else:
            text = self.font.render(self.text,1,(0,255,0))
        self.size = text.get_size()
        pantalla.blit(text,self.pos)
        self.iniciado = True
    def logic_update(self,events):
        if self.iniciado:
            mouse = events.get_mouse()
            clicked = mouse.get_pressed()
            x,y = mouse.get_position()
            self.clicked = False
            if x > self.pos[0] and x < self.pos[0]+self.size[0] and y > self.pos[1] and y < self.pos[1]+self.size[1]:
                self.hover = True
                if clicked[0]:
                    self.clicked = True
                    return self.command
            else:
                self.hover = False


class multiple_actualizacion:
    def __init__(self,clases):
        self.clases = clases
    def graphic_update(self,pantalla):
        devs = []
        for q in self.clases:
            devs.append(q.graphic_update(pantalla))
        for q in devs:
            if q != None:
                return q
    def logic_update(self,events):
        devs = []
        for q in self.clases:
            devs.append(q.logic_update(events))
        for w in devs:
            if w != None and w != []:
                return w
        return []
    
def get_players(objetos):
    js = []
    for x in range(len(objetos)):
        if objetos[x].TYPE == "Jugador":
            js.append(objetos[x])
    return js