import SocketServer
from game import com
import pygame

class MiTcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        pass 
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass


class test_a:
    def __init__(self,file_level):
        self.game = com.load_com_multiplayer(file_level,"player")
        
        
    def graphic_update(self,SCREEN):
        self.game.graphic_update(SCREEN)
    def logic_update(self,EVENTS):
        
        EVENTS.set_player_movement(EVENTS.get_keyboard()[pygame.K_UP],EVENTS.get_keyboard()[pygame.K_DOWN],EVENTS.get_keyboard()[pygame.K_LEFT],EVENTS.get_keyboard()[pygame.K_RIGHT],EVENTS.get_keyboard()[pygame.K_SPACE],1)
        
        return self.game.logic_update(EVENTS)
    