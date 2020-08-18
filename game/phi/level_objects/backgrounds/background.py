from game.phi.level_objects.element import element
from utils.pfunctions import add_border
import generate,pygame,random

class background(element):
    def __init__(self,X,Y,cx,cy,name,type):
        img = pygame.Surface((50,50))
        self.speed = 5
        self.danino = False
        if type == 1:
            img.fill((0,133,255))
            img = add_border(img,2,2,2,2,(0, 0, 0))
            self.speed = 5
        elif type == 2:
            img.fill((255,222,0))
            for q in range(50):
                for w in range(50):
                    if random.randrange(0,6) == 2:
                        img.blit(pygame.Surface((1,1)),(q,w))
            self.speed = 2
        elif type == 3:
            img.fill((231,231,231))
            self.speed = 10
        elif type == 4:
            self.danino = 4
            img.fill((226,36,48))
            for q in range(50):
                for w in range(50):
                    if random.randrange(0,12) == 5:
                        img.blit(pygame.Surface((1,1)),(q,w))
        img = generate.generate_background(img,cx,cy)
        self._cx = cx
        self._cy = cy
        self._type = type
        self.element(X,Y,name,"background",[],img)