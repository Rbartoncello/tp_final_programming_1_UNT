from constantes import *
from functools import reduce
from Gui.gui_play import Play
from Gui.gui_menu_initial import MenuInitial
from Gui.gui_display_end_level import DisplayEndLevel
from Gui.gui_pause import Pause
from Gui.gui_menu_levels import MenuLevels
from Gui.gui_menu_ranking import MenuRanking
from Gui.gui_form_input_name import FormInputName
from Gui.gui_menu_settings import MenuSettings


class StateGame:
    def __init__(self, screen) -> None:
        self.menu_initial = MenuInitial(
            name=MENU_INITIAL,
            master_surface=screen,
            pos=POS_MENU_INITIAL,
            size=(W_MENU, H_MENU),
            image_bg=MENU_BG,
            color_bg=None, color_border=None,
            active=True)

        self.levels = MenuLevels(
            name=MENU_LEVELS,
            master_surface=screen,
            pos=POS_MENU_LEVELS,
            size=(W_MENU, H_MENU),
            image_bg=MENU_BG,
            color_bg=None, color_border=None,
            active=False)

        self.play = Play(
            name=DISPLAY_PLAY,
            master_surface=screen,
            pos=(0, 0),
            size=(W_WINDOWN, H_WINDOWN),
            color_bg=None, color_border=None,
            active=False)

        self.menu_settings = MenuSettings(
            name=MENU_SETTINGS,
            master_surface=screen,
            pos=POS_MENU_INITIAL,
            size=(W_MENU, H_MENU),
            image_bg=MENU_BG,
            color_bg=None, color_border=None,
            active=False)

        self.display_lose = DisplayEndLevel(
            name=DISPLAY_GAME_OVER,
            master_surface=screen,
            pos=POS_MENU_LEVELS,
            size=(W_MENU, H_MENU),
            image_bg=MENU_BG,
            color_bg=None, color_border=None,
            active=False,
            scale=0.8,
            stars=0,
            header=PATH_GAME_OVER
        )

        self.display_win = DisplayEndLevel(
            name=DISPLAY_WIN,
            master_surface=screen,
            pos=POS_MENU_LEVELS,
            size=(W_MENU, H_MENU),
            image_bg=MENU_BG,
            color_bg=None, color_border=None,
            active=False,
            scale=0.8,
            stars=0,
            header=PATH_HEADER_WIN)

        self.display_pause = Pause(
            name=DISPLAY_PAUSE,
            master_surface=screen,
            pos=POS_MENU_LEVELS,
            size=(W_MENU, H_MENU),
            image_bg=MENU_BG,
            color_bg=None, color_border=None,
            active=False,
            scale=0.8,
            is_pause=self.play.level.set_pause)

        self.menu_ranking = MenuRanking(
            name=MENU_RANKING,
            master_surface=screen,
            pos=POS_MENU_LEVELS,
            size=(W_MENU, H_MENU),
            image_bg=MENU_BG,
            color_bg=None, color_border=None,
            active=False)

        self.form_input_names = FormInputName(
            name=FORM_INPUT_NAME,
            master_surface=screen,
            pos=POS_MENU_LEVELS,
            size=(W_MENU, H_MENU),
            image_bg=MENU_BG,
            color_bg=None, color_border=None,
            active=False)

        self.states = [
            self.menu_initial,
            self.levels,
            self.play,
            self.display_lose,
            self.display_win,
            self.display_pause,
            self.menu_ranking,
            self.form_input_names,
            self.menu_settings]

    def run(self, list_event):
        for state in self.states:
            if state.active:
                if state == self.levels:
                    state.last_level_unlock = self.play.current_level
                elif state == self.display_win:
                    state.set_stars(self.play.stars())
                    self.levels.stars_last_level_unlock = self.play.stars()
                elif state == self.play:
                    state.current_level = self.levels.level_selected
                elif state == self.form_input_names and self.play.score:
                    state.score = reduce(lambda x, y: x + y, self.play.score)
                elif state == self.menu_settings:
                    state.sounds = self.play.sound
                state.update(list_event)

                state.draw()
