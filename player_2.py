import pygame
from constantes import *
from auxiliar import Auxiliar


class Player():
    def __init__(self, data):
        self.__walks_types = {
            LEFT: Auxiliar.getSurfaceFromSpriteSheet(PATH_SOURCES+"Main Characters/Virtual Guy/Wall Jump (32x32).png", 5, 1),
            RIGHT: Auxiliar.getSurfaceFromSpriteSheet(
                PATH_SOURCES+"Main Characters/Virtual Guy/Wall Jump (32x32).png", 5, 1, True)
        }
        self.__jumps_types = {
            RIGHT: Auxiliar.getSurfaceFromSpriteSheet(PATH_SOURCES+"Main Characters/Virtual Guy/Jump (32x32).png", 1, 1),
            LEFT: Auxiliar.getSurfaceFromSpriteSheet(
                PATH_SOURCES+"Main Characters/Virtual Guy/Jump (32x32).png", 1, 1, True)
        }
        self.__stays_types = {
            RIGHT: Auxiliar.getSurfaceFromSpriteSheet(PATH_SOURCES+"Main Characters/Virtual Guy/Idle (32x32).png", 11, 1),
            LEFT: Auxiliar.getSurfaceFromSpriteSheet(
                PATH_SOURCES+"Main Characters/Virtual Guy/Idle (32x32).png", 11, 1, True)
        }

        self._direction = RIGHT
        self._frame = 0
        self._speed_walk = {
            RIGHT: data['speed_walk'],
            LEFT: -data['speed_walk']
        }
        self._speed_run = data['speed_run']
        self._gravity = data['gravity']
        self.animation_time_accumulation = 0
        self.frame_rate_ms = data['frame_rate_ms']
        self.lives = 5
        self.score = 0
        self.move = pygame.math.Vector2(0, 0)
        self.jump_power = data['jump_power']
        self.animation = self.__stays_types[self._direction]
        self.image = self.animation[self._frame]
        self.rect = self.image.get_rect(bottomleft=(data['x'], data['y']))
        self.movement_time_accumulation = 0
        self.move_rate_ms = data['move_rate_ms']
        self.y_start_jump = 0
        self.jump_height = data['jump_height']
        self.rects = {
            TOP: pygame.Rect((0, 0), (self.rect.w / 2, W_H_RECT)),
            GROUND: pygame.Rect((0, 0), (self.rect.w / 3, W_H_RECT)),
            LEFT: pygame.Rect((self.rect.left, self.rect.y), (W_H_RECT, self.rect.h)),
            RIGHT: pygame.Rect(
                (self.rect.right-W_H_RECT, self.rect.y), (W_H_RECT, self.rect.h))
        }
        self.is_jump = False
        self.is_fall = False

        self.rects[GROUND].midbottom = self.rect.midbottom
        self.rects[TOP].midtop = self.rect.midtop

    def walk(self, direction):
        if not self.is_jump:
            if self._direction != direction or self.animation != self.__walks_types[self._direction]:
                self._frame = 0
                self._direction = direction
                self.animation = self.__walks_types[self._direction]
                self.move.x = self._speed_walk[self._direction]

    def jump(self, on_off=True):
        if on_off and not self.is_jump and not self.is_fall:
            self.y_start_jump = self.rect.bottom

            self.move.x = self._speed_walk[self._direction]

            self.animation = self.__jumps_types[self._direction]
            self._frame = 0
            self.is_jump = True
            self.move.y = -self.jump_power
        if not on_off:
            self.is_jump = False
            self.stay()

    def stay(self):
        if self.animation != self.__stays_types[self._direction]:
            self.animation = self.__stays_types[self._direction]
            self.move.xy = (0, 0)
            self._frame = 0

    def collisioned_with_platform(self, ubication, platforms):
        return list(filter(lambda platform: self.rects[ubication].colliderect(platform.side(ubication)), platforms))

    def is_on_platform(self, platforms):
        retorno = False
        if self.rect.bottom >= FLOOR + 1000:
            retorno = True
        elif self.collisioned_with_platform(GROUND, platforms):
            retorno = True
        return retorno

    def do_movement(self, delta_ms, platforms):
        self.movement_time_accumulation += delta_ms
        if self.movement_time_accumulation >= self.move_rate_ms:

            for platform in platforms:
                if self.rects[RIGHT].colliderect(platform.side(LEFT)):
                    self.rect.right = platform.side(LEFT).left
                if self.rects[LEFT].colliderect(platform.side(RIGHT)):
                    self.rect.left = platform.side(RIGHT).right
                if self.rects[TOP].colliderect(platform.side(TOP)):
                    print("toco")
                    self.move.y = 0

            if abs(self.y_start_jump) - abs(self.rect.bottom) > self.jump_height and self.is_jump:
                self.move.y = 0

            self.update_position(self.move.xy)

            if not self.is_on_platform(platforms):
                if self.move.y == 0:
                    self.is_fall = True
                    self.update_position((0, self._gravity))
            else:
                if self.is_jump:
                    self.jump(False)
                self.is_fall = False

    def do_animation(self, delta_ms):
        self.animation_time_accumulation += delta_ms
        if self.animation_time_accumulation >= self.frame_rate_ms:
            self.animation_time_accumulation = 0
            if self._frame >= len(self.animation) - 1:
                self._frame = 0
            else:
                self._frame += 1

    def update(self, delta_ms, platforms):
        self.do_movement(delta_ms, platforms)
        self.do_animation(delta_ms)

    def update_position(self, pos):
        self.rect = pygame.Rect.move(self.rect, pos)
        self.rects[GROUND].midbottom = self.rect.midbottom
        self.rects[TOP].midtop = self.rect.midtop
        self.rects[LEFT].midleft = self.rect.midleft
        self.rects[RIGHT].midright = self.rect.midright

    def draw(self, screen):
        self.image = self.animation[self._frame]
        screen.blit(self.image, self.rect)
        if DEBUG:
            pygame.draw.rect(screen, RED1, self.rect)
            pygame.draw.rect(screen, GREEN1, self.rects[GROUND])
            pygame.draw.rect(screen, GREEN2, self.rects[TOP])
            pygame.draw.rect(screen, GREEN3, self.rects[LEFT])
            pygame.draw.rect(screen, GREEN4, self.rects[RIGHT])
        #self.image = self.animation[self._frame]
        #screen.blit(self.image, self.rect)

    def events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            self.walk(LEFT)

        elif not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            self.walk(RIGHT)

        elif (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]) or (
                keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.stay()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jump(True)
