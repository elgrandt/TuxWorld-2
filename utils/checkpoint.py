import os
ruta = "data/progress/"

def grabar(level,check_name,usuario):
    if not os.path.isdir(ruta + usuario):
        os.mkdir(ruta + usuario)
    file = open(ruta + usuario + "/" + level + ".chk","w")
    file.write(check_name)

def consultar(level,objetos,usuario):
    try:
        file = open(ruta + usuario + "/" + level + ".chk")
        info = file.read()
        for q in objetos:
            if q.TYPE == "Checkpoint":
                if q.NAME == info:
                    return (q._x, q._y)
        return "Error"
    except:
        return "Error"