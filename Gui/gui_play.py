import json
import pygame as py
from pygame.locals import *
from constantes import *
from Gui.gui_form_in_game import FormInGame
from Gui.gui_form import Form

from level import Level


with open(FILE, 'r') as archivo:
    data = json.load(archivo)
class Play(Form):
    def __init__(self, name, master_surface, pos, size, color_bg, color_border,active):
        super().__init__(name, master_surface, pos, size, color_bg, color_border, active)
        self.level = Level(master_surface, data)
        self.form_in_game = FormInGame(
            name="form_in_game",
            master_surface=master_surface,
            pos=(0, 0),
            size=(W_WINDOWN, H_FORM_IN_GAME),
            color_bg=None, color_border=None,
            value=self.level.player,
            active=False)
        self.__is_pause = False
        self.clock = py.time.Clock()
        self.flag = True
        self.cache = 0
        self.__current_level = 1
    
    def current_level(self): 
        return self.__current_level
    
    def stars(self): 
        return self.level.stars()
    
    def update(self, list_event):
        if not self.level.lost():
            if self.level.win():
                self.__current_level+= 1
                self.set_active(DISPLAY_WIN)
            else:
                self.level.run(self.clock.tick(FPS))
                self.form_in_game.active = True
                if self.form_in_game.active and not self.level.lost():
                    self.form_in_game.update(list_event, self.level.player, self.level.timer, self.level.set_pause)
        else:
            self.set_active(DISPLAY_GAME_OVER)


    def draw(self):
        if self.form_in_game.active and  not self.level.lost():
            self.form_in_game.draw()
