from random import choice
import pygame as py
from constantes import *
from auxiliar import Auxiliar


class Tramp:
    def __init__(self, data) -> None:
        self.__frame_index = 0
        self.__animations = {key: Auxiliar.getSurfaceFromSpriteSheet(data['path'], data['cols'], data['rows']) for
                             (key, data) in data['animations'].items()}
        self.__status = 'off'
        self.__image = self.__animations[self.__status][self.__frame_index]
        self.__rect = self.__image.get_rect(center=(data['x'], data['y']))
        self.__time_accumulation_animation = 0
        self.__frame_rate_ms = 35

    @property
    def rect(self):
        return self.__rect

    def update(self, delta_ms):
        self.do_animation(delta_ms)

    def do_animation(self, delta_ms):
        self.__time_accumulation_animation += delta_ms
        if self.__time_accumulation_animation >= self.__frame_rate_ms:
            self.__status = 'on'
            self.__time_accumulation_animation = 0
            if self.__frame_index >= len(self.__animations[self.__status]) - 1:
                self.__frame_index = 0
            else:
                self.__frame_index += 1
        elif self.__frame_index >= len(self.__animations[self.__status]) - 1:
            self.__frame_index = 0

    def draw(self, screen):
        try:
            self.__image = self.__animations[self.__status][self.__frame_index]
        except IndexError:
            print("ERROR: ", self.__status, self.__frame_index)
        else:
            screen.blit(self.__image, self.__rect)
        if DEBUG:
            py.draw.rect(screen, CRIMSON, self.__rect)
