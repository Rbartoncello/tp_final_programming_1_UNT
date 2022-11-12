from random import choice
import pygame as py
from constantes import *
from auxiliar import Auxiliar


class Character():
    def __init__(self, data):
        self.animations = None
        self.create_animations(data)
        self.frame_index = 0
        self.status = data['status_init']
        self.orientation = choice(data['orientation_init'])

        self.image = self.animations[self.status][self.orientation][self.frame_index]
        self.rect = self.image.get_rect(topleft=(data['x'], data['y']))
        self.rects = {
            TOP: py.Rect((self.rect.left, self.rect.top), (self.rect.w-W_H_RECT*2, W_H_RECT)),
            GROUND: py.Rect((self.rect.left, self.rect.bottom - W_H_RECT), (self.rect.w-W_H_RECT*2, W_H_RECT)),
            LEFT: py.Rect((self.rect.left, self.rect.top), (W_H_RECT, self.rect.h - W_H_RECT*2)),
            RIGHT: py.Rect((self.rect.right - W_H_RECT, self.rect.top),
                           (W_H_RECT, self.rect.h - W_H_RECT*2))
        }

        self.direction = py.math.Vector2(0, 0)
        self.speed = data["speed"]
        self.gravity = data["gravity"]
        self.jump_speed = data['jump_speed']

        self.time_accumulation_animation = 0
        self.frame_rate_ms = data['frame_rate_ms']
        self.time_accumulation_kill = 0

    def create_animations(self, data):
        self.animations = {}
        for animation in data['animations']:
            self.animations[animation] = self.create_sides_animation(
                data['animations'][animation], data['type'])

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

    def jump(self, collided=False):
        if (self.status != JUMP and self.status != FALL) or collided:
            self.direction.y = self.jump_speed

    def do_animation(self, delta_ms, was_kill=False):
        self.time_accumulation_animation += delta_ms
        if was_kill:
            self.time_accumulation_kill += delta_ms
        if self.time_accumulation_animation >= self.frame_rate_ms:
            self.time_accumulation_animation = 0
            if self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
                self.frame_index = 0
            else:
                self.frame_index += 1
        elif self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
            self.frame_index = 0
    
    def update_position(self, pos):
        self.rect = py.Rect.move(self.rect, pos)
        self.rects[TOP].midtop = self.rect.midtop
        self.rects[GROUND].midbottom = self.rect.midbottom
        self.rects[RIGHT].midright = self.rect.midright
        self.rects[LEFT].midleft = self.rect.midleft

    def side(self, side):
        return self.rects[side]

    def draw(self, screen):
        try:
            self.image = self.animations[self.status][self.orientation][self.frame_index]
        except IndexError:
            print("ERROR: ", self.status, self.orientation, self.frame_index)
        else:
            
            screen.blit(self.image, self.rect)
        Auxiliar.debuggerMod(screen=screen, color_main=RED1, color_top=WHITE, color_bottom=WHITE, color_left=WHITE, color_right=WHITE, rect_main=self.rect, rects=self.rects)
