import pygame as py
from constantes import *
from character import Character


class Player(Character):
    def __init__(self, data):
        super().__init__(data)
        self.__live = data['live']
        self.__score = 0
        

    @property
    def score(self): return self.__score

    @score.setter
    def score(self, score): self.__score += score
    
    @property
    def live(self): return self.__live

    def update(self, delta_ms):
        if not self._was_die:
            self.get_input()
            self.get_status()
        super().update(delta_ms)

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

    def check_collisions(self, platforms, enemies, fruits, tramps):
        if platforms:
            for platform in platforms:
                if platform.side(RIGHT).colliderect(self.rects[LEFT]) and self.direction.x < 0:
                    self._rect.left = platform.side(RIGHT).right
                if platform.side(LEFT).colliderect(self.rects[RIGHT]) and self.direction.x > 0:
                    self._rect.right = platform.side(LEFT).left
                if platform.side(TOP).colliderect(self._rect):
                    self._rect.top = platform.side(TOP).bottom
                    self.direction.y = 0
                if platform.side(GROUND).colliderect(self._rect):
                    self._rect.bottom = platform.side(GROUND).top
                    self.direction.y = 0
        if enemies:
            for enemy in enemies:
                if enemy.shots:
                    for shot in enemy.shots:
                        if shot.rect.colliderect(self._rect) and not shot.rect.x in range(enemy.rect.left, enemy.rect.right):
                            shot.reset()
                            self.__live -= 1
                            self.__sound = py.mixer.Sound('sound/shot.mp3')
                            self.__sound.play()
                            if self.__live == 0: self.die('sound/game_over.mp3')
                    if self.rects[GROUND].colliderect(enemy.side(TOP)):
                        self.jump(True)
                        self.score = SCORE_KILL
                        enemy.die('sound/kill_enemy.mp3')
        if fruits:
            for fruit in fruits:
                if self._rect.colliderect(fruit.rect):
                    fruit.pick_up()
                if fruit.was_pick_up:
                    self.score = SCORE_FRUIT
                    
        if tramps:
            for tramp in tramps:
                if self._rect.colliderect(tramp.rect):
                    self.die('sound/game_over.mp3')
                    
                    
