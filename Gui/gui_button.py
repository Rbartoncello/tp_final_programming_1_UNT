import pygame as py
from pygame.locals import *
from Gui.gui_widget import Widget
from constantes import *


class Button(Widget):
    def __init__(self, master, pos=(0, 0), size=(200, 50), color_bg=GREEN, color_border=RED1, image_bg=None, text=None, font=None, font_size=None, font_color=None, on_click=None, on_click_param=None):
        super().__init__(master, pos, size, color_bg, color_border,
                         image_bg, text, font, font_size, font_color)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL

    def render(self):
        super().render()
        if self.state == M_STATE_HOVER:  #  Se aclara la imagen
            self.slave_surface.fill(
                M_BRIGHT_HOVER, special_flags=py.BLEND_RGB_ADD)
        elif self.state == M_STATE_CLICK:  #  Se oscurece la imagen
            self.slave_surface.fill(
                M_BRIGHT_CLICK, special_flags=py.BLEND_RGB_SUB)

    def update(self, lista_eventos):
        mousePos = py.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if py.mouse.get_pressed()[0]:
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == py.MOUSEBUTTONDOWN:
                if self.slave_rect_collide.collidepoint(evento.pos):
                    self.on_click(self.on_click_param)

        self.render()
