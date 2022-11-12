import pygame as py
from constantes import *
from character import Character
from shot import Shot


class Enemy(Character):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.was_killed = False
        
        self.rect_sensor = py.Rect(self.rect.centerx, self.rect.centery, W_WINDOWN-self.rect.centerx, 5)
        self.sensor_activate = False

        self.__shots = []
        for i in range(data['amount_shot']):
            self.__shots.append(
                Shot(data['shot'], data['type'], self.rect.midtop))

    @property
    def shots(self):
        return self.__shots

    def do_moving(self, delta_ms):
        self.time_accumulation_animation += delta_ms
        if self.time_accumulation_animation >= self.frame_rate_ms:
            self.time_accumulation_animation = 0
            if self.orientation == RIGHT:
                self.direction.x = 1
            elif self.orientation == LEFT:
                self.direction.x = -1
            self.update_position((self.direction.x * self.speed, 0))
        if not self.was_killed and self.sensor_activate:
            for i, shot in enumerate(self.__shots):
                shot.move(delta_ms, self.direction.x, i)

    def update(self, delta_ms):
        self.do_animation(delta_ms, self.was_killed)
        self.apply_gravity()
        self.do_moving(delta_ms)

    def update_position(self, pos):
        if not self.was_killed:
            super().update_position(pos)
            if self.orientation == RIGHT:
                self.rect_sensor.midleft = self.rect.center
                self.rect_sensor.w = W_WINDOWN-self.rect.centerx
            elif self.orientation == LEFT:
                self.rect_sensor.midleft = (0,self.rect.centery)
                self.rect_sensor.w = self.rect.centerx
        for shot in self.__shots:
            shot.update_position(self.rect.center)

    def check_collisions(self, platforms, player):
        if platforms:
            for platform in platforms:
                if platform.side(GROUND).colliderect(self.rect):
                    self.rect.bottom = platform.side(GROUND).top
                    self.direction.y = 0
                if platform.side(RIGHT).colliderect(self.rects[LEFT]) and self.direction.x < 0:
                    self.orientation = RIGHT
                if platform.side(LEFT).colliderect(self.rects[RIGHT]) and self.direction.x > 0:
                    self.orientation = LEFT
                for shot in self.__shots:
                    shot.check_collisions(platform)
        if player.side(GROUND).colliderect(self.rects[TOP]):
            player.jump(True)
            self.status = HIT
            self.was_killed = True
        if player.rect.colliderect(self.rect_sensor):
            self.sensor_activate = True
            print(self.sensor_activate)
        else:
            self.sensor_activate = False

    def was_kill(self):
        return self.was_killed and self.time_accumulation_kill >= TIME_TO_DIE

    def draw(self, screen):
        for shot in self.__shots:
            shot.draw(screen)
        super().draw(screen)
        if DEBUG:
            py.draw.rect(screen, ORANGE, self.rect_sensor)
