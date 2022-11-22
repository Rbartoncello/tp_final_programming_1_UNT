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
        self.create_exit_button(size[0])

        self.__buttons_levels = []
        self.create_levels_buttons()

        self.__image_bg = py.image.load(PATH_BG_SELECT_LEVELS)
        self.__image_bg = py.transform.scale(
            self.__image_bg, (W_MENU-150, H_MENU-150)).convert_alpha()
        self.__rect_image_bg = self.surface.get_rect(topleft=(75, 75))

        self.__image_header = py.image.load(PATH_HEADER_SELECT_LEVELS)
        self.__image_header = py.transform.rotozoom(
            self.__image_header, 0, 0.6).convert_alpha()
        self.__rect_image_header = self.__image_header.get_rect(
            midtop=(W_MENU/2, -15))
        
        self.__last_level_unlock = 1
        
        self.play = Play(
            name=DISPLAY_PLAY,
            master_surface=master_surface,
            pos=(0, 0),
            size=(W_WINDOWN, H_WINDOWN),
            color_bg=None, color_border=None,
            last_level = self.__last_level_unlock,
            active=False)
    
    @property    
    def last_level_unlock(self): return self.__last_level_unlock
    
    @last_level_unlock.setter
    def last_level_unlock(self, level): self.__last_level_unlock = level

    def create_levels_buttons(self):
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
                self.unlock_button_level(level)

    def create_exit_button(self, w):
        self.__button_exit = Button(
            master=self,
            pos=((w/2)+250, 90),
            size=SIZE_BUTTON_EXIT,
            color_bg=None, color_border=None,
            image_bg=PATH_BUTTON_CLOSE,
            on_click=self.__on_click_button_exit,
            on_click_param=MENU_INITIAL
        )

    def unlock_button_level(self, level):
        if level == 1:
            self.__buttons_levels[level-1].unlock = True
        # self.unlock_buttons()
        
    def update_buttons(self, stars):
        self.__buttons_levels[self.__last_level_unlock-2].set_star(stars)
        self.__buttons_levels[self.__last_level_unlock-1].unlock = True

    def unlock_buttons(self):
        for button in self.__buttons_levels:
            button.unlock = True

    def __on_click_button_level(self, parametro):
        if DEBUG:
            print(parametro)
        self.set_active(DISPLAY_PLAY)

    def __on_click_button_exit(self, parametro):
        if DEBUG:
            print(parametro)
        self.set_active(parametro)

    def update(self, lista_eventos):
        self.__button_exit.update(lista_eventos)
        if self.play.level.win():
            self.__last_level_unlock+=1
        self.update_buttons(3)
        for button in self.__buttons_levels:
            button.update(lista_eventos)

    def draw(self):
        super().draw()
        self.surface.blit(self.__image_bg, self.__rect_image_bg)
        for button in self.__buttons_levels:
            button.draw()
        self.surface.blit(self.__image_header, self.__rect_image_header)
        self.__button_exit.draw()
