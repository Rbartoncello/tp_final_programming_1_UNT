import pygame as py
from constantes import *
from character import Character
from shot import Shot


class Enemy(Character):
    def __init__(self, data) -> None:
        super().__init__(data)

        self.__sensors = {
            HORIZONTAL: py.Rect(self._rect.centerx, self._rect.centery, W_WINDOWN-self._rect.centerx, W_H_RECT_SENSOR),
            VERTICAL: py.Rect(self._rect.centerx, self._rect.centery, W_H_RECT_SENSOR, H_WINDOWN-self._rect.centerx)
        }
        self.type_sensor = data['type_sensor']
        self.__rect_sensor = self.__sensors[self.type_sensor]
        self.__sensor_activate = False

        self.__shots = []
        for i in range(data['amount_shot']):
            self.__shots.append(
                Shot(data['shot'], data['type'], self._rect.midtop))

    @property
    def shots(self): return self.__shots

    def do_moving(self, delta_ms):
        self.time_accumulation_animation += delta_ms
        if self.time_accumulation_animation >= self.frame_rate_ms:
            self.time_accumulation_animation = 0
            if self.orientation == RIGHT:
                self.direction.x = 1
            elif self.orientation == LEFT:
                self.direction.x = -1
            self.update_position((self.direction.x * self.speed, 0))
        if not self._was_die and self.__sensor_activate:
            for i, shot in enumerate(self.__shots):
                shot.move(delta_ms, self.direction.x, i)

    def update(self, delta_ms):
        super().update(delta_ms)
        self.do_moving(delta_ms)

    def update_position(self, pos):
        if not self._was_die:
            super().update_position(pos)
            if self.type_sensor == HORIZONTAL:
                if self.orientation == RIGHT:
                    self.__rect_sensor.midleft = self._rect.center
                    self.__rect_sensor.w = W_WINDOWN-self._rect.centerx
                elif self.orientation == LEFT:
                    self.__rect_sensor.midleft = (0, self._rect.centery)
                    self.__rect_sensor.w = self._rect.centerx
            elif self.type_sensor == VERTICAL:
                self.__rect_sensor.midtop = self._rect.center
                self.__rect_sensor.h = H_WINDOWN - self._rect.centery
        for shot in self.__shots:
            shot.update_position(self._rect.center)

    def check_collisions(self, platforms, player):
        if platforms:
            for platform in platforms:
                if platform.side(GROUND).colliderect(self._rect):
                    self._rect.bottom = platform.side(GROUND).top
                    self.direction.y = 0
                if platform.side(RIGHT).colliderect(self.rects[LEFT]) and self.direction.x < 0:
                    self.orientation = RIGHT
                if platform.side(LEFT).colliderect(self.rects[RIGHT]) and self.direction.x > 0:
                    self.orientation = LEFT
                for shot in self.__shots:
                    shot.check_collisions(platform)

        if player is not None:
            if self.rects[LEFT].colliderect(player.side(RIGHT)):
                if not self._was_die:
                    player.die('sound/game_over.mp3')
            if self.rects[RIGHT].colliderect(player.side(LEFT)):
                if not self._was_die:
                    player.die('sound/game_over.mp3')
            if player.rect.colliderect(self.__rect_sensor):
                self.__sensor_activate = True
            else:
                self.__sensor_activate = False

    def draw(self, screen):
        for shot in self.__shots:
            shot.draw(screen)
        super().draw(screen)
        if DEBUG:
            py.draw.rect(screen, ORANGE, self.__rect_sensor)
