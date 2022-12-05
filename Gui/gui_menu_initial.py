import pygame as py
from pygame.locals import *
import sys
from constantes import *
from Gui.gui_form import Form
from Gui.gui_button import Button


class MenuInitial(Form):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active):
        super().__init__(name, master_surface, pos, size, image_bg, color_bg, color_border, active)
        py.mixer.music.load('sound/bg.mp3')
        py.mixer.music.play(loops=-1)

        self.__button_settings = self.create_button(
            ((size[0] / 2) - 300, (size[1] / 2)), SIZE_BUTTON_MENU_INITIAL, PATH_BUTTON_SETTINGS,
            self.__on_click_button_settings, BUTTON_SETTINGS)

        self.__button_start = self.create_button(
            ((size[0] / 2) - 75, (size[1] / 2)), SIZE_BUTTON_MENU_INITIAL, PATH_BUTTON_PLAY,
            self.__on_click_button_start, MENU_LEVELS)

        self.__button_exit = self.create_button(
            ((size[0] / 2) + 150, (size[1] / 2)), SIZE_BUTTON_MENU_INITIAL, PATH_BUTTON_CLOSE,
            self.__on_click_button_exit, BUTTON_EXIT)

        self.__button_ranking = self.create_button(
            (size[0] - 150, 50), (100, 100), PATH_BUTTON_RANKING, self.__on_click_button_ranking, BUTTON_RANKNG)


        self.__lista_widget = [self.__button_start, self.__button_settings, self.__button_exit, self.__button_ranking]

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
        if DEBUG: print(parametro)
        self.set_active(parametro)

    def __on_click_button_settings(self, parametro):
        if DEBUG: print(parametro)
        self.set_active(MENU_SETTINGS)

    def __on_click_button_ranking(self, parametro):
        if DEBUG: print(parametro)
        self.set_active(MENU_RANKING)

    def __on_click_button_exit(self, parametro):
        if DEBUG: print(parametro)
        self.set_active(FORM_INPUT_NAME)

    def update(self, lista_event):
        for aux_widget in self.__lista_widget:
            aux_widget.update(lista_event)

    def draw(self):
        super().draw()
        for aux_widget in self.__lista_widget:
            aux_widget.draw()
