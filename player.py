import pygame as py
from constantes import *
from auxiliar import Auxiliar


class Player():
    def __init__(self, data):
        self.create_animations(data)
        self.frame_index = 0
        self.orientation = RIGHT
        self.status = IDLE
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

    def update(self, delta_ms):
        self.get_input()
        self.get_status()
        self.do_animation(delta_ms)
        self.apply_gravity()

    def update_position(self, pos):
        self.rect = py.Rect.move(self.rect, pos)
        self.rects[RIGHT].midright = self.rect.midright
        self.rects[LEFT].midleft = self.rect.midleft

    def get_input(self):
        keys = py.key.get_pressed()

        if keys[py.K_RIGHT] and not keys[py.K_LEFT]:
            self.direction.x = 1
            self.orientation = RIGHT
            self.update_position((self.direction.x * self.speed, 0))

        elif keys[py.K_LEFT] and not keys[py.K_RIGHT]:
            self.direction.x = -1
            self.orientation = LEFT
            self.update_position((self.direction.x * self.speed, 0))

        elif not keys[py.K_LEFT] and not keys[py.K_RIGHT] or keys[py.K_LEFT] and keys[py.K_RIGHT]:
            self.direction.x = 0
        for event in py.event.get():
            if event.type == py.KEYDOWN and event.key == py.K_SPACE:
                self.jump()

    def get_status(self):
        if self.direction.y < 0:
            self.status = JUMP
        elif self.direction.y > 1:
            self.status = FALL
        else:
            if self.direction.x != 0:
                self.status = RUN
            else:
                self.status = IDLE

    def draw(self, screen):
        try:
            self.image = self.animations[self.status][self.orientation][self.frame_index]
        except IndexError:
            print("ERROR: ", self.status, self.orientation, self.frame_index)
        else:
            screen.blit(self.image, self.rect)
        if DEBUG:
            py.draw.rect(screen, RED1, self.rect)
            py.draw.rect(screen, WHITE, self.rects[LEFT])
            py.draw.rect(screen, WHITE, self.rects[RIGHT])

    def side(self, side):
        return self.rects[side]
