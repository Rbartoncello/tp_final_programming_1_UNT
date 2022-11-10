import pygame as py
from constantes import *
from character import Character
from shot import Shot


class Enemy(Character):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.shots = []
        for i in range(data['amount_shot']):
            self.shots.append(
                Shot(data['shot'], data['type'], self.rect.midtop))

    def do_moving(self, delta_ms):
        self.animation_time_accumulation += delta_ms
        if self.animation_time_accumulation >= self.frame_rate_ms:
            self.animation_time_accumulation = 0
            if self.orientation == RIGHT:
                self.direction.x = 1
            elif self.orientation == LEFT:
                self.direction.x = -1
            self.update_position((self.direction.x * self.speed, 0))
            for i, shot in enumerate(self.shots):
                shot.move(delta_ms, self.direction.x, i)

    def update(self, delta_ms):
        self.do_animation(delta_ms)
        self.apply_gravity()
        self.do_moving(delta_ms)

    def update_position(self, pos):
        self.rect = py.Rect.move(self.rect, pos)
        self.rects[RIGHT].midright = self.rect.midright
        self.rects[LEFT].midleft = self.rect.midleft
        for i, shot in enumerate(self.shots):
            shot.update_position(self.rect.center)

    def check_collisions(self, platforms):
        for platform in platforms:
            if platform.side(GROUND).colliderect(self.rect):
                self.rect.bottom = platform.side(GROUND).top
                self.direction.y = 0
            if platform.side(RIGHT).colliderect(self.rects[LEFT]) and self.direction.x < 0:
                self.orientation = RIGHT
            if platform.side(LEFT).colliderect(self.rects[RIGHT]) and self.direction.x > 0:
                self.orientation = LEFT
            for shot in self.shots:
                shot.check_collisions(platform)

    def draw(self, screen):
        for shot in self.shots:
            shot.draw(screen)
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
