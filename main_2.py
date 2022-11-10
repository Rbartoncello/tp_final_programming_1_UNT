import pygame as py
from pygame.locals import *
import sys
from constantes import *
from player import Player
from plataforma import Platform
import json

flags = DOUBLEBUF

screen = py.display.set_mode((W_WINDOWN, H_WINDOWN), flags, 16)
py.init()
clock = py.time.Clock()

bg = py.image.load(PATH_SOURCES+"Background/Blue.png").convert()
bg = py.transform.scale(bg, (W_WINDOWN, H_WINDOWN))

with open(FILE, 'r') as archivo:
    data = json.load(archivo)
    
list_platforms = []

for platform in data['platforms']:
    list_platforms.append(Platform(platform))
    
player = Player(data['player'])

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    
    delta_ms = clock.tick(FPS)
    screen.blit(bg, bg.get_rect())
    
    for platform in list_platforms:
        platform.draw(screen)
    player.events()
    player.update(delta_ms, list_platforms)
    player.draw(screen)

    # print(delta_ms)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    py.display.flip()

