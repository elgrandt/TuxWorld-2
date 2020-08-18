import game.com.com as com,re

def interpretar(file):
    arch = open(file)
    
    s = re.sub('\t+','',arch.read())
    s=  s.splitlines()
    s = com.analisis(s)
    ids = []
    props = []
    for q in range(len(s)):
        ID = s[q].title
        ids.append(ID)
        propiedades = []
        for w in s[q].content:
            propiedades.append([w.title,w.content])
        props.append(propiedades)
    return [ids,props]

archive = "data/styles/test"
estilos = interpretar(archive)
ids = estilos[0]
props = estilos[1]

def obtener_propiedades(ID):
    for q in range(len(ids)):
        if ids[q] == ID:
            return props[q]
    return False

def op(ID,propiedad,default = False):
    propiedades = obtener_propiedades(ID)
    if propiedades != False:
        for q in range(len(propiedades)):
            if propiedades[q][0] == propiedad:
                for w in range(len(propiedades[q][1])):
                    if type(propiedades[q][1][w]) == str:
                        if propiedades[q][1][w].isdigit():
                            propiedades[q][1][w] = int(propiedades[q][1][w])
                if len(propiedades[q][1]) > 1:
                    return propiedades[q][1]
                else:
                    return propiedades[q][1][0]
    return default