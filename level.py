import pygame as py
from plataforma import Platform
from player import Player
from enemy import Enemy
from fruit import Fruit
from tramp import Tramp


from constantes import *


def set_pos_platform(index, displacenment):
    return (index + 1) * W_H_PLATFORM - displacenment


def adjust_pos_next_platform(pos, displacenment):
    return pos + displacenment


class Level:
    def __init__(self, screen, data) -> None:
        self.__player = None
        self.platforms = []
        self.enemies = []
        self.fruits = []
        self.__tramps = []
        self.__player = None
        self.screen = screen
        self.setup(data)
        self.__timer = 0
        self.__is_pause = False
        self.display_win =None
        self.display_lose =None
        self.create_displays()
        
    @property
    def timer(self): return int(self.__timer)
    
    @property
    def pause(self): return self.__is_pause
    
    def create_displays(self):
        self.display_win = None
        self.display_lose = None

    
    
    def lost(self): 
        return self.__player == None or self.__player.was_die
    
    def win(self):
        return not self.fruits
    
    def stars(self):
        stars = 0
        if not self.fruits:
            if not self.enemies and self.timer < 30:
                stars = 3
            elif not self.enemies or self.timer < 30:
                stars = 2
            else:
                stars = 1
        return stars

    def set_pause(self, state): self.__is_pause = state


    def create_map(self, maps, platforms):
        for row_index,row in enumerate(maps):
            for col_index,cell in enumerate(row):
                for (platform, data) in platforms.items():
                    if platform == cell:
                        pos = py.math.Vector2(col_index * W_H_PLATFORM, row_index * W_H_PLATFORM)
                        
                        if cell == WALL_PLATFORM:
                            if pos.x < int(W_WINDOWN/2):
                                pos.x = set_pos_platform(col_index, data['width'])
                            self.platforms.append(Platform(data, pos))
                            pos.y = adjust_pos_next_platform(pos.y, data['height'])
                        elif cell == BORDER_PLATFORM:
                            if pos.y < int(H_WINDOWN/2):
                                pos.y = set_pos_platform(row_index, data['height'])
                            self.platforms.append(Platform(data, pos))
                            pos.x = adjust_pos_next_platform(pos.x, data['width'])
                        
                        elif cell == CORNER_PLATFORM:
                            if pos.x < int(W_WINDOWN/2):
                                pos.x = set_pos_platform(col_index, data['width'])
                            if pos.y < int(H_WINDOWN/2):
                                pos.y = set_pos_platform(row_index, data['height'])
                        
                        self.platforms.append(Platform(data, pos))
    
    def setup(self, data):
        self.__player = Player(data['player'])
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

    def update(self, delta_ms):
        
        if not self.__is_pause:
            self.__timer += (delta_ms/1000)

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

    def draw(self):
        if self.__tramps:
            for tramp in self.__tramps:
                tramp.draw(self.screen)
        
        if self.platforms:
            for platform in self.platforms:
                platform.draw(self.screen)

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
    def player(self): return self.__player

    def run(self, delta_ms):
        self.check_collisions()
        self.update(delta_ms)
        self.draw()
