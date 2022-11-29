from constantes import *
from Gui.gui_play import Play
from Gui.gui_menu_initial import MenuInitial
from Gui.gui_display_end_level import DisplayEndLevel
from Gui.gui_pause import Pause
from Gui.gui_menu_levels import MenuLevels


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

        self.states = [self.menu_initial, self.levels, self.play, self.display_lose, self.display_win,
                       self.display_pause]

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
                state.update(list_event)
                state.draw()
