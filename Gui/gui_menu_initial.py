import pygame as py
from pygame.locals import *
import sys
from constantes import *
from Gui.gui_form import Form
from Gui.gui_button import Button
from Gui.gui_textbox import TextBox


class MenuInitial(Form):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active):
        super().__init__(name, master_surface, pos, size, image_bg, color_bg, color_border, active)

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

        """ self.txt1 = TextBox(
            master=self,
            pos=(200, 50),
            size=(240, 50),
            color_bg=None,
            color_border=None,
            image_bg="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",
            text="Text",
            font="Verdana",
            font_size=30,
            font_color=BLACK
        ) """

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

    def __on_click_button_ranking(self, parametro):
        if DEBUG: print(parametro)

    def __on_click_button_exit(self, parametro):
        if DEBUG: print(parametro)
        py.quit()
        sys.exit()

    def update(self, lista_event):
        for aux_widget in self.__lista_widget:
            aux_widget.update(lista_event)

    def draw(self):
        super().draw()
        for aux_widget in self.__lista_widget:
            aux_widget.draw()
