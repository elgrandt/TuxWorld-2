import pygame
import element
import utils.pfunctions as pf
import extra_data.images as img
import utils.checkpoint as check

class checkpoint(element.element):
    def __init__(self, x, y, NAME):
        self.surf = img.checkpoint_sin_act
        self.checked = False
        self.lchecked = False
        self.element(x, y, NAME, "Checkpoint", [], self.surf)
    def plu(self,events,up):
        if self.checked:
            self.surface = img.checkpoint_act
            if not self.lchecked:
                self.lchecked = True
                check.grabar(up.level_name, self.NAME, up.my_player)