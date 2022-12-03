import json
import pygame as py
from pygame.locals import *
from constantes import *
from Gui.gui_form_in_game import FormInGame
from Gui.gui_form import Form

from level import Level


class Play(Form):
    def __init__(self, name, master_surface, pos, size, color_bg, color_border, active):
        super().__init__(name, master_surface, pos, size, color_bg, color_border, active)
        self.level = Level(master_surface, 1)
        self.form_in_game = FormInGame(
            name="form_in_game",
            master_surface=master_surface,
            pos=(0, 0),
            size=(W_WINDOWN, H_FORM_IN_GAME),
            color_bg=None, color_border=None,
            value=self.level.player,
            active=False)
        self.clock = py.time.Clock()
        self.flag = True
        self.cache = 0
        self.__current_level = 1
        self.__score = []
        self.__sound = py.mixer.Sound('sound/game_win.mp3')
    
    @property
    def sound(self):
        sounds = self.level.sound
        
        sounds.append(self.__sound)
        sounds.append(sound)
        
        return sounds
    
    @property
    def current_level(self): 
        return self.__current_level
    
    @property
    def score(self): 
        return self.__score
    
    @current_level.setter
    def current_level(self, level): 
        self.__current_level = level

    def stars(self):
        return self.level.stars

    def update(self, list_event):
        if not self.level.lost:
            if self.__current_level != self.level.level:
                self.level = Level(self.master_surface, self.__current_level)
            else: 
                if self.flag:
                    self.level = Level(self.master_surface, self.__current_level)
                    self.flag = False
                elif self.level.win:
                    self.__sound = py.mixer.Sound('sound/game_win.mp3')
                    sound.set_volume(0.1)
                    self.__sound.set_volume(0.9)
                    self.__sound.play()
                    self.__score.insert(self.__current_level, self.level.score)
                    self.__current_level += 1
                    self.set_active(DISPLAY_WIN)
                    self.flag = True
                else:
                    self.level.run(self.clock.tick(FPS))
                    self.form_in_game.active = True
                    if self.form_in_game.active and not self.level.lost:
                        self.form_in_game.update(
                            list_event, self.level.player, self.level.timer, self.level.set_pause)
        else:
            self.level = Level(self.master_surface, self.__current_level)
            self.set_active(DISPLAY_GAME_OVER)

    def draw(self):
        if self.form_in_game.active and not self.level.lost:
            self.form_in_game.draw()
            
            
    def reset_level(self, level):
        self.level.reset(level)
