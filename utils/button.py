from iosys import events
import pygame

class button:
    def __init__(self,img_list,position,frec = 0.01):
        self.img_list = img_list
        
        self.x,self.y = position
        
        self.state = 0
        self.frec = frec
        self.item = 0
        
        self.pressed = False
        self.released = False
    def graphic_update(self,SCREEN,pos):
        self.x,self.y = pos
        SCREEN.blit(self.img_list[self.state],(self.x,self.y))
    
    def logic_update(self,EVENTS):
        
        condicion1 = EVENTS.mouse.x > self.x and EVENTS.mouse.x < self.x + self.img_list[self.state].get_size()[0];
        condicion2 = EVENTS.mouse.y > self.y and EVENTS.mouse.y < self.y + self.img_list[self.state].get_size()[1];
        
        if (condicion1 and condicion2):
            self.released = True
            
            self.item += 1
            self.state = int(self.item * self.frec)
            
            if self.state >= len(self.img_list):
                self.state = len(self.img_list) - 1
                
            if (EVENTS.mouse.left == True):
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.released = False
            self.pressed = False
            self.state = 0
            self.item = 0
    def get_position(self):
        return self.x,self.y
    def on_press(self):
        return self.pressed
    def on_release(self):
        return self.released