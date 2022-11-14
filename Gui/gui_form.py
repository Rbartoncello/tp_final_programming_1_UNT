import pygame
from pygame.locals import *


class Form():
    forms_dict = {}

    def __init__(self, name, master_surface, pos, side, color_bg, color_border, active):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = pos[0]
        self.y = pos[1]
        self.w = side[0]
        self.h = side[1]
        self.color_background = color_bg
        self.color_border = color_border

        self.surface = pygame.Surface(side)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = pos[0]
        self.slave_rect.y = pos[1]
        self.active = active
        self.x = pos[0]
        self.y = pos[1]

        if (self.color_background != None):
            self.surface.fill(self.color_background)

    def set_active(self, name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def render(self):
        pass

    def update(self, lista_eventos):
        pass

    def draw(self):
        self.master_surface.blit(self.surface, self.slave_rect)
