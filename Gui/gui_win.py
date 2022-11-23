import pygame as py
from pygame.locals import *
from constantes import *
from Gui.gui_display_end_level import DisplayEndLevel


class Win(DisplayEndLevel):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active, scale, stars, header):
        super().__init__(name, master_surface, pos, size, image_bg, color_bg, color_border, active, scale, )

        self.__image_stars = py.image.load(PATH_BUTTON_LEVELS_STAR[str(stars)])
        self.__image_stars = py.transform.rotozoom(self.__image_stars, 0, 1.5).convert_alpha()
        self.__rect_image_stars = self.__image_stars.get_rect(center=(W_MENU/2, H_MENU/2+50))

    def draw(self):
        super().draw()
        self.surface.blit(self.__image_stars, self.__rect_image_stars)
    
    def set_stars(self, stars): 
        self.__image_stars = py.image.load(PATH_BUTTON_LEVELS_STAR[str(stars)]) 
        self.__image_stars = py.transform.rotozoom(self.__image_stars, 0, 1.5).convert_alpha()
        self.__rect_image_stars = self.__image_stars.get_rect(center=(W_MENU/2, H_MENU/2+50))