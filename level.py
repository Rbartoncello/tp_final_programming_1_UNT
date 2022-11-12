from plataforma import Platform
from player import Player
from enemy import Enemy
from fruit import Fruit

from constantes import *


class Level():
    def __init__(self, screen, data) -> None:
        self.list_platforms = []
        self.enemies = []
        self.fruits = []
        self.player = None
        self.screen = screen
        self.setup(data)

    def setup(self, data):
        self.player = Player(data['player'])
        self.enemies = [Enemy(data['enemy'])]

        for platform in data['platforms']:
            self.list_platforms.append(Platform(platform))
        
        for fruit in data["fruits"]:
            self.fruits.append(Fruit(fruit))

    def check_collisions(self):
        if self.enemies:
            for enemy in self.enemies:
                enemy.check_collisions(self.list_platforms, self.player)
        self.player.check_collisions(self.list_platforms, self.enemies, self.fruits)
        
    def update(self, delta_ms):
        self.player.update(delta_ms)
        if self.enemies:
            for enemy in self.enemies: enemy.update(delta_ms)
        if self.fruits:
            for fruit in self.fruits: fruit.update(delta_ms)
                
    def draw(self):
        
        if self.list_platforms:
            for platform in self.list_platforms: platform.draw(self.screen)
            
        self.player.draw(self.screen)
        
        if self.enemies:
            for enemy in self.enemies:
                if not enemy.was_kill(): enemy.draw(self.screen)
                else: del enemy
                
        if self.fruits:
            for fruit in self.fruits:
                if not fruit.was_collected: fruit.draw(self.screen)
                else: del fruit

    def run(self, delta_ms):
        self.check_collisions()
        self.update(delta_ms)
        self.draw()
