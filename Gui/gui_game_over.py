import pygame as py
from pygame.locals import *
import sys
from constantes import *
from Gui.gui_form import Form


class GameOver(Form):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active):
        super().__init__(name, master_surface, pos, size, image_bg, color_bg, color_border, active)

    def update(self, lista_eventos):
        pass

    def draw(self):
        super().draw()
