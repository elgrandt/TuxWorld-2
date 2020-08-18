
def detectar(SELF,UP):
    hacker = False
    if not SELF.programador:
        paredes = []
        frenos = []
        for obj in UP.objetos:
            if obj.TYPE == "Wall":
                wall = False
                swall = False
                esquina = False
                for tag in obj.TAGS:
                    if tag == "Wall":
                        wall = True
                    elif tag == "SWall":
                        swall = True
                    elif tag == "Esquina":
                        esquina = True
                if wall and swall and not esquina:
                    if obj.ubic == "Freno":
                        frenos.append(obj)
                    else:
                        paredes.append(obj)

                    
        for p in paredes:
            fin = None
            fin_size = None
            for q in range(len(frenos)):
                _x,_y = frenos[q]._x,frenos[q]._y
                _w,_h = frenos[q].W,frenos[q].H
                if p.ubic == "Arriba":
                    if _y < p._y:
                        fin = _y + _h
                        fin_size = (_w,_h)
                if p.ubic == "Abajo":
                    if _y > p._y + p.H:
                        fin = _y
                        fin_size = (_w,_h)
                if p.ubic == "Izquierda":
                    if _x < p._x:
                        fin = _x + _w
                        fin_size = (_w,_h)
                if p.ubic =="Derecha":
                    if _x > p._x + p.W:
                        fin = _x
                        fin_size = (_w,_h)

            if fin == None:
                if p.ubic == "Arriba":
                    if SELF._y + 50 < p._y + p.H and SELF._x+SELF.W > p._x and SELF._x < p._x + p.W:
                        SELF._y = p._y + p.H
                elif p.ubic == "Abajo":
                    if SELF._y - SELF.H - 20 > p._y and SELF._x+SELF.W > p._x and SELF._x < p._x + p.W:
                        SELF._y = p._y - SELF.H
                elif p.ubic == "Izquierda":
                    if SELF._x + 15 < p._x + p.W and SELF._y+SELF.H > p._y and SELF._y < p._y + p.H:
                        SELF._x = p._x + p.W
                elif p.ubic == "Derecha":
                    if SELF._x + SELF.W - 15 > p._x and SELF._y+SELF.H > p._y and SELF._y < p._y + p.H:
                        SELF._x = p._x - SELF.W
            else:
                if p.ubic == "Arriba":
                    if SELF._y + 50 < p._y + p.H and SELF._x+SELF.W > p._x and SELF._x < p._x + p.W and SELF._y > fin + fin_size[1]:
                        SELF._y = p._y + p.H
                elif p.ubic == "Abajo":
                    if SELF._y - SELF.H - 20 > p._y and SELF._x+SELF.W > p._x and SELF._x < p._x + p.W and SELF._y + SELF.H < fin:
                        SELF._y = p._y - SELF.H
                elif p.ubic == "Izquierda":
                    if SELF._x + 15 < p._x + p.W and SELF._y+SELF.H > p._y and SELF._y < p._y + p.H and SELF._x > fin + fin_size[0]:
                        SELF._x = p._x + p.W
                elif p.ubic == "Derecha":
                    if SELF._x + SELF.W - 15 > p._x and SELF._y+SELF.H > p._y and SELF._y < p._y + p.H and SELF._x + SELF.W < fin:
                        SELF._x = p._x - SELF.W