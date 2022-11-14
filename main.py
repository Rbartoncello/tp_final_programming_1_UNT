import json
import pygame as py
from pygame.locals import *
import sys
from constantes import *
from Gui.gui_form_in_game import FormInGame
from level import Level

flags = DOUBLEBUF

with open(FILE, 'r') as archivo:
    data = json.load(archivo)

screen = py.display.set_mode((W_WINDOWN, H_WINDOWN), flags, 16)
py.init()
clock = py.time.Clock()


level = Level(screen, data)
form_in_game = FormInGame(name="form_in_game", master_surface=screen, pos=(0, 0), size=(
    W_WINDOWN, H_FORM_IN_GAME), color_bg=None, color_border=None, value=level.player,  active=True)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    delta_ms = clock.tick(FPS)

    screen.fill('black')

    level.run(delta_ms)

    if (form_in_game.active):
        form_in_game.update(py.event.get(), level.player, level.timer)
        form_in_game.draw()

    py.display.update()
