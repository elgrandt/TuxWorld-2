
def crear_nivel(objetos,nombre,user,dir = ""):
    commands = []
    
    commands.append("level{")
    if nombre[0] == "#":
        commands.append("name: '"+nombre[1:]+"'")
    else:
        commands.append("name: '"+nombre+"'")
    commands.append("author: '"+user+"'")
    commands.append("description: 'nothing'")
    commands.append("arenas: arena1")
    commands.append("}")
    
    commands.append("arena1{")
    #commands.append("player1: 100 100 1")
    for q in range(len(objetos)):
        obj = objetos[q]
        TYPE = obj.TYPE
        if TYPE == "jugador":
            title = "player1"
            prop = [obj._x,obj._y,1]
        elif TYPE == "background":
            title = "background"
            prop = [obj._x, obj._y, obj._cx, obj._cy, obj.NAME, obj._type]
        elif TYPE == "Wall":
            esquina = False
            for w in obj.TAGS:
                if w == "Esquina":
                    esquina = True
            if not esquina:
                title = "wall"
                prop = [obj._x, obj._y, obj._lonx, obj._lony, obj._rotated, obj.ubic, obj.NAME]
            else:
                title = "esquina"
                prop = [obj._x, obj._y, obj._dir, obj.NAME]
        elif TYPE == "Enemy":
            title = "enemy"
            prop = [obj._x, obj._y, obj.NAME, obj._TYPE, True, obj.direccion, obj.limites[0], obj.limites[1], obj.limites[2], obj.limites[3]]
        elif TYPE == "Button":
            title = "button"
            prop = [obj._x, obj._y, obj.object, obj.NAME, obj.default]
        elif TYPE == "Puerta":
            title = "puerta"
            prop = [obj._x, obj._y, obj.direccion, obj.NAME, obj.long]
        elif TYPE == "Teletransportador_in":
            title = "teletransportador"
            prop = [obj.pos_in[0], obj.pos_in[1], obj.pos_out[0], obj.pos_out[1], obj.NAME[:len(obj.NAME) - 3]]
        elif TYPE == "Luz":
            title = "luz"
            prop = [obj._x,obj._y,obj.size[0],obj.size[1],obj.luminocidad_original, obj.NAME]
        elif TYPE == "Laser":
            title = "laser"
            prop = [obj._x,obj._y,obj.dir,obj.vel,obj.NAME]
        elif TYPE == "Meta":
            title = "meta"
            prop = [obj._x,obj._y,obj.long,obj.original_vertical,obj.NAME]
        elif TYPE == "Moneda" or TYPE == "vida_extra" or TYPE == "Box" or TYPE == "Dinamite" or TYPE == "Checkpoint":
            if TYPE == "Moneda":
                title = "coin"
            elif TYPE == "vida_extra":
                title = "extra_life"
            elif TYPE == "Box":
                title = "box"
            elif TYPE == "Dinamite":
                title = "bomb"
            elif TYPE == "Checkpoint":
                title = "checkpoint"
            prop = [obj._x, obj._y, obj.NAME]
        else:
            prop = "NO"

        if prop != "NO":
            command = title + ": "
            for w in range(len(prop)):
                if type(prop[w]) == str:
                    prop[w] = '"'+prop[w]+'"'
                if w != len(prop) - 1:
                    command += str(prop[w]) + " "
                else:
                    command += str(prop[w])
            commands.append(command)
    commands.append("}")
    
    if len(nombre) > 1 and nombre[0] == "#":
        file = open(dir,"w")
    else:
        file = open("data/levels/"+nombre+".lvl","w")
    for q in commands:
        if q.find("{") != -1 or q.find("}") != -1:
            file.write(q+"\n")
        else:
            file.write("\t"+q+"\n")
    file.close()