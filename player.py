import pygame as py
from constantes import *
from auxiliar import Auxiliar
from character import Character

class Player(Character):
    def __init__(self, data):
        super().__init__(data)
        self.live = data['live']
        self.score = 0

    def update(self, delta_ms):
        self.get_input()
        self.get_status()
        self.do_animation(delta_ms)
        self.apply_gravity()

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
                
    def check_collisions(self, platforms, enemies, fruits):
        if platforms:
            for platform in platforms:
                if platform.side(RIGHT).colliderect(self.rects[LEFT]) and self.direction.x < 0:
                    self.rect.left = platform.side(RIGHT).right
                if platform.side(LEFT).colliderect(self.rects[RIGHT]) and self.direction.x > 0:
                    self.rect.right = platform.side(LEFT).left
                if platform.side(TOP).colliderect(self.rect):
                    self.rect.top = platform.side(TOP).bottom
                    self.direction.y = 0
                if platform.side(GROUND).colliderect(self.rect):
                    self.rect.bottom = platform.side(GROUND).top
                    self.direction.y = 0
        if enemies:
            for enemy in enemies:
                if enemy.shots:
                    for shot in enemy.shots:
                        if shot.rect.colliderect(self.rect):
                            shot.reset()
                            self.live -= 1
                            if self.live == 0:
                                pass
                    if enemy.side(RIGHT).colliderect(self.rects[LEFT]):
                        pass
                    if enemy.side(LEFT).colliderect(self.rects[RIGHT]):
                        pass
        if fruits:
            for fruit in fruits:
                if self.rect.colliderect(fruit.rect):
                    fruit.collecte()