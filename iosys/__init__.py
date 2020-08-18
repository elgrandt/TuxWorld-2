import thread
from events import events
import pygame
from pygame.locals import *

class iosys:
    def __init__(self,WIDTH,HEIGHT):
        from stage import stage
        print "iosys started"
        #CLOCK
        self.CLOCK = pygame.time.Clock()
        #OUTPUT
        self.SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),HWSURFACE|DOUBLEBUF|RESIZABLE)
        pygame.display.set_caption("Tux world")
        #INPUT
        self.EVENTS = events()
        #LOGIC
        self.STAGE = stage()
    
        self.on = True
        self.fullscreen = False
    def graphic_update(self):
        self.STAGE.graphic_update(self.SCREEN)
    def logic_update(self):
        command = self.STAGE.logic_update(self.EVENTS)
        self.analizar_comandos(command)
    def analizar_comandos(self,command):
        if command == "salir":
            self.on = False
        elif command == "restart":
            self.on = False
    def updating(self):
        while self.on == True:
            self.SCREEN.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on = False
                elif event.type == pygame.VIDEORESIZE:
                    if self.fullscreen == False:
                        pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                    else:
                        pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE|FULLSCREEN)
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_F11:
                        if self.fullscreen == False:
                            self.fullscreen = True
                            from Tkinter import Tk
                            root = Tk()
                            tam = root.maxsize()
                            pygame.display.set_mode(tam,HWSURFACE|DOUBLEBUF|RESIZABLE|FULLSCREEN)
                        else:
                            self.fullscreen = False
                            pygame.display.set_mode(pygame.display.get_surface().get_size(),HWSURFACE|DOUBLEBUF|RESIZABLE)
                    elif event.key == K_ESCAPE:
                        self.on = False
                
            self.EVENTS.update_mouse(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            self.EVENTS.update_keyboard(pygame.key.get_pressed())
            self.graphic_update()
            self.logic_update()
            
            pygame.display.update()
            
            self.CLOCK.tick(40)