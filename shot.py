import pygame as py
from constantes import *
from auxiliar import Auxiliar


class Shot:
    def __init__(self, data, user, pos) -> None:
        self.frame_index = 0
        self.shots = Auxiliar.getSurfaceFromSpriteSheet(PATH_SOURCES + user + data['path'], data['cols'], data['rows'])
        self.shot = self.shots[self.frame_index]
        self.rect = self.shot.get_rect(midtop=pos)
        self.is_shooting = False
        self.direction = py.math.Vector2(0, 0)
        self.speed = data['speed']

        self.time_shooting_accumulation = 0
        self.time_shooting = data['time_shooting']

    def move(self, delta_ms, direction, i):
        self.time_shooting_accumulation += delta_ms
        if self.time_shooting_accumulation >= self.time_shooting and not self.is_shooting:
            self.time_shooting_accumulation = 0
            self.is_shooting = True
            self.direction.x = direction
            self.rect.x += (self.rect.w * i + self.rect.w) * self.direction.x

    def update_position(self, pos):
        if not self.is_shooting:
            self.rect.center = pos
        else:
            self.rect.x += self.direction.x * self.speed
            if self.rect.left > W_WINDOWN or self.rect.right < 0:
                self.time_shooting_accumulation = 0
                self.is_shooting = False
                
    def check_collisions(self, platform):
        if platform.platform.colliderect(self.rect):
            self.time_shooting_accumulation = 0
            self.is_shooting = False

    def draw(self, screen):
        try:
            self.shot = self.shots[self.frame_index]
        except IndexError:
            print("ERROR: ", self.status, self.orientation, self.frame_index)
        else:
            screen.blit(self.shot, self.rect)
        if DEBUG:
            py.draw.rect(screen, YELLOW1, self.rect)
