import pygame as py
from plataforma import Platform
from player import Player
from enemy import Enemy
from fruit import Fruit
from tramp import Tramp
import time
import json

from constantes import *


def set_pos_platform(index, displacenment):
    return (index + 1) * W_H_PLATFORM - displacenment


def adjust_pos_next_platform(pos, displacenment):
    return pos + displacenment


def data_level(level):
    with open(FILE.format(level), 'r') as archivo:
        data = json.load(archivo)
    return data

def data_player():
    with open(FILE_PLAYER, 'r') as archivo:
        data = json.load(archivo)
    return data


class Level:
    def __init__(self, screen, level) -> None:
        self.__player = None
        self.platforms = []
        self.enemies = []
        self.fruits = []
        self.__tramps = []
        self.screen = screen
        self.setup(data_level(level))
        self.__timer = time.time()
        self.__is_pause = False
        self.start_time = time.time()
        self.last_time = self.start_time
        self.time_in_pause = 0
        self.__level = level
        self.__score = 0

    @property
    def sound(self):
        sounds = [self.__player.sound] 
        
        for enemy in self.enemies:
            sounds.append(enemy.sound)
        
        for fruit in self.fruits:
            sounds.append(fruit.sound)
        
        return sounds
    
    @property
    def level(self):
        return self.__level

    @property
    def timer(self):
        return int(self.__timer)

    @property
    def pause(self):
        return self.__is_pause

    @property
    def lost(self):
        return self.__player is None or self.__player.was_die

    @property
    def win(self):
        return not self.fruits

    @property
    def score(self):
        return self.__score

    @property
    def stars(self):
        stars = 1
        if not self.fruits:
            if not self.enemies and self.timer < 30:
                stars = 3
            elif not self.enemies or self.timer < 30:
                stars = 2
        return stars

    def set_pause(self, state):
        if state:
            self.last_time = time.time()
            self.flag = True
        self.__is_pause = state

    def create_map(self, maps, platforms):
        for row_index, row in enumerate(maps):
            for col_index, cell in enumerate(row):
                for (platform, data) in platforms.items():
                    if platform == cell:
                        pos = py.math.Vector2(
                            col_index * W_H_PLATFORM, row_index * W_H_PLATFORM)
                        if cell == WALL_PLATFORM:
                            if pos.x < int(W_WINDOWN / 2):
                                pos.x = set_pos_platform(
                                    col_index, data['width'])
                            self.platforms.append(Platform(data, pos))
                            pos.y = adjust_pos_next_platform(
                                pos.y, data['height'])
                        elif cell == BORDER_PLATFORM:
                            if pos.y < int(H_WINDOWN / 2):
                                pos.y = set_pos_platform(
                                    row_index, data['height'])
                            self.platforms.append(Platform(data, pos))
                            pos.x = adjust_pos_next_platform(
                                pos.x, data['width'])
                        elif cell == CORNER_PLATFORM:
                            if pos.x < int(W_WINDOWN / 2):
                                pos.x = set_pos_platform(
                                    col_index, data['width'])
                            if pos.y < int(H_WINDOWN / 2):
                                pos.y = set_pos_platform(
                                    row_index, data['height'])

                        self.platforms.append(Platform(data, pos))

    def setup(self, data):
        self.__player = Player(data_player())
        self.enemies = [Enemy(enemy) for enemy in data['enemy']]

        self.create_map(data['map'], data['platforms'])

        self.fruits = [Fruit(fruit) for fruit in data['fruits']]

        self.__tramps = [Tramp(tramp) for tramp in data['tramps']]

    def check_collisions(self):
        if self.enemies:
            for enemy in self.enemies:
                enemy.check_collisions(self.platforms, self.__player)
        if self.__player is not None:
            self.__player.check_collisions(
                self.platforms, self.enemies, self.fruits, self.__tramps)

    def was_not_pause(self):
        return int(self.last_time) == int(self.start_time)

    def update(self, delta_ms):
        self.__score = self.__player.score

        
        if self.was_not_pause():
            self.__timer = (time.time() - self.start_time)
        else:
            if self.flag:
                self.time_in_pause += time.time() - self.last_time
                self.flag = False
            self.__timer = (time.time() - self.start_time) - (self.time_in_pause)
        if self.__player is not None:
            self.__player.update(delta_ms)
        if self.enemies:
            for enemy in self.enemies:
                enemy.update(delta_ms)
        if self.fruits:
            for fruit in self.fruits:
                fruit.update(delta_ms)
        if self.__tramps:
            for tramp in self.__tramps:
                tramp.update(delta_ms)

    def draw_objects_maps(self, objects):
        if objects:
            for item in objects:
                item.draw(self.screen)

    def draw(self):
        self.draw_objects_maps(self.__tramps)
        self.draw_objects_maps(self.platforms)

        if self.__player is not None:
            if not self.__player.was_die:
                self.__player.draw(self.screen)
            else:
                self.__player = None

        if self.enemies:
            for i, enemy in enumerate(self.enemies):
                if not enemy.was_die:
                    enemy.draw(self.screen)
                else:
                    self.enemies.pop(i)

        if self.fruits:
            for i, fruit in enumerate(self.fruits):
                if not fruit.was_collected:
                    fruit.draw(self.screen)
                else:
                    self.fruits.pop(i)

    @property
    def player(self):
        return self.__player

    def run(self, delta_ms):
        self.check_collisions()
        self.update(delta_ms)
        self.draw()
        
    def reset(self, level):
        self.setup(data_level(level))
        self.__timer = 0
        self.__score = 0
