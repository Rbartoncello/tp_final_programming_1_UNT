import pygame as py
from pygame.locals import *
from constantes import *
from Gui.gui_form import Form
from Gui.gui_displaybox import DisplayBox
from Gui.gui_lives_bar import LivesBar
from Gui.gui_button import Button


class FormInGame(Form):
    def __init__(self, name, master_surface, pos, size, color_bg, color_border, value, active):
        super().__init__(name, master_surface, pos, size, color_bg, color_border, active)

        self.pause_button = self.create_button(
            (0, 0), (size[1], size[1]), PATH_BUTTON_PAUSE, self.__on_click, BUTTON_PAUSE)

        self.score_display = DisplayBox(master=self, pos=(0, 0), size=(
            W_SCORE_TIMER * 10, size[1]), color_bg=None, color_border=None, image_bg=PATH_BG_SCORE_DISPLAY,
                                        text="Time: 0   Score: 0", font="IMPACT", font_size=40, font_color=BLACK)

        self.lives_bar = LivesBar(master=self, pos=(W_WINDOWN - 120, 0), size=(
            120, 35), color_bg=None, color_border=None, image_bg=PATH_BG_LIVES_BAR,
                                  image_progress="images/gui/set_gui_01/Standard/Elements/heart.png", value=value.live, value_max=value.live)

        self.lista_widget = [self.score_display, self.lives_bar, self.pause_button]

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

    def __on_click(self, parametro):
        if DEBUG: print(parametro, self.timer)
        self.is_pause(True)
        self.set_active(DISPLAY_PAUSE)

    def update(self, lista_event, player, timer, is_pause):
        self.timer = timer
        self.lives_bar.value = player.live
        self.is_pause = is_pause
        self.score_display.value = (timer, player.score)
        
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_event)
        
        for event in lista_event:
            if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                self.__on_click(BUTTON_PAUSE)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:
            aux_widget.draw()
