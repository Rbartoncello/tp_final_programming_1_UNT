import pygame as py
from pygame.locals import *
from constantes import *
from Gui.gui_form import Form


class DisplayEndLevel(Form):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active, scale, stars,header):
        super().__init__(name, master_surface, pos, size,
                         image_bg, color_bg, color_border, active)

        self.time_delay = 10000
        self.time_accumulation_delay = 0
        self.clock = py.time.Clock()

        self.__image_bg = py.image.load(PATH_BG_SELECT_LEVELS)
        self.__image_bg = py.transform.scale(
            self.__image_bg, (W_MENU-150, H_MENU-150)).convert_alpha()
        self.__rect_image_bg = self.surface.get_rect(topleft=(75, 75))

        self.__image_header = py.image.load(header)
        self.__image_header = py.transform.rotozoom(
            self.__image_header, 0, scale).convert_alpha()
        self.__rect_image_header = self.__image_header.get_rect(
            midtop=(W_MENU/2, 60))
        
        self.__image_stars = py.image.load(PATH_BUTTON_LEVELS_STAR[str(stars)])
        self.__image_stars = py.transform.rotozoom(self.__image_stars, 0, 1.5).convert_alpha()
        self.__rect_image_stars = self.__image_stars.get_rect(center=(W_MENU/2, H_MENU/2+50))

    def update(self, lista_eventos):
        self.time_accumulation_delay += self.clock.tick(FPS)
        if self.time_accumulation_delay >= self.time_delay:
            self.time_accumulation_delay = 0
            self.set_active(MENU_LEVELS)

    def draw(self):
        super().draw()
        self.surface.blit(self.__image_bg, self.__rect_image_bg)
        self.surface.blit(self.__image_header, self.__rect_image_header)
        self.surface.blit(self.__image_stars, self.__rect_image_stars)
    def set_stars(self, stars): 
        self.__image_stars = py.image.load(PATH_BUTTON_LEVELS_STAR[str(stars)]) 
        self.__image_stars = py.transform.rotozoom(self.__image_stars, 0, 1.5).convert_alpha()
        self.__rect_image_stars = self.__image_stars.get_rect(center=(W_MENU/2, H_MENU/2+50))