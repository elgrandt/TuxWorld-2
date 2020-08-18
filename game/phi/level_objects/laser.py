import element, pygame, extra_data.images as img

class laser(element.element):
    def __init__(self,x,y,direccion,velocidad,name,mobile=True):
        self.mobile = mobile
        self.surf = img.laser
        self.disparo = pygame.Surface((30,10))
        self.dir = direccion
        if self.dir == 0:
            self.pos_inicial = [x + self.surf.get_size()[0], y + self.surf.get_size()[1] / 2 - self.disparo.get_size()[1] / 2]
        if self.dir == 1:
            self.surf = pygame.transform.rotate(self.surf,270)
            self.disparo = pygame.transform.rotate(self.disparo,90)
            self.pos_inicial = [x + self.surf.get_size()[0] / 2 - self.disparo.get_size()[0] / 2, y + self.surf.get_size()[1]]
        if self.dir == 2:
            self.surf = pygame.transform.rotate(self.surf,180)
            self.pos_inicial = [x,y + self.surf.get_size()[1] / 2 - self.disparo.get_size()[1] / 2]
        if self.dir == 3:
            self.surf = pygame.transform.rotate(self.surf,90)
            self.disparo = pygame.transform.rotate(self.disparo,90)
            self.pos_inicial = [x + self.surf.get_size()[0] / 2 - self.disparo.get_size()[0] / 2,y]
        self.element(x, y, name, "Laser", [], self.surf)
        self.choco_wall = False
        self.pos_disparo = [self.pos_inicial[0],self.pos_inicial[1]]
        self.vel = velocidad
        self.up = None
    def pgu(self, pantalla):
        if self.up != None and self.mobile:
            pantalla.blit(self.disparo,[self.pos_disparo[0] - self.up._CAM.X, self.pos_disparo[1] - self.up._CAM.Y])
    def plu(self,events,up):
        self.up = up
        for obj in up.objetos:
            pared = False
            if obj.TYPE == "Wall":
                for q in obj.TAGS:
                    if q == "SWall":
                        pared = True
                    if q == "Esquina":
                        pared = False
            if self.dir == 0 or self.dir == 2:
                question = self.pos_disparo[0] + self.disparo.get_size()[0] > obj._x and self.pos_disparo[0] < obj._x + obj.W and self.pos_inicial[1] + self.disparo.get_size()[1] > obj._y and self.pos_inicial[1] < obj._y + obj.H
            if self.dir == 1 or self.dir == 3:
                question = self.pos_inicial[0] + self.disparo.get_size()[0] > obj._x and self.pos_inicial[0] < obj._x + obj.W and self.pos_disparo[1] + self.disparo.get_size()[1] > obj._y and self.pos_disparo[1] < obj._y + obj.H
            if question:
                if pared:
                    self.choco_wall = True
                if obj.TYPE == "jugador":
                    if obj.principal:
                        if obj.restar_energia(4):
                            pared = True
        if self.choco_wall:
            self.choco_wall = False
            self.pos_disparo = [self.pos_inicial[0],self.pos_inicial[1]]
        if self.dir == 0:
            self.pos_disparo[0] += self.vel
        elif self.dir  == 1:
            self.pos_disparo[1] += self.vel
        elif self.dir == 2:
            self.pos_disparo[0] -= self.vel
        elif self.dir == 3:
            self.pos_disparo[1] -= self.vel