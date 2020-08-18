
class limite:
    def __init__(self,LX,LY):
        self.LX,self.LY = LX,LY
    def analizar(self,pos):
        frenar1 = False
        frenar2 = False
        frenar3 = False
        frenar4 = False
        if pos[0] > self.LX[0]:
            frenar1 = True
        if pos[0] < self.LX[1]:
            frenar2 = True
        if pos[1] > self.LY[0]:
            frenar3 = True
        if pos[1] < self.LY[1]:
            frenar4 = True
        return [frenar1,frenar2,frenar3,frenar4]