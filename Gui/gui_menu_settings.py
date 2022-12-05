import pygame as py
from constantes import *
from Gui.gui_form import Form
from Gui.gui_button import Button


class MenuSettings(Form):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active):
        super().__init__(name, master_surface, pos, size,
                         image_bg, color_bg, color_border, active)

        self.__button_exit = None
        self.create_exit_button(size[0])

        self.__button_music_on = self.create_button(
            ((size[0] / 2) - 150, (size[1] / 2)), SIZE_BUTTONS_SETTINGS, PATH_BUTTON_MUSIC_ON, self.__on_click_music_on, BUTTON_MUSIC_ON)

        self.__button_music_off = self.create_button(
            ((size[0] / 2) - 150, (size[1] / 2)), SIZE_BUTTONS_SETTINGS, PATH_BUTTON_MUSIC_OFF, self.__on_click_music_off, BUTTON_MUSIC_OFF)

        self.__button_sound_on = self.create_button(
            ((size[0] / 2) + 25, (size[1] / 2)), SIZE_BUTTONS_SETTINGS, PATH_BUTTON_SOUND_ON, self.__on_click_sound_on, BUTTON_SOUND_ON)

        self.__button_sound_off = self.create_button(
            ((size[0] / 2) + 25, (size[1] / 2)), SIZE_BUTTONS_SETTINGS, PATH_BUTTON_SOUND_OFF, self.__on_click_sound_off, BUTTON_SOUND_OFF)

        self.__lista_widget = [
            self.__button_music_on,
            self.__button_sound_on,
            self.__button_exit
        ]

        self.__image_header = py.image.load(PATH_HEADER_SETTINGS)
        self.__image_header = py.transform.rotozoom(
            self.__image_header, 0, 0.6).convert_alpha()
        self.__rect_image_header = self.__image_header.get_rect(
            midtop=(W_MENU/2, 0))
        
        self.__sounds = []
        
    
    @property
    def sounds(self):
        return self.__sounds
    
    @sounds.setter
    def sounds(self, sounds):
        self.__sounds = sounds

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

    def change_state_button(self, button_true, button_false):
        self.__lista_widget.remove(button_true)
        self.__lista_widget.append(button_false)

    def create_exit_button(self, w):
        self.__button_exit = Button(
            master=self,
            pos=((w/2)+250, 45),
            size=SIZE_BUTTON_EXIT,
            color_bg=None, color_border=None,
            image_bg=PATH_BUTTON_CLOSE,
            on_click=self.__on_click_exit,
            on_click_param=BUTTON_EXIT
        )

    def __on_click_exit(self, parametro):
        if DEBUG:
            print(parametro)
        self.set_active(MENU_INITIAL)

    def __on_click_music_on(self, parametro):
        if DEBUG:
            print(parametro)
        self.change_state_button(
            self.__button_music_on, self.__button_music_off)
        self.draw()
        py.mixer.music.set_volume(0)

    def __on_click_music_off(self, parametro):
        if DEBUG:
            print(parametro)
        self.change_state_button(
            self.__button_music_off, self.__button_music_on)
        self.draw()

        py.mixer.music.set_volume(1.0)

    def __on_click_sound_on(self, parametro):
        if DEBUG:
            print(parametro)
        self.change_state_button(
            self.__button_sound_on, self.__button_sound_off)
        
        for sound in self.__sounds:
            sound.set_volume(0.0)

    def __on_click_sound_off(self, parametro):
        if DEBUG:
            print(parametro)
        self.change_state_button(
            self.__button_sound_off, self.__button_sound_on)
        
        for sound in self.__sounds:
            sound.set_volume(0.5)

    def update(self, lista_eventos):
        for aux_widget in self.__lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.surface.blit(self.__image_header, self.__rect_image_header)
        for aux_widget in self.__lista_widget:
            aux_widget.draw()
