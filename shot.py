import pygame as py
from constantes import *
from auxiliar import Auxiliar


class Shot:
    def __init__(self, data, user, pos) -> None:
        self.frame_index = 0
        self.shots = Auxiliar.getSurfaceFromSpriteSheet(PATH_SOURCES + user + data['path'], data['cols'], data['rows'])
        self.shot = self.shots[self.frame_index]
        self.__rect = self.shot.get_rect(midtop=pos)
        self.is_shooting = False
        self.direction = py.math.Vector2(0, 0)
        self.speed = data['speed']

        self.time_shooting_accumulation = 0
        self.time_shooting = data['time_shooting']

    @property
    def rect(self): return self.__rect
    
    def move(self, delta_ms, direction, i):
        self.time_shooting_accumulation += delta_ms
        if self.time_shooting_accumulation >= self.time_shooting and not self.is_shooting:
            self.time_shooting_accumulation = 0
            self.is_shooting = True
            self.direction.x = direction
            self.__rect.x += (self.__rect.w * i + 2*self.__rect.w) * self.direction.x

    def update_position(self, pos):
        if not self.is_shooting:
            self.__rect.center = pos
        else:
            self.__rect.x += self.direction.x * self.speed
            if self.__rect.left > W_WINDOWN or self.__rect.right < 0:
                self.reset()

    def reset(self):
        self.time_shooting_accumulation = 0
        self.is_shooting = False
        
    def check_collisions(self, platform):
        if platform.platform.colliderect(self.__rect):
            self.reset()

    def draw(self, screen):
        try:
            self.shot = self.shots[self.frame_index]
        except IndexError:
            print("ERROR: ", self.status, self.orientation, self.frame_index)
        else:
            screen.blit(self.shot, self.__rect)
        if DEBUG:
            py.draw.rect(screen, YELLOW1, self.__rect)
