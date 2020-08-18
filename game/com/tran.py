import game.phi.level_objects as lo
import copy

def ev(var,variables,j = 0):
    s = copy.deepcopy(var)
    for x in range(len(s)):
        for y in range(len(variables)):
            if variables[y][0] == s[x]:
                s[x] = str(variables[y][1])
    for q in range(len(s)):
        s[q] = search_variables(s[q],variables)
    for x in range(len(s)):
        s[x] = eval(s[x])
    return s

def search_variables(text,variables):
    var = False
    act = ""
    for q in range(len(text)):
        if text[q] == "%":
            if var == False:
                var = True
            else:
                act = act[1:]
                existe = False
                for w in variables:
                    if w[0] == act:
                        value = w[1]
                        if isinstance(value,int) or isinstance(value,list):
                            value = str(value)
                        new = text.replace("%"+act+"%",value)
                        existe = True
                        break
                if existe:
                    text = search_variables(new,variables)
                    break
        if var == True:
            act += text[q]
    return text

class inte:
    def __init__(self):
        self.variables = []
    def add_variable(self,name,value):
        self.variables.append([name,value])
    def change_value(self,name,value):
        for x in range(len(self.variables)):
            if self.variables[x][0] == name:
                self.variables[x][1] = value
    def transform(self,phrase):
        if phrase.title != "line" and phrase.title != "if":
            p = ev(phrase.content,self.variables)
        if (phrase.title == "background"): 
            element = lo.backgrounds.background.background(*p)
            return [element]
        elif (phrase.title == "wall"):
            element = lo.walls.clasic_wall(p[0],p[1], p[6], p[2], p[3], p[4],p[5])
            return [element]
        elif (phrase.title == "enemy"):
            element = lo.enemies.enemy.reEnemy(*p)
            return [element]
        elif (phrase.title == "coin"):
            element = lo.moneda.moneda( (p[0],p[1]), p[2], 1)
            return [element]
        elif (phrase.title == "esquina"):
            element = lo.walls.esquina.esquina(p[0],p[1],p[3],p[2])
            return [element]
        elif (phrase.title == "extra_life"):
            element = lo.vidas_extra.vida((p[0],p[1]),p[2])
            return [element]
        elif (phrase.title == "box"):
            element = lo.box.box((p[0],p[1]),p[2])
            return [element]
        elif (phrase.title == "bomb"):
            element = lo.bomb.bomb((p[0],p[1]),p[2])
            return [element]
        elif (phrase.title == "button"):
            element = lo.button.button(*p)
            return [element]
        elif (phrase.title == "puerta"):
            element = lo.puerta.puerta(*p)
            return [element]
        elif (phrase.title == "checkpoint"):
            element = lo.checkpoint.checkpoint(*p)
            return [element]
        elif (phrase.title == "teletransportador"):
            element = lo.teletransportador.teletransportador(*p)
            return [element]
        elif (phrase.title == "luz"):
            element = lo.luz.luz(*p)
            return [element]
        elif (phrase.title == "laser"):
            element = lo.laser.laser(*p)
            return [element]
        elif (phrase.title == "meta"):
            element = lo.meta.meta(*p)
            return [element]
        elif (phrase.title == "comentario"):
            pass
        elif (phrase.title == "line"):
            variable = phrase.params[0]
            opan = [phrase.params[1],phrase.params[2],phrase.params[3]]
            p = ev(opan,self.variables)
            elements = []
            self.add_variable(variable,p[0])
            for v in range(p[0],p[1],p[2]):
                self.change_value(variable,v)
                for a in range(len(phrase.content)):
                    el = self.transform(phrase.content[a])
                    if el != None:
                        for b in range(len(el)):
                            elements.append(el[b])
            self.variables.remove([variable,v])
            return elements
        elif (phrase.title[:6] == "player"):
            pass
        elif (phrase.title == "if"):
            resultado = False
            signo = phrase.params[1]
            del phrase.params[1]
            p = ev(phrase.params,self.variables)
            parte1 = p[0]
            parte2 = p[1]
            if signo == "<":
                resultado = parte1 < parte2
            elif signo == "==":
                resultado = parte1 == parte2
            elif signo == ">":
                resultado = parte1 > parte2
            if resultado:
                ele = []
                for q in range(len(phrase.content)):
                    res = self.transform(phrase.content[q])
                    if res != None:
                        for q in range(len(res)):
                            ele.append(res[q])
                return ele
        elif (phrase.title == "print"):
            act = ""
            for q in range(len(p)):
                act += str(p[q])
                if q != len(p)-1:
                    act += ", "
            print act
        else:
            if len(p) == 1:
                p = p[0]
            existe = False
            for q in self.variables:
                if q[0] == phrase.title:
                    existe = True
            if existe:
                self.change_value(phrase.title, p)
            else:
                self.add_variable(phrase.title, p)