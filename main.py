import pygame as py
from pygame.locals import *
import sys
from constantes import *
from state_game import StateGame


flags = DOUBLEBUF


screen = py.display.set_mode((W_WINDOWN, H_WINDOWN), flags, 16)
py.init()

state_game = StateGame(screen)

while True:
    list_event = py.event.get()
    for event in list_event:
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    screen.fill('black')


    state_game.run(list_event)

    py.display.update()
