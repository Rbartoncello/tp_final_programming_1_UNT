import pygame as py

from plataforma import Platform
from player import Player
from enemy import Enemy
from constantes import *


class Level():
    def __init__(self, screen, data) -> None:
        self.screen = screen
        self.setup(data)

    def setup(self, data):
        self.player = Player(data['player'])
        self.enemy = Enemy(data['enemy'])
        

        self.list_platforms = []
        for platform in data['platforms']:
            self.list_platforms.append(Platform(platform))

    def horizontal_collsion(self):
        for platform in self.list_platforms:
            if platform.side(RIGHT).colliderect(self.player.side(LEFT)) and self.player.direction.x < 0:
                self.player.rect.left = platform.side(RIGHT).right
            if platform.side(LEFT).colliderect(self.player.side(RIGHT)) and self.player.direction.x > 0:
                self.player.rect.right = platform.side(LEFT).left
                
            if platform.side(RIGHT).colliderect(self.enemy.side(LEFT)) and self.enemy.direction.x < 0:
                self.enemy.orientation = RIGHT
            if platform.side(LEFT).colliderect(self.enemy.side(RIGHT)) and self.enemy.direction.x > 0:
                self.enemy.orientation = LEFT

    def vertical_collsion(self):
        # self.player.apply_gravity()
        for platform in self.list_platforms:
            # print(platform.side(GROUND).colliderect(self.player.rect))
            if platform.side(TOP).colliderect(self.player.rect):
                self.player.rect.top = platform.side(TOP).bottom
                self.player.direction.y = 0
            if platform.side(GROUND).colliderect(self.player.rect):
                self.player.rect.bottom = platform.side(GROUND).top
                self.player.direction.y = 0
            
            if platform.side(GROUND).colliderect(self.enemy.rect):
                self.enemy.rect.bottom = platform.side(GROUND).top
                self.enemy.direction.y = 0

    def run(self, delta_ms):
        for platform in self.list_platforms: platform.draw(self.screen)

        self.player.update(delta_ms)
        self.enemy.update(delta_ms)
        
        self.horizontal_collsion()
        self.vertical_collsion()
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        
