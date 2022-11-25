import pygame as py
from pygame.locals import *
from constantes import *
from Gui.gui_button import Button
from Gui.gui_display_end_level import DisplayEndLevel


class Pause(DisplayEndLevel):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active, scale, is_pause):
        super().__init__(name, master_surface, pos, size, image_bg, color_bg, color_border, active, scale, header=PATH_HEADER_PAUSE)

        self.__button_settings = self.create_button(
            ((size[0] / 2) - 300, (size[1] / 2)), SIZE_BUTTONS_PAUSE, PATH_BUTTON_SETTINGS, self.__on_click_button_settings, BUTTON_SETTINGS)

        self.__button_start = self.create_button(
            ((size[0] / 2) - 135, (size[1] / 2)), SIZE_BUTTONS_PAUSE, PATH_BUTTON_PLAY, self.__on_click_button_start, BUTTON_PAUSE)

        self.__button_menu = self.create_button(
            ((size[0] / 2) + 35, (size[1] / 2)), SIZE_BUTTONS_PAUSE, PATH_BUTTON_MENU, self.__on_click_button_menu, BUTTON_MENU)
        
        self.__button_restart = self.create_button(
            ((size[0] / 2) + 200, (size[1] / 2)), SIZE_BUTTONS_PAUSE, PATH_BUTTON_RESTART, self.__on_click_button_restart, BUTTON_RESTART)
        
        self.__lista_widget = [self.__button_start, self.__button_settings, self.__button_menu, self.__button_restart]
        
        self.is_pause = is_pause
        
        self.clock = py.time.Clock()
        
        self.time_in_pause = 0
        

    def create_button(self, pos, size, path, on_click, on_click_param):
        return Button(
            master=self,
            pos=pos,
            size=size,
            color_bg=None, color_border=None,
            image_bg=path,
            on_click=on_click,
            on_click_param=on_click_param
        )

    def __on_click_button_start(self, parametro):
        if DEBUG: print(parametro, self.time_in_pause/1000)
        self.is_pause(False)
        self.time_in_pause = 0
        self.set_active(DISPLAY_PLAY)

    def __on_click_button_settings(self, parametro):
        if DEBUG: print(parametro)


    def __on_click_button_menu(self, parametro):
        if DEBUG: print(parametro)
        self.set_active(MENU_INITIAL)
        
    def __on_click_button_restart(self, parametro):
        if DEBUG: print(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.__lista_widget:
            aux_widget.update(lista_eventos)
        
        self.time_in_pause += self.clock.tick(FPS)

    def draw(self):
        super().draw()
        for aux_widget in self.__lista_widget:
            aux_widget.draw()
        
