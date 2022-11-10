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

    def check_collisions(self):
        self.enemy.check_collisions(self.list_platforms)
        self.player.check_collisions(self.list_platforms)

    def run(self, delta_ms):
        for platform in self.list_platforms:
            platform.draw(self.screen)

        self.player.update(delta_ms)
        self.enemy.update(delta_ms)

        self.check_collisions()

        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
