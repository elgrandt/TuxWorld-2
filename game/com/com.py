import re
import game.phi.level_objects as lo
import tran

class level_reading:
    def __init__(self,name,author,description,areas):
        self.name = name
        self.author = author
        self.description = description
        self.areas = areas
    
def search_variable(lis,name,typ,arr=False):
    variables = []
    for x in range(len(lis)):
        if (lis[x].title == name and lis[x].TYPE == typ):
            variables.append(lis[x])
    if not arr:
        if len(variables) >= 1:
            return variables[0]
        else:
            return None
    else:
        return variables
 
def separate(s):
    lis = [""]
    for x in range(len(s)):
        if (s[x] == " "):
            lis.append([""])
        else:
            lis[len(lis)-1] += s[x]
    for x in range(len(lis)):
        if (lis[x] == "" or lis[x] == " "):
            del lis[x]
    return lis
    
def svs(lis,name,typ):
    elements = []
    for x in range(len(lis)):
        if (lis[x].title == name and lis[x].TYPE == typ):
            elements.append(lis[x])
    return elements

def create_level(s,player):
    lvl = search_variable(s,"level","draw")
    data = search_variable(lvl.content,"name","dec").content
    name = ""
    for q in data:
        name += q
    data = ""
    for q in name:
        if q != "'":
            data += q
    name = data
    author = search_variable(lvl.content,"author","dec").content[0]
    description = search_variable(lvl.content,"description","dec").content[0]
    areasn = search_variable(lvl.content,"arenas","dec").content
    areas = []
    for x in range(len(areasn)):
        areas.append(search_variable(s,areasn[x],"draw"))
    interpretador = tran.inte()
    elm = []
    for x in range(len(areas)):
        players = []
        b = 1
        while True:
            p = search_variable(areas[x].content,"player"+str(b),"dec")
            if (p == None):
                break
            else:
                players.append(p)
            b+=1
        luces = search_variable(areas[x].content,"luz","dec",True)
        for w in range(len(luces)):
            for q in range(len(areas[x].content)):
                if areas[x].content[q].title == "luz":
                    del areas[x].content[q]
                    break
        elements = []
        for y in range(len(areas[x].content)):
            el = interpretador.transform(areas[x].content[y] )
            if (el != None):
                for a in range(len(el)):
                    elements.append( el[a] )
        for z in range(len(players)):
            p = players[z].content
            for a in range(len(p)):
                p[a] = eval(p[a])
            elements.append(lo.jugador.jugador(p[0],p[1],player,p[2]))
        
        for w in range(len(luces)):
            p = luces[w].content
            for a in range(len(p)):
                p[a] = eval(p[a])
            elements.append(lo.luz.luz(*p))
            
        elm.append(elements)
    level = level_reading(name,author,description,elm)
    return level

class draw:
    def __init__(self,title):
        self.title = title
        self.TYPE = "draw"
    def add_content(self,content):
        self.content = content
    def add_params(self,params):
        for x in range(len(params)-1,-1,-1):
            if params[x] == "":
                del params[x]
        self.params = params
    def show(self):
        data = ""
        for x in range(len(self.params)):
            data += self.params[x]
            if (x != len(self.params)-1):
                data += ","
        data2 = ""
        for x in range(len(self.content)):
            data2 += self.content[x].show()
        return self.title+"("+str(data)+"){"+str(data2)+"}"

class declaration:
    def __init__(self,title):
        self.title = title
        self.TYPE = "dec"
    def add_content(self,content):
        for x in range(len(content)-1,-1,-1):
            if content[x] == "":
                del content[x]
        self.content = content
    def show(self):
        data = ""
        for x in range(len(self.content)):
            data += self.content[x]
            if (x != len(self.content)-1 and x != 0):
                data += ","
        return ""+self.title+":"+data+";"

def analisis(s,sums = 1):
    declarations = []
    x = 0
    dec_type = "notdef"
    while x < len(s):
        bs = ""
        good = False
        for y in range(len(s[x])):
            if (s[x][y] != " "):
                good = True
        for y in range(len(s[x])):
            if s[x][y] == "}":
                good = False
        y = 0
        pa = False
        st = False
        if (good == True):
            while (True):
                if (x >= len(s)):
                    break
                if (y >= len(s[x])):
                    break
                if (s[x][y] == '"'):
                    pa = not(pa)
                if s[x][y] == "{" and pa == False:
                    dec_type = "clasp"
                    if (y != len(s[x])-1):
                        raise SyntaxError,"syntax error"
                    break
                elif (s[x][y] == ":" and pa == False):
                    dec_type = "variable"
                    break
                else:
                    bs += s[x][y]
                y+= 1
            y += 1
            if (dec_type == "clasp"):
                args = [""]
                for a in range(len(bs)):
                    if (bs[a] != " "):
                        args[len(args)-1] += bs[a]
                    else:
                        args.append("")
                title = args[0]
                content = []
                for a in range(1,len(args)):
                    content.append(args[a])
                clasp = draw(title)
                clasp.add_params(content)
                x+=1
                con = []
                met = 1
                while (met != 0):
                    for y in range(len(s[x])):
                        if (s[x][y] == "{"):
                            met += 1
                        elif (s[x][y] == "}"):
                            met -= 1
                    if (met != 0):
                        con.append(s[x])
                        x+=1
                for a in range(len(con)-1,-1,-1):
                    if con[a] == "":
                        del con[a]
                clasp.add_content(analisis(con,5))
                declarations.append(clasp)
            elif (dec_type == "variable"):
                args = [""]
                par = False
                clasp = False
                while (y < len(s[x])):
                    if (s[x][y] == '"'):
                        par = not(par)
                    if ((s[x][y] != " " or par == True)):
                        args[len(args)-1] += s[x][y]
                    else:
                        args.append("")
                    y+=1
                for z in range(len(args)-1,-1,-1):
                    if (args[z] == " "):
                        del args[z]
                if (clasp == True):
                    x+=1
                    c = draw(bs)
                    c.add_params(args)
                    con = []
                    met = 1
                    while (met != 0):
                        for y in range(len(s[x])):
                            if (s[x][y] == "{"):
                                met += 1
                            elif (s[x][y] == "}"):
                                met -= 1
                        if (met != 0):
                            con.append(s[x])
                            x+=1
                    for a in range(len(con)-1,-1,-1):
                        if con[a] == "":
                            del con[a]
                    c.add_content(analisis(con,5))
                    declarations.append(c)
                else:
                    lvariable = declaration(bs)
                    lvariable.add_content(args)
                    declarations.append(lvariable)
            elif (dec_type == "variable"):
                args = [""]
                par = False
                while (y < len(s[x])):
                    if (s[x][y] == '"'):
                        par = not(par)
                    if (s[x][y] != " " or par == True):
                        args[len(args)-1] += s[x][y]
                    else:
                        args.append("")
                    y+=1
                for z in range(len(args)-1,-1,-1):
                    if (args[z] == " "):
                        del args[z]      
                variable = declaration(bs)
                variable.add_content(args)
                declarations.append(variable)
            elif (dec_type == "claspp"):
                params = ""
                while (s[x][y] != "{"):
                    params += s[x][y]
                    y+=1
                params = separate(params)
                declarations = []
                met = 1
                while (met != 0):
                    for a in range(len(s[x])):
                        if (s[x][a] == "{"):
                            met += 1
                        elif (s[x][a] == "}"):
                            met -= 1
                    if (met != 0):
                        declarations.append(s[x])
                        x += 1
                final_dec = draw(bs)
                final_dec.add_params(params)
                final_dec.add_content(declarations)
        x+=1
    return declarations

def show_data(s):
    data = ""
    for x in range(len(s)):
        data += s[x].show()
    return data

def com(file1,player):
    file2 = open(file1)
    s = re.sub('\t+','',file2.read())
    s=  s.splitlines()
    s = analisis(s)
    level = create_level(s,player)
    return level
    