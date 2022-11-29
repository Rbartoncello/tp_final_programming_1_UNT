import pygame as py
from pygame.locals import *
from constantes import *


class Form:
    forms_dict = {}

    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active=False):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.pos = py.math.Vector2(pos)
        self.size = size
        if image_bg is not None:
            self.surface = py.image.load(image_bg)
            self.surface = py.transform.scale(
                self.surface, size).convert_alpha()
        else:
            self.surface = py.Surface(size)
            self.color_bg = color_bg
            self.color_border = color_border
            if self.color_bg is not None:
                self.surface.fill(self.color_bg)

        self.slave_rect = self.surface.get_rect(topleft=pos)
        self.active = active

    def set_active(self, name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def render(self):
        pass

    def update(self, lista_event):
        pass

    def draw(self):
        self.master_surface.blit(self.surface, self.slave_rect)
