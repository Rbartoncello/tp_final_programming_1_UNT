import json
import pygame as py
from pygame.locals import *
import sys
from constantes import *
from Gui.gui_play import Play
from Gui.gui_menu_initial import MenuInitial
from Gui.gui_game_over import GameOver

from Gui.gui_menu_levels import MenuLevels
from level import Level

flags = DOUBLEBUF

with open(FILE, 'r') as archivo:
    data = json.load(archivo)

screen = py.display.set_mode((W_WINDOWN, H_WINDOWN), flags, 16)
py.init()
clock = py.time.Clock()


#level = Level(screen, data)
form_play = Play(
    name="form_play",
    master_surface=screen,
    pos=(0, 0),
    size=(W_WINDOWN, H_WINDOWN),
    color_bg=None, color_border=None,
    data=data,
    active=False)

menu_initial = MenuInitial(
    name=MENU_INITIAL,
    master_surface=screen,
    pos=POS_MENU_INITIAL,
    size=(W_MENU, H_MENU),
    image_bg=MENU_BG,
    color_bg=None, color_border=None,
    active=True)

menu_levels = MenuLevels(
    name=MENU_LEVELS,
    master_surface=screen,
    pos=POS_MENU_LEVELS,
    size=(W_MENU, H_MENU),
    image_bg=MENU_BG,
    color_bg=None, color_border=None,
    active=False)

menu_game_over = GameOver(
    name='game_over',
    master_surface=screen,
    pos=POS_MENU_INITIAL,
    size=(W_MENU, H_MENU),
    image_bg='images/gui/jungle/you_lose/header.png',
    color_bg=None, color_border=None,
    active=False)

guis = [menu_initial, menu_levels, form_play, menu_game_over]

while True:
    list_event = py.event.get()
    for event in list_event:
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    delta_ms = clock.tick(FPS)

    screen.fill('black')

    #level.run(delta_ms)

    for gui in guis:
        if gui.active:
            gui.update(list_event)
            gui.draw()

    py.display.update()
