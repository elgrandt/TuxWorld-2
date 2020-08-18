class element:
    def element(self,X,Y,NAME,TYPE,TAGS,SURFACE):
        self._x = X
        self._y = Y
        
        self._CAMX = 0
        self._CAMY = 0
        
        self.NAME = NAME
        self.TYPE = TYPE
        self.TAGS = TAGS
        
        self.surface = SURFACE
        
        self.W, self.H = SURFACE.get_size();
        
        self.permitido_act = True
    def graphic_update(self,pantalla):
        if self.permitido_act:
            pantalla.blit(self.surface,(self._x - self._CAMX, self._y - self._CAMY))
        self.pgu(pantalla)
    def logic_update(self,events,UP):
        self.W, self.H = self.surface.get_size();
        self._CAMX, self._CAMY = UP._CAM.X, UP._CAM.Y
        return self.plu(events,UP)
    def pgu(self,pantalla):
        pass
    def plu(self,events,UP):
        pass
    def get_pos(self):
        return self._x,self._y
    def get_size(self):
        return self.W,self.H