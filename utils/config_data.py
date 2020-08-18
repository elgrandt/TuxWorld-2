
def obtener_data(perfil):
    try:
        arch = "data/perfiles/"+perfil+"/data.conf"
        arch = open(arch)
        arch = arch.read()
        lineas = []
        linea_act = ""
        for q in arch:
            if q != "\n":
                linea_act += q
            else:
                lineas.append(linea_act)
                linea_act = ""
        if linea_act != "":
            lineas.append(linea_act)
        obj = []
        for q in lineas:
            act = ""
            primera_parte = ""
            segunda_parte = ""
            for w in q:
                if w != ":":
                    act += w
                else:
                    primera_parte = act
                    act = ""
            segunda_parte = act
            if segunda_parte[0] == " ":
                segunda_parte = segunda_parte[1:]
            segunda_parte = int(segunda_parte)
            obj.append([primera_parte,segunda_parte])
        if len(obj) == 0:
            obj = [["Tutorial",0]]
        return obj
    except:
        return []

def grabar_data(data,perfil):
    arch = "data/perfiles/"+perfil+"/data.conf"
    arch = open(arch,"w")
    for q in data:
        arch.write(q[0]+": "+str(q[1])+"\n")