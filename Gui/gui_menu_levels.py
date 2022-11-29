import pygame as py
from pygame.locals import *
from constantes import *
from Gui.gui_form import Form
from Gui.gui_button import Button
from Gui.gui_button_level import ButtonLevel
from Gui.gui_play import Play


class MenuLevels(Form):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active):
        super().__init__(name, master_surface, pos, size,
                         image_bg, color_bg, color_border, active)

        self.__button_exit = None
        self.__create_exit_button(size[0])

        self.__buttons_levels = []
        self.__create_levels_buttons()

        self.__image_bg = py.image.load(PATH_BG_SELECT_LEVELS)
        self.__image_bg = py.transform.scale(
            self.__image_bg, (W_MENU - 150, H_MENU - 150)).convert_alpha()
        self.__rect_image_bg = self.surface.get_rect(topleft=(75, 75))

        self.__image_header = py.image.load(PATH_HEADER_SELECT_LEVELS)
        self.__image_header = py.transform.rotozoom(
            self.__image_header, 0, 0.6).convert_alpha()
        self.__rect_image_header = self.__image_header.get_rect(
            midtop=(W_MENU / 2, -15))

        self.__last_level_unlock = 1
        self.__level_selected = 1
        self.__stars_last_level_unlock = 0

    @property
    def last_level_unlock(self):
        return self.__last_level_unlock

    @property
    def level_selected(self):
        return self.__level_selected

    @last_level_unlock.setter
    def last_level_unlock(self, level):
        self.__last_level_unlock = level

    @property
    def stars_last_level_unlock(self):
        return self.__stars_last_level_unlock

    @stars_last_level_unlock.setter
    def stars_last_level_unlock(self, level):
        self.__stars_last_level_unlock = level

    def __create_levels_buttons(self):
        level = 0
        for row in range(MAX_LEVELS_ROW):
            for col in range(MAX_LEVELS_COL):
                level += 1
                self.__buttons_levels.append(ButtonLevel(
                    master=self,
                    pos=(125 + col * 200, 175 + row * 170),
                    size=SIZE_BUTTON_LEVEL,
                    color_bg=None, color_border=None,
                    image_bg=PATH_BUTTON_IMAGE_BG,
                    on_click=self.__on_click_button_level,
                    on_click_param=level,
                    text=None, font=None, font_size=None, font_color=None,
                    level=level
                ))

    def __create_exit_button(self, w):
        self.__button_exit = Button(
            master=self,
            pos=((w / 2) + 250, 90),
            size=SIZE_BUTTON_EXIT,
            color_bg=None, color_border=None,
            image_bg=PATH_BUTTON_CLOSE,
            on_click=self.__on_click_button_exit,
            on_click_param=MENU_INITIAL
        )

    def __unlock_button_level(self, level):
        self.__buttons_levels[level - 1].unlock = True

    def __update_buttons(self):
        self.__buttons_levels[self.__last_level_unlock - 2].set_star(self.__stars_last_level_unlock)
        self.__buttons_levels[self.__last_level_unlock - 1].unlock = True

    def __unlock_buttons(self):
        for button in self.__buttons_levels:
            button.unlock = True

    def __on_click_button_level(self, parametro):
        if DEBUG: print(parametro)
        self.__level_selected = parametro
        self.set_active(DISPLAY_PLAY)

    def __on_click_button_exit(self, parametro):
        if DEBUG: print(parametro)
        self.set_active(parametro)

    def update(self, lista_event):
        self.__button_exit.update(lista_event)
        self.__update_buttons()
        for button in self.__buttons_levels:
            button.update(lista_event)

    def draw(self):
        super().draw()
        self.surface.blit(self.__image_bg, self.__rect_image_bg)
        for button in self.__buttons_levels:
            button.draw()
        self.surface.blit(self.__image_header, self.__rect_image_header)
        self.__button_exit.draw()
