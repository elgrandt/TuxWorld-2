import com
import tran

def load_com_level(file,name,area = 0):
    import game
    data = com.com(file, name)
    phi = game.phi.phi()
    phi.my_player = name
    phi.level_name = data.name
    phi.level_author = data.author
    phi.level_description = data.description
    for x in range(len(data.areas[area])):
        phi.objetos.append(data.areas[area][x])
    mgame = game.game()
    mgame.phi = phi
    return mgame
def load_com_multiplayer(file,name,area = 0):
    import game
    data = com.com(file, name)
    phi = game.phi.phi()
    phi.my_player = name
    phi.level_name = data.name
    phi.level_author = data.author
    phi.level_description = data.description
    for x in range(len(data.areas[area])):
        if (data.areas[area][x].TYPE == "jugador"):
            data.areas[area][x].ID = 1
        phi.objetos.append(data.areas[area][x])
    mgame = game.game()
    mgame.phi = phi
    return mgame
    