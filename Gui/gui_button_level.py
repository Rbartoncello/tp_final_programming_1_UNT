import pygame as py
from pygame.locals import *
from Gui.gui_button import Button
from constantes import *


class ButtonLevel(Button):
    def __init__(self, master, pos, size, color_bg, color_border, image_bg, text, font, font_size, font_color, on_click, on_click_param, level):
        super().__init__(master, pos, size, color_bg, color_border, image_bg,
                         text, font, font_size, font_color, on_click, on_click_param)

        self.__image_lock = py.image.load(PATH_BUTTON_LEVELS_UNLOCK)        
        self.__image_lock = py.transform.rotozoom(self.__image_lock, 0, 0.5).convert_alpha()
        x_lock=(size[0]-self.__image_lock.get_size()[0])/2
        y_lock=(size[1]-self.__image_lock.get_size()[1])/2
        self.__pos_image_lock = (x_lock, y_lock)

        self.__level = level
        self.__image_number = py.image.load(PATH_BUTTON_LEVELS_NUMBER[str(self.__level)])
        x_number=(size[0]-self.__image_number.get_size()[0])/2
        y_number=(size[1]-self.__image_number.get_size()[1])/2
        self.__pos_image_number = (x_number, y_number)
        
        self.__image_stars = py.image.load(PATH_BUTTON_LEVELS_STAR['0'])
        self.__image_stars = py.transform.rotozoom(self.__image_stars, 0, 0.44).convert_alpha()
        x_stars=(size[0]-self.__image_stars.get_size()[0])/2
        y_stars=(size[1]-self.__image_stars.get_size()[1])
        self.__pos_image_stars = (x_stars, y_stars)

        self.__unlock = False

    @property
    def unlock(self): return self.__unlock

    @unlock.setter
    def unlock(self, state): self.__unlock = state
    
    def set_star(self, star): 
        size = self.__image_stars.get_size()        
        self.__image_stars = py.image.load(PATH_BUTTON_LEVELS_STAR[str(star)])
        self.__image_stars = py.transform.scale(self.__image_stars, size).convert_alpha()

    def render(self):
        super().render()
        if self.__unlock:
            self.__image_algo = py.transform.scale(py.image.load(PATH_BUTTON_IMAGE_BG), self.image_bg.get_size()).convert_alpha()
            self.image_bg.blit(self.__image_algo, self.image_bg.get_rect())
            self.image_bg.blit(self.__image_number, self.__pos_image_number)
            self.image_bg.blit(self.__image_stars, self.__pos_image_stars)
        else:
            self.image_bg.blit(self.__image_lock, self.__pos_image_lock)

    def update(self, lista_event):
        mousePos = py.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if py.mouse.get_pressed()[0]:
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_event:
            if evento.type == py.MOUSEBUTTONDOWN:
                if self.slave_rect_collide.collidepoint(evento.pos) and self.__unlock:
                    self.on_click(self.on_click_param)

        self.render()
