import pygame
from pygame.locals import *
from Gui.gui_widget import Widget
from constantes import *


class LivesBar(Widget):
    def __init__(self, master, pos=(0, 0), size=(200, 50), color_bg=GREEN, color_border=RED1, image_bg=None, image_progress=None, value=1, value_max=5):
        super().__init__(master, pos, size, color_bg, color_border, image_bg, None, None, None, None)

        self.surface_element = pygame.image.load(image_progress)
        self.surface_element = pygame.transform.scale(
            self.surface_element, (size[0]/value_max, size[1])).convert_alpha()

        self.__value = value
        self.__value_max = value_max
        self.render()

    @property
    def value(self): return self.__value

    @value.setter
    def value(self, value): self.__value = value

    def render(self):
        super().render()
        for x in range(self.__value):
            self.slave_surface.blit(
                self.surface_element, (x*self.size[0]/self.__value_max, 0))

    def update(self, lista_eventos):

        self.render()
