import pygame as py
from pygame.locals import *
import sys
from constantes import *
from Gui.gui_play import Play
from Gui.gui_menu_initial import MenuInitial
from Gui.gui_game_over import GameOver

from Gui.gui_menu_levels import MenuLevels

flags = DOUBLEBUF


screen = py.display.set_mode((W_WINDOWN, H_WINDOWN), flags, 16)
py.init()

menu_initial = MenuInitial(
    name=MENU_INITIAL,
    master_surface=screen,
    pos=POS_MENU_INITIAL,
    size=(W_MENU, H_MENU),
    image_bg=MENU_BG,
    color_bg=None, color_border=None,
    active=True)

levels = MenuLevels(
    name=MENU_LEVELS,
    master_surface=screen,
    pos=POS_MENU_LEVELS,
    size=(W_MENU, H_MENU),
    image_bg=MENU_BG,
    color_bg=None, color_border=None,
    active=False)

play = Play(
    name=DISPLAY_PLAY,
    master_surface=screen,
    pos=(0, 0),
    size=(W_WINDOWN, H_WINDOWN),
    color_bg=None, color_border=None,
    last_level = levels.last_level_unlock,
    active=False)

game_over = GameOver(
    name=DISPLAY_GAME_OVER,
    master_surface=screen,
    image_bg=PATH_GAME_OVER,
    color_bg=None, color_border=None,
    active=False
    )

guis = [menu_initial, levels, play, game_over]

while True:
    list_event = py.event.get()
    for event in list_event:
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    screen.fill('black')


    for gui in guis:
        if gui.active:
            gui.update(list_event)
            gui.draw()

    py.display.update()
