from random import choice
import pygame as py
from constantes import *
from auxiliar import Auxiliar


def create_side_animation(data, name, side):
    return Auxiliar.getSurfaceFromSpriteSheet(PATH_SOURCES + name + data['path'], data['cols'], data['rows'],data[side])


def create_sides_animation(data, name):
    return {
        RIGHT: create_side_animation(data, name, RIGHT),
        LEFT: create_side_animation(data, name, LEFT)
    }


class Character:
    def __init__(self, data):
        self.animations = None
        self.create_animations(data)
        self.frame_index = 0
        self.status = data['status_init']
        self.orientation = choice(data['orientation_init'])

        self.image = self.animations[self.status][self.orientation][self.frame_index]
        self._rect = self.image.get_rect(topleft=(data['x'], data['y']))
        self.rects = {
            TOP: py.Rect((self._rect.left, self._rect.top), (self._rect.w - W_H_RECT * 2, W_H_RECT)),
            GROUND: py.Rect((self._rect.left, self._rect.bottom - W_H_RECT), (self._rect.w - W_H_RECT * 2, W_H_RECT)),
            LEFT: py.Rect((self._rect.left, self._rect.top), (W_H_RECT, self._rect.h - W_H_RECT * 2)),
            RIGHT: py.Rect((self._rect.right - W_H_RECT, self._rect.top),
                           (W_H_RECT, self._rect.h - W_H_RECT * 2))
        }

        self.direction = py.math.Vector2(0, 0)
        self.speed = data["speed"]
        self.gravity = data["gravity"]
        self.jump_speed = data['jump_speed']

        self.time_accumulation_animation = 0
        self.frame_rate_ms = data['frame_rate_ms']
        self._time_accumulation_die = 0

        self._was_die = False

    def create_animations(self, data):
        self.animations = {}
        for animation in data['animations']:
            self.animations[animation] = create_sides_animation(
                data['animations'][animation], data['type'])

    @property
    def rect(self):
        return self._rect

    @property
    def was_die(
            self):
        return self._was_die and self._time_accumulation_die >= TIME_TO_DIE
 
    def update(self, delta_ms):
        self.do_animation(delta_ms, self._was_die)
        self.apply_gravity()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.update_position(self.direction)

    def jump(self, collided=False):
        if (self.status != JUMP and self.status != FALL) or collided:
            self.direction.y = self.jump_speed

    def do_animation(self, delta_ms, was_die=False):
        self.time_accumulation_animation += delta_ms
        if was_die:
            self._time_accumulation_die += delta_ms
        if self.time_accumulation_animation >= self.frame_rate_ms:
            self.time_accumulation_animation = 0
            if self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
                self.frame_index = 0
            else:
                self.frame_index += 1
        elif self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
            self.frame_index = 0

    def update_position(self, pos):
        self._rect = py.Rect.move(self._rect, pos)
        self.rects[TOP].midtop = self._rect.midtop
        self.rects[GROUND].midbottom = self._rect.midbottom
        self.rects[RIGHT].midright = self._rect.midright
        self.rects[LEFT].midleft = self._rect.midleft

    def side(self, side):
        return self.rects[side]

    def die(self):
        self.frame_index = 0
        self.status = HIT
        self._was_die = True

    def draw(self, screen):
        try:
            self.image = self.animations[self.status][self.orientation][self.frame_index]
        except IndexError:
            print("ERROR: ", self.status, self.orientation, self.frame_index)
        else:
            screen.blit(self.image, self._rect)
        Auxiliar.debuggerMod(screen=screen, color_main=RED1, color_top=WHITE, color_bottom=WHITE,
                             color_left=WHITE, color_right=WHITE, rect_main=self._rect, rects=self.rects)
