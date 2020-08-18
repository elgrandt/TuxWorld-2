from menu import menu
import game.game_over.game_over as game_over
import sys
import game.com as gm
import new_level
import extra_data.images as img
from utils.help import help
import utils.alert as al

class stage:
    def __init__(self):
        self.current_area = menu("test version")
        self.menu = True
        self.pos_boton_menu = (5,5)
    def graphic_update(self,SCREEN):
        self.current_area.graphic_update(SCREEN)
        try:
            self.current_area.es_menu
            menu = True
        except:
            menu = False
        if not menu:
            SCREEN.blit(img.menu,self.pos_boton_menu)
        self.menu = menu
    def logic_update(self,EVENTS):
        command = self.current_area.logic_update(EVENTS)
        if not self.menu:
            x,y = EVENTS.get_mouse().get_position()
            if EVENTS.get_mouse().get_pressed()[0]:
                if x > self.pos_boton_menu[0] and x < self.pos_boton_menu[0] + img.menu.get_size()[0] and y > self.pos_boton_menu[1] and y < self.pos_boton_menu[1] + img.menu.get_size()[1]:
                    self.current_area = menu("test version")
        return self.evaluate_command(command)
    def evaluate_command(self,command):
        if command != None:
            if command == "highscores":
                #highscores
                pass  
            elif command.find("new level") != -1:
                self.current_area = new_level.new_level()
                profile_name = command[:command.find("new level")]
                self.current_area.objetos.profile_name = profile_name
            elif command == "game over":
                self.current_area = game_over.looser("GAME OVER")
            elif command == "exit":
                return "salir"
            elif command.find("load") != -1:
                self.current_area = gm.load_com_level(command[command.find("load")+4:],command[:command.find("load")])
            elif command == "restart game":
                import main
                return "salir"
            elif command == "hacker":
                self.current_area = game_over.looser("ILEGAL")
            elif command.find("edit_level") != -1:
                file_sel = command[command.find("edit_level")+len("edit_level"):]
                profile_name = command[:command.find("edit_level")]
                self.current_area = new_level.new_level()
                import game.com.com as com
                data = com.com(file_sel, "Jugador")
                for x in range(len(data.areas[0])):
                    if data.areas[0][x].TYPE != "jugador":
                        if data.areas[0][x].TYPE == "Enemy":
                            data.areas[0][x].mobile = False
                        self.current_area.objetos.phi.objetos.append(data.areas[0][x])
                del self.current_area.objetos.phi.objetos[self.current_area.objetos.indice_jugador]
                self.current_area.objetos.phi.objetos.append(new_level.lo.jugador.jugador(100,100,"Test",False))
                self.current_area.objetos.indice_jugador = len(self.current_area.objetos.phi.objetos)
                self.current_area.objetos.default_save = "#"+data.name
                self.current_area.objetos.dir = file_sel
                self.current_area.objetos.profile_name = profile_name
            elif command.find("test A") != -1:
                import multiplayer
                self.current_area = multiplayer.test_a(command[command.find("test A ")+7:])
            elif command == "test B":
                import multiplayer
                