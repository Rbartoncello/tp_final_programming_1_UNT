import json 
import pygame as py
from pygame.locals import *
import sys
from constantes import *
from player import Player
from level import Level

flags = DOUBLEBUF

with open(FILE, 'r') as archivo:
    data = json.load(archivo)

screen = py.display.set_mode((W_WINDOWN, H_WINDOWN), flags, 16)
py.init()
clock = py.time.Clock()

level = Level(screen, data)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    delta_ms = clock.tick(FPS)
    
    screen.fill('black')
    level.run(delta_ms)

    py.display.update()
