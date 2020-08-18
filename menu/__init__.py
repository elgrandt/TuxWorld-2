import extra_data
import extra_data.fonts as ef
import extra_data.images as ei
import pygame, time, utils.pfunctions as pfunctions
import utils as u
import os

class mborder():
    def __init__(self,X,Y,W,H):
        self._x = X
        self._y = Y
        self.h = H
        self.w = W
        
        self._toX = X
        self._toY = Y
        
        self.surface = pygame.surface.Surface((W,H),pygame.SRCALPHA,32)
        u.pfunctions.add_border(self.surface, 2, 2, 2, 2, (0,0,0))
    def set_goto(self,pos):
        self._toX = pos[0]
        self._toY = pos[1]
    def graphic_update(self,pantalla):
        pantalla.blit(self.surface,(self._x,self._y))
    def logic_update(self,events):
        if self._x < self._toX:
            self._x+=5
        elif self._x > self._toX:
            self._x -=5
        
        if self._y < self._toY:
            self._y += 5
        elif self._y > self._toY:
            self._y -= 5

class select_option:
    def __init__(self,xp,y,names,options):
        
        self.options = options
     
        self.Tboton = (300,40)
        Tp = pygame.display.get_surface().get_size()
        xp = Tp[0]/2-self.Tboton[0]/2
        y = Tp[1]/2-((self.Tboton[1]+10)*len(self.options))/2
        
        self.buttons = []
        posy = y
        for x in range(len(self.options)):
            surface = pygame.surface.Surface(self.Tboton)
            surface.fill((247,211,88))
            text = ef.ubuntu_bold_graph.render(names[x],1,(0,0,0))
            surface.blit( text , ( ( surface.get_size()[0] - text.get_size()[0] ) / 2 , ( (surface.get_size()[1] - text.get_size()[1] ) / 2 ) ) )
           
            button = u.button.button([surface], (xp,posy), 0.1)
            self.buttons.append( button ) 
            posy += surface.get_size()[1] + 10
            
        self.mborder = mborder(xp,y,surface.get_size()[0],surface.get_size()[1])
        
        self.selected = 0
        self.LT = 0
        self.LT2 = 0
        self.LT3 = pygame.time.get_ticks()
        self.LT4 = pygame.time.get_ticks()
    def graphic_update(self,pantalla):
        Tp = pantalla.get_size()
        X = Tp[0]/2-self.Tboton[0]/2
        Y = Tp[1]/2-((self.Tboton[1]+10)*len(self.options))/2
        for x in range(len(self.buttons)):
            self.buttons[x].graphic_update(pantalla,(X,Y))
            Y += self.Tboton[1]+10
        self.mborder.graphic_update(pantalla)
    def logic_update(self,events):
        commands = []
        
        self.mborder.logic_update(events)
        rel = False
        for x in range(len(self.buttons)):
            self.buttons[x].logic_update(events)
            if self.buttons[x].on_release() == True:
                self.mborder.set_goto(self.buttons[x].get_position())
                rel = True
                self.selected = x
            if self.buttons[x].on_press() == True and pygame.time.get_ticks() > self.LT4 + 200:
                self.LT4 = pygame.time.get_ticks()
                commands.append(self.options[x])
        if rel == True:
            import extra_data.cursors as cursor
            pygame.mouse.set_cursor(*cursor.cursor1)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
        pressed = events.get_keyboard()
        
        if pygame.time.get_ticks() > self.LT + 200:
            if pressed[pygame.K_DOWN]:
                self.LT = pygame.time.get_ticks()
                if self.selected < len(self.buttons)-1:
                    self.mborder.set_goto(self.buttons[self.selected+1].get_position())
                    self.selected += 1
        if pygame.time.get_ticks() > self.LT2 + 200:
            if pressed[pygame.K_UP]:
                self.LT2 = pygame.time.get_ticks()
                if self.selected > 0:
                    self.mborder.set_goto(self.buttons[self.selected-1].get_position())
                    self.selected -= 1
                    
        if pressed[pygame.K_RETURN] and self.LT3+100 < pygame.time.get_ticks():
            self.LT3 = pygame.time.get_ticks()
            commands.append(self.options[self.selected])
        
        return commands
    
class background:
    def __init__(self,bks):
        import random
        self.bks = bks
        self.last = 0
        self.actual = random.randrange(len(self.bks))
        self.toNext = 500
        self.px = 0
    def graphic_update(self,pantalla):
        pantalla.blit(self.bks[self.last],(self.px-800,0))
        pantalla.blit(self.bks[self.actual],(self.px,0))
    def logic_update(self,events):
        self.bks[self.actual] = pygame.transform.scale(self.bks[self.actual], pygame.display.get_surface().get_size())
        if self.toNext > 0:
            self.toNext -= 1
        else:
            self.last = self.actual
            import random
            self.toNext = 500
            self.actual = random.randrange(len(self.bks))
            self.px = 800
        if self.px > 0:
            self.px -= 5

def crear_jugador(name):
    directorio = os.path.join("data/perfiles", name)
    if not os.path.isdir(directorio):
        os.mkdir(directorio)
        open("data/perfiles/"+name+"/data.conf","w")
        return False
    else:
        return True

def obtener_perfiles():
    direct = "data/perfiles/*"
    import glob
    profiles = glob.glob(direct)
    perfiles = []
    for q in range(len(profiles)):
        nombre = profiles[q][len(direct)-1:]
        perfiles.append(nombre)
    return perfiles

class seleccionar_perfil:
    def __init__(self,perfiles,commands,nuevo = True):
        self.commands = commands
        self.perfiles = perfiles
        self.tamano_y = 10
        for q in perfiles:
            self.tamano_y += 50
        self.tamano = (300,self.tamano_y)
        self.font = pygame.font.Font(ef.font3,30)
        self.font2 = pygame.font.Font(ef.font3,20)
        self.pos_perfiles = []
        self.LT = pygame.time.get_ticks()
        self.texto_subrayado = False
        self.pos_text = (0,0)
        self.nuevo = nuevo
    def graphic_update(self,pantalla):
        Tpantalla = pantalla.get_size()
        title = self.font.render("Seleccione perfil:",1,(255,255,0))
        self.pos = (Tpantalla[0]/2-self.tamano[0]/2,Tpantalla[1]/2-self.tamano[1]/2)
        pantalla.blit(title,(self.pos[0],self.pos[1]-35))
        pfunctions.rect(pantalla, self.pos, self.tamano, (0,0,0), 10, False, 4)
        y_act = 10
        for q in self.perfiles:
            pos_act = (self.pos[0]+10,self.pos[1]+y_act)
            tam_act = (self.tamano[0]-20,40)
            if not pygame.mouse.get_pressed()[0]:
                x,y = pygame.mouse.get_pos()
                if x > pos_act[0] and x < pos_act[0]+tam_act[0] and y > pos_act[1] and y < pos_act[1]+tam_act[1]:
                    pfunctions.boton_redondo(pantalla, pos_act, tam_act, 10, " "+q, False, 4, (255,0,0), (0,255,0), (0,0,0))
                else:
                    pfunctions.boton_redondo(pantalla, pos_act, tam_act, 10, " "+q, False, 4, (0,0,255), (0,255,0), (0,0,0))
            else:
                pfunctions.boton_redondo(pantalla, pos_act, tam_act, 10, " "+q, False, 4, (0,0,255), (0,255,0), (0,0,0))
            self.pos_perfiles.append((self.pos[0]+10,self.pos[1]+y_act))
            y_act += 50
        if self.texto_subrayado:
            self.font2.set_underline(True)
        else:
            self.font2.set_underline(False)
        if self.nuevo:
            self.texto = self.font2.render("Crear nuevo perfil",1,(97,161,250))
            self.pos_text = (Tpantalla[0]/2-self.texto.get_size()[0]/2,self.pos[1]+self.tamano[1]+10)
            pantalla.blit(self.texto,self.pos_text)
    def logic_update(self,events):
        mouse = events.get_mouse()
        x,y = mouse.get_position()
        if self.nuevo:
            if pygame.time.get_ticks() > self.LT+200:
                if x > self.pos_text[0] and x < self.pos_text[0]+self.texto.get_size()[0] and y > self.pos_text[1] and y < self.pos_text[1]+self.texto.get_size()[1]:
                    self.texto_subrayado = True
                    if mouse.get_pressed()[0]:
                        return ["NUEVO"+self.commands.replace("load","select_name")]
                else:
                    self.texto_subrayado = False
        if mouse.get_pressed()[0] and pygame.time.get_ticks() > self.LT+200:
            self.LT = pygame.time.get_ticks()
            for q in range(len(self.perfiles)):
                pos_act = self.pos_perfiles[q]
                tam_act = (self.tamano[0]-20,40)
                if x > pos_act[0] and x < pos_act[0]+tam_act[0] and y > pos_act[1] and y < pos_act[1]+tam_act[1]:
                    return [self.perfiles[q]+self.commands]
        return []

class menu():
    def __init__(self,version):
        self.version = version
        self.background = background(ei.load_backgrounds())
        
        self.text_title = pygame.surface.Surface(pygame.display.get_surface().get_size(),pygame.SRCALPHA, 32)
        self.text_title.convert_alpha()
        text = extra_data.fonts.ubuntu_bold_title.render("Tux world",1,(33,179,204))
                                                
        self.text_title.blit(text,( ( self.text_title.get_size()[0] - text.get_size()[0] ) / 2, ( self.text_title.get_size()[1] - text.get_size()[1] ) / 2 - pygame.display.get_surface().get_size()[1]/3))
        
        version = extra_data.fonts.ubuntu_bold_graph.render(version,1,(33,179,204))
        
        self.text_title.blit(version, ( ( self.text_title.get_size()[0] - version.get_size()[0] ) / 2 , ( self.text_title.get_size()[1] - text.get_size()[1] ) / 2 + text.get_size()[1] + 5 - pygame.display.get_surface().get_size()[1]/3) )
        
        self.select_option = select_option( ( self.text_title.get_size()[0] - 300 ) / 2 ,200,["New game","Multiplayer","Creadores"],["new game","multiplayer","creadores"])
        self.type_act = None
        self.es_menu = True
    def graphic_update(self,pantalla):
        self.background.graphic_update(pantalla)
        self.select_option.graphic_update(pantalla)
        pantalla.blit(self.text_title,(0,0))
        self.pantalla = pantalla
    def logic_update(self,events):
        self.text_title = pygame.surface.Surface(pygame.display.get_surface().get_size(),pygame.SRCALPHA, 32)
        self.text_title.convert_alpha()
        text = extra_data.fonts.ubuntu_bold_title.render("Tux world",1,(33,179,204))
        self.text_title.blit(text,( ( self.text_title.get_size()[0] - text.get_size()[0] ) / 2, ( self.text_title.get_size()[1] - text.get_size()[1] ) / 2 - pygame.display.get_surface().get_size()[1]/3))
        version = extra_data.fonts.ubuntu_bold_graph.render(self.version,1,(33,179,204))
        self.text_title.blit(version, ( ( self.text_title.get_size()[0] - version.get_size()[0] ) / 2 , ( self.text_title.get_size()[1] - text.get_size()[1] ) / 2 + text.get_size()[1] + 5 - pygame.display.get_surface().get_size()[1]/3) )
        
        self.background.logic_update(events)
        if self.type_act == "Input":
            Tpantalla = pygame.display.get_surface().get_size()
            self.select_option.Size = (Tpantalla[0]-Tpantalla[0]/4,40)
            self.select_option.Position = (Tpantalla[0]/8,Tpantalla[1]/2-20)
        coms = self.select_option.logic_update(events)
        
        import glob
        import re
        if len(coms) > 0:
            if coms[0] == "new game":
                files = glob.glob("data/levels/*")
                fls = []
                comss = []
                for x in range(len(files)):
                    fl = files[x]
                    comss.append("select_name_game"+fl)
                    fls.append(re.sub("data/levels", "", fl))
                self.select_option = select_option( ( self.text_title.get_size()[0] - 300 ) / 2 ,200,fls,comss)
            if coms[0].find("select_name_game") != -1:
                perfiles = obtener_perfiles()
                self.fl = coms[0][coms[0].find("select_name_game")+len("select_name_game"):]
                if len(perfiles) == 0 or coms[0][:len("NUEVO")] == "NUEVO":
                    Tpantalla = pygame.display.get_surface().get_size()
                    self.select_option = pfunctions.Input(pygame.display.get_surface(),"Nombre de usuario",(Tpantalla[0]-Tpantalla[0]/4,40),(Tpantalla[0]/8,Tpantalla[1]/2-20),"crear"+self.fl,(255,0,0))
                    self.select_option.Font_size = 40
                    self.type_act = "Input"
                else:
                    self.select_option = seleccionar_perfil(perfiles,"load"+self.fl)
            if coms[0][:len("select_name_ngame")] == "select_name_ngame":
                perfiles = obtener_perfiles()
                self.fl = coms[0][len("select_name_ngame"):]
                if len(perfiles) == 0 or coms[0][:len("NUEVO")] == "NUEVO":
                    Tpantalla = pygame.display.get_surface().get_size()
                    self.select_option = pfunctions.Input(pygame.display.get_surface(),"Nombre de usuario",(Tpantalla[0]-Tpantalla[0]/4,40),(Tpantalla[0]/8,Tpantalla[1]/2-20),"crear"+self.fl,(255,0,0))
                    self.select_option.Font_size = 40
                    self.type_act = "Input"
                else:
                    self.select_option = seleccionar_perfil(perfiles,"edit_level"+self.fl,False)
            if coms[0][:len("select_name_nlvl")] == "select_name_nlvl":
                perfiles = obtener_perfiles()
                self.fl = coms[0][len("select_name_nlvl"):]
                if len(perfiles) == 0 or coms[0][:len("NUEVO")] == "NUEVO":
                    Tpantalla = pygame.display.get_surface().get_size()
                    self.select_option = pfunctions.Input(pygame.display.get_surface(),"Nombre de usuario",(Tpantalla[0]-Tpantalla[0]/4,40),(Tpantalla[0]/8,Tpantalla[1]/2-20),"new level",(255,0,0))
                    self.select_option.Font_size = 40
                    self.type_act = "Input"
                else:
                    self.select_option = seleccionar_perfil(perfiles,"new level",False)
            if coms[0] == "creadores":
                files = glob.glob("data/levels/*")
                fls = []
                comms = []
                for x in range(len(files)):
                    fl = files[x]
                    comms.append("select_name_ngame"+fl)
                    fls.append(re.sub("data/levels", "", fl))
                test = pygame.font.Font(ef.font3,20).render("Nuevo nivel",1,(0,0,0)).get_size()
                buttons_y = (40+10) * len(fls)
                pos_link = (self.pantalla.get_size()[0]/2-test[0]/2,self.pantalla.get_size()[1]/2+buttons_y/2 + 10)
                self.select_option = pfunctions.multiple_actualizacion([select_option((self.text_title.get_size()[0]-300)/2,200,fls,comms),pfunctions.link(pos_link,"Nuevo nivel",["select_name_nlvl"])])
            if coms[0].find("crear") != -1:
                new_name = coms[0][:coms[0].find("crear")]
                existe = crear_jugador(new_name)
                if not existe:
                    coms[0] = coms[0].replace("crear","load")
                else:
                    self.select_option.publicar_error("El usuario ya existe")
            if coms[0] == "multiplayer":
                self.select_option = select_option( ( self.text_title.get_size()[0] - 300 ) / 2 ,200,["Test A","Test B"],["Test A","Test B"])
            elif coms[0] == "Test A":
                files = glob.glob("data/levels/*")
                fls = []
                comms = []
                for x in range(len(files)):
                    fl = files[x]
                    comms.append("test A "+fl)
                    fls.append(re.sub("data/levels", "", fl))
                
                self.select_option = pfunctions.multiple_actualizacion([select_option((self.text_title.get_size()[0]-300)/2,200,fls,comms)])
            elif coms[0] == "Test B":
                pass
            else:
                return coms[0]