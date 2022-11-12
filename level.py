from plataforma import Platform
from player import Player
from enemy import Enemy
from fruit import Fruit

from constantes import *


class Level:
    def __init__(self, screen, data) -> None:
        self.platforms = []
        self.enemies = []
        self.fruits = []
        self.player = None
        self.screen = screen
        self.setup(data)

    def setup(self, data):
        self.player = Player(data['player'])
        self.enemies = [Enemy(data['enemy'])]

        for platform in data['platforms']:
            self.platforms.append(Platform(platform))

        for fruit in data["fruits"]:
            self.fruits.append(Fruit(fruit))

    def check_collisions(self):
        if self.enemies:
            for enemy in self.enemies:
                enemy.check_collisions(self.platforms, self.player)
        if self.player is not None: self.player.check_collisions(self.platforms, self.enemies, self.fruits)

    def update(self, delta_ms):
        if self.player is not None: self.player.update(delta_ms)
        if self.enemies:
            for enemy in self.enemies:
                enemy.update(delta_ms)
        if self.fruits:
            for fruit in self.fruits:
                fruit.update(delta_ms)

    def draw(self):

        if self.platforms:
            for platform in self.platforms:
                platform.draw(self.screen)

        if self.player is not None:
            if not self.player.was_die:
                self.player.draw(self.screen)
            else:
                self.player = None

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

    def run(self, delta_ms):
        self.check_collisions()
        self.update(delta_ms)
        self.draw()
