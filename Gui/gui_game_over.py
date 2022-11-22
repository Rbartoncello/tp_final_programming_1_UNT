import pygame as py
from pygame.locals import *
import sys
from constantes import *
from Gui.gui_form import Form


class GameOver(Form):
    def __init__(self, name, master_surface, image_bg, color_bg, color_border, active):        
        self.image = py.image.load(image_bg)
        self.image = py.transform.rotozoom(self.image, 0, 0.9).convert_alpha()
        x_lock=abs(W_WINDOWN-self.image.get_size()[0])/2
        y_lock=abs(H_WINDOWN-self.image.get_size()[1])/2
        super().__init__(name, master_surface, (x_lock, y_lock), self.image.get_size(), image_bg, color_bg, color_border, active)
        self.time_delay = 10000
        self.time_accumulation_delay = 0
        self.clock = py.time.Clock()
        

    def update(self, lista_eventos):
        self.time_accumulation_delay += self.clock.tick(FPS)
        if self.time_accumulation_delay >= self.time_delay:
            self.set_active(MENU_INITIAL)

    def draw(self):
        super().draw()
