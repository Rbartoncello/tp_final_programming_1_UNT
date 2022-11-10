from random import choice
import pygame as py
from constantes import *
from auxiliar import Auxiliar


class Character():
    def __init__(self, data):
        self.create_animations(data)
        self.frame_index = 0
        self.status = data['status_init']
        self.orientation = choice(data['orientation_init'])

        self.image = self.animations[self.status][self.orientation][self.frame_index]
        self.rect = self.image.get_rect(topleft=(data['x'], data['y']))
        self.rects = {
            LEFT: py.Rect((self.rect.left, self.rect.top - W_H_RECT), (W_H_RECT, self.rect.h - W_H_RECT)),
            RIGHT: py.Rect((self.rect.right - W_H_RECT, W_H_RECT),(W_H_RECT, self.rect.h - W_H_RECT))
        }

        self.direction = py.math.Vector2(0, 0)
        self.speed = data["speed"]
        self.gravity = data["gravity"]
        self.jump_speed = data['jump_speed']

        self.animation_time_accumulation = 0
        self.frame_rate_ms = data['frame_rate_ms']
        
    def create_animations(self, data):
        self.animations = {}
        for animation in data['animations']:
            self.animations[animation] = self.create_sides_animation(data['animations'][animation], data['type'])

    def create_side_animation(self, data, name, side):
        return Auxiliar.getSurfaceFromSpriteSheet(PATH_SOURCES+name+data['path'], data['cols'], data['rows'], data[side])

    def create_sides_animation(self, data, name):
        return {
            RIGHT: self.create_side_animation(data, name, RIGHT),
            LEFT: self.create_side_animation(data, name, LEFT)
        }
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.update_position(self.direction)
        
    def jump(self):
        if self.status != JUMP and self.status != FALL:
            self.direction.y = self.jump_speed
        
    def do_animation(self, delta_ms):
        self.animation_time_accumulation += delta_ms
        if self.animation_time_accumulation >= self.frame_rate_ms:
            self.animation_time_accumulation = 0
            if self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
                self.frame_index = 0
            else:
                self.frame_index += 1
        elif self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
            self.frame_index = 0

    def side(self, side):
        return self.rects[side]