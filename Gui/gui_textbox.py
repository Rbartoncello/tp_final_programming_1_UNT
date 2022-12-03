import pygame
from pygame.locals import *
from Gui.gui_widget import Widget
from constantes import *


class TextBox(Widget):
    def __init__(self, master, pos=(0, 0), size=(200, 50), color_bg=GREEN, color_border=RED1, image_bg=None, text="Button", font="Arial", font_size=14, font_color=BLUE, on_click=None, on_click_param=None):
        super().__init__(master, pos, size, color_bg, color_border, image_bg, text, font, font_size, font_color)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.writing_flag = False
        self.render()
        
    @property
    def text(self): return self._text

    def render(self):
        super().render()
        if self.state == M_STATE_HOVER:  #  Se aclara la imagen
            self.slave_surface.fill(
                M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD)
        elif self.state == M_STATE_CLICK:  #  Se oscurece la imagen
            self.slave_surface.fill(
                M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB)

    def update(self, lista_eventos):
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if (self.writing_flag):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                self.writing_flag = self.slave_rect_collide.collidepoint(
                    evento.pos)
            if evento.type == pygame.KEYDOWN and self.writing_flag:
                if evento.key == pygame.K_RETURN:
                    self.writing_flag = False
                elif evento.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                else:
                    self._text += evento.unicode

        self.render()
