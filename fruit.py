import pygame as py
from constantes import *
from auxiliar import Auxiliar


def create_animation(data):
    return Auxiliar.getSurfaceFromSpriteSheet(data['path'], data['cols'], data['rows'])


class Fruit:
    def __init__(self, data) -> None:
        self.__frame_index = 0
        self.__animations = {}
        self.__create_animations(data)
        self.__status = IDLE
        self.__image = self.__animations[self.__status][self.__frame_index]
        self.__rect = self.__image.get_rect(topleft=(data['x'], data['y']))
        self.__time_accumulation_animation = 0
        self.__frame_rate_ms = 30
        self.__was_collected = False
        self.sumo_punto = False

    @property
    def rect(self):
        return self.__rect

    @property
    def was_collected(self):
        return self.__was_collected and self.__frame_index >= len(self.__animations[COLLECTED]) - 1

    @property
    def was_pick_up(self):
        if self.__was_collected and not self.sumo_punto:
            self.sumo_punto = True
            return True
        else:
            False

    def pick_up(self):
        if not self.__was_collected:
            self.__frame_index = 0
        self.__was_collected = True
        self.__status = COLLECTED
        self.__frame_rate_ms = 50

    def __create_animations(self, data):
        for animation in data['animations']:
            self.__animations[animation] = create_animation(data['animations'][animation])

    def update(self, delta_ms):
        self.do_animation(delta_ms)

    def do_animation(self, delta_ms):
        self.__time_accumulation_animation += delta_ms
        if not (self.__was_collected and self.__frame_index >= len(self.__animations[COLLECTED]) - 1):
            if self.__time_accumulation_animation >= self.__frame_rate_ms:
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
            py.draw.rect(screen, SIENNA, self.__rect)
