import pygame as py
from random import randint, choice
from constantes import *
from auxiliar import Auxiliar


class Enemy():
    def __init__(self, data) -> None:
        self.animations = {}
        for animation in data['animations']:
            self.animations[animation] = self.create_sides_animation(data['animations'][animation], data['type'])
        
        self.frame_index = 0
        self.orientation = choice([LEFT, RIGHT])
        self.status = RUN
        self.image = self.animations[self.status][self.orientation][self.frame_index]
        self.rect = self.image.get_rect(topleft=(data['x'], data['y']))
        self.rects = {
            LEFT: py.Rect((self.rect.left, self.rect.top - W_H_RECT), (W_H_RECT, self.rect.h - W_H_RECT)),
            RIGHT: py.Rect((self.rect.right - W_H_RECT, W_H_RECT),(W_H_RECT, self.rect.h - W_H_RECT))
        }

        self.frame_index_shot = 0
        self.shots = Auxiliar.getSurfaceFromSpriteSheet(
            PATH_SOURCES+data['type']+"Leafs.png", 2, 1)
        self.shot = self.shots[self.frame_index_shot]
        self.rect_shot = self.shot.get_rect(midtop=self.rect.midtop)
        self.is_shooting = False
        self.direction_shot = py.math.Vector2(0, 0)

        self.direction = py.math.Vector2(0, 0)
        self.speed = data["speed"]
        self.gravity = data["gravity"]
        self.jump_speed = data['jump_speed']

        self.animation_time_accumulation = 0
        self.frame_rate_ms = data['frame_rate_ms']

        self.time_shooting_accumulation = 0
        self.time_shooting = 1000
    
    def create_side_animation(self, data, name, side):
        return Auxiliar.getSurfaceFromSpriteSheet(PATH_SOURCES+name+data['path'], data['cols'], data['rows'], data[side])
    
    def create_sides_animation(self, data, name):
        return {
            RIGHT: self.create_side_animation(data,name, RIGHT),
            LEFT: self.create_side_animation(data,name, LEFT)
        }

    def do_animation(self, delta_ms):
        self.animation_time_accumulation += delta_ms
        if self.animation_time_accumulation >= self.frame_rate_ms:
            self.animation_time_accumulation = 0
            if self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
                self.frame_index = 0
            else:
                self.frame_index += 1

    def do_moving(self, delta_ms):
        self.animation_time_accumulation += delta_ms
        if self.animation_time_accumulation >= self.frame_rate_ms:
            self.animation_time_accumulation = 0
            if self.orientation == RIGHT:
                self.direction.x = 1
            elif self.orientation == LEFT:
                self.direction.x = -1
            self.update_position((self.direction.x * self.speed, 0))
            self.do_shooting(delta_ms)

    def do_shooting(self, delta_ms):
        self.time_shooting_accumulation += delta_ms
        if self.time_shooting_accumulation >= self.time_shooting and not self.is_shooting:
            self.time_shooting_accumulation = 0
            self.is_shooting = True
            self.direction_shot.x = self.direction.x

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.update_position(self.direction)

    def update(self, delta_ms):
        self.do_animation(delta_ms)
        self.apply_gravity()
        self.do_moving(delta_ms)

    def update_position(self, pos):
        self.rect = py.Rect.move(self.rect, pos)
        self.rects[RIGHT].midright = self.rect.midright
        self.rects[LEFT].midleft = self.rect.midleft
        if not self.is_shooting:
            self.rect_shot.center = self.rect.center
        else:
            self.rect_shot.x += self.direction_shot.x * self.speed * 2
            if self.rect_shot.left > W_WINDOWN or self.rect_shot.right < 0:
                self.time_shooting_accumulation = 0
                self.is_shooting = False

    def draw(self, screen):
        try:
            self.image = self.animations[self.status][self.orientation][self.frame_index]
            self.shot = self.shots[self.frame_index_shot]
        except IndexError:
            print("ERROR: ", self.status, self.orientation, self.frame_index)
        else:
            screen.blit(self.shot, self.rect_shot)
            screen.blit(self.image, self.rect)
        if DEBUG:
            py.draw.rect(screen, RED1, self.rect)
            py.draw.rect(screen, YELLOW1, self.rect_shot)
            py.draw.rect(screen, WHITE, self.rects[LEFT])
            py.draw.rect(screen, WHITE, self.rects[RIGHT])

    def side(self, side):
        return self.rects[side]
