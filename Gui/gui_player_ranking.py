import pygame as py
from pygame.locals import *
from Gui.gui_widget import Widget
from constantes import *
from Gui.gui_text import Text


class PlayerRanking(Widget):
    def __init__(self, master, pos, size, color_bg, color_border, text):
        super().__init__(master, pos, size, color_bg, color_border, image_bg=None,
                         text=text, font="Verdana", font_size=30, font_color=BLACK)

        self.__image_player = py.image.load(PATH_PICTURE_PLAYER)
        self.__image_player = py.transform.rotozoom(
            self.__image_player, 0, 0.5).convert_alpha()
        x = (size[0]-self.__image_player.get_size()[0])/2
        y = (size[1]-self.__image_player.get_size()[1])/2
        self.__pos_image = (x, y)

        self.txt1 = Text(
            master=self.master_form,
            pos=(self.pos.x + x + self.__image_player.get_size()
                 [0], self.pos.y + (self.__image_player.get_size()[1])/2),
            size=(300, 50),
            color_bg=None,
            color_border=None,
            image_bg=None,
            text=text,
            font="Verdana",
            font_size=30,
            font_color=BLACK
        )

        self.txt2 = Text(
            master=self.master_form,
            pos=(self.pos.x + x + self.__image_player.get_size()
                 [0] + 300, self.pos.y + (self.__image_player.get_size()[1])/2),
            size=(100, 50),
            color_bg=None,
            color_border=None,
            image_bg=None,
            text=text,
            font="Verdana",
            font_size=30,
            font_color=BLACK
        )

    @property
    def value(self): return self.txt1.value

    @value.setter
    def value(self, value):
        self.txt1.value = value[1]
        self.txt2.value = value[2]

    def render(self):
        super().render()
        self.slave_surface.blit(self.__image_player, self.__pos_image)

    def update(self, lista_eventos):
        self.render()
        self.txt1.update(lista_eventos)
        self.txt2.update(lista_eventos)

    def draw(self):
        super().draw()
        self.txt1.draw()
        self.txt2.draw()
