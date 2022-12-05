from colores import *
import pygame as py

GROUND_LEVEL = 600
FPS = 60


DEBUG = False
TIME_TO_DIE = 2000
FLOOR = 600


TOP = 'top'
GROUND = 'ground'
RIGHT = 'right'
LEFT = 'left'
HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'


""" CHARACTERS STATES """

IDLE = 'idle'
WALK = 'walk'
JUMP = 'jump'
RUN = 'run'
FALL = 'fall'
HIT = 'hit'
DIE = 'die'


COLLECTED = 'collected'


""" SCORES """

SCORE_FRUIT = 1
SCORE_KILL = 100


""" MOUSE STATES """

M_STATE_NORMAL = 'normal'
M_STATE_HOVER = 'hover'
M_STATE_CLICK = 'click'
M_BRIGHT_HOVER = GRAY13
M_BRIGHT_CLICK = GRAY11


""" MAPS ITEMS """

WALL_PLATFORM = '3'
BORDER_PLATFORM = '4'
CORNER_PLATFORM = '5'


""" SIZES """
W_WINDOWN = 1008
H_WINDOWN = 674
W_H_RECT = 6
W_H_RECT_SENSOR = 5
H_FORM_IN_GAME = 50
W_SCORE_TIMER = len('Timer: 0000        Score: 0000')
W_H_PLATFORM = 48
SIZE_BUTTON_MENU_INITIAL = (150, 150)

SIZE_BUTTON_SEND = (150, 100)
SIZE_BUTTONS_SETTINGS = (125, 125)


SIZE_BUTTONS_PAUSE = (100, 100)
SIZE_BUTTON_EXIT = (75, 75)
SIZE_BUTTON_LEVEL = (125, 125)
W_H_BUTTON_LEVEL = 125
W_BUTTON_LEVEL_UNLOCK = 50
H_BUTTON_LEVEL_UNLOCK = 75
W_BUTTON_MENU_INITIAL = 150
H_BUTTON_MENU_INITIAL = 150
W_MENU = 800
H_MENU = 616


""" POSITIONS """

POS_MENU_INITIAL = (W_WINDOWN / 2 - W_MENU / 2, H_WINDOWN / 2 - H_MENU / 2)
POS_MENU_LEVELS = (W_WINDOWN / 2 - W_MENU / 2, H_WINDOWN / 2 - H_MENU / 2)


""" PATHS """

FILE = './data/levels/{}.json'
FILE_PLAYER = './data/player/data.json'

PATH_SOURCES = "PIXEL ADVENTURE/Recursos/"
PATH_BG_SCORE_DISPLAY = "PIXEL ADVENTURE/Recursos/gui/set_gui_01/Sand/Bars/Bar_Background01.png"
PATH_BG_LIVES_BAR = "PIXEL ADVENTURE/Recursos/gui/set_gui_01/Sand/Bars/Bar_Background01.png"
PATH_HEADER_SELECT_LEVELS = 'images/gui/jungle/level_select/header.png'
PATH_BG_SELECT_LEVELS = 'images/gui/jungle/level_select/table2.png'
PATH_BUTTON_CLOSE = 'images/gui/jungle/btn/close.png'
PATH_BUTTON_SETTINGS = 'images/gui/jungle/btn/settings.png'
PATH_BUTTON_PLAY = 'images/gui/jungle/btn/play.png'
PATH_BUTTON_RANKING = 'images/gui/jungle/menu/prize.png'
PATH_BUTTON_PAUSE = 'images/gui/jungle/btn/pause.png'
PATH_BUTTON_MENU = 'images/gui/jungle/btn/menu.png'
PATH_BUTTON_RESTART = 'images/gui/jungle/btn/restart.png'

PATH_BUTTON_MUSIC_ON = 'images/gui/jungle/btn/music.png'
PATH_BUTTON_MUSIC_OFF = 'images/gui/jungle/btn/music_off.png'

PATH_BUTTON_SOUND_ON = 'images/gui/jungle/btn/sound.png'
PATH_BUTTON_SOUND_OFF = 'images/gui/jungle/btn/sound_off.png'

PATH_BUTTON_IMAGE_BG = 'images/gui/jungle/level_select/table.png'
PATH_BUTTON_LEVELS_UNLOCK = 'images/gui/jungle/level_select/lock.png'
PATH_GAME_OVER = 'images/gui/jungle/you_lose/header.png'
PATH_HEADER_WIN = 'images/gui/jungle/you_win/header.png'
PATH_HEADER_PAUSE = 'images/gui/jungle/pause/header.png'
PATH_HEADER_RANKING = 'images/gui/jungle/rating/header.png'
PATH_HEADER_SETTINGS = 'images/gui/jungle/settings/92.png'


PATH_BUTTON_SEND = 'images/gui/jungle/rating/btn.png'
PATH_PICTURE_PLAYER = 'images/gui/jungle/rating/face.png'


PATH_BUTTON_LEVELS_NUMBER = {
    '1': 'images/gui/set_gui_01/Sand/Buttons/1.png',
    '2': 'images/gui/set_gui_01/Sand/Buttons/2.png',
    '3': 'images/gui/set_gui_01/Sand/Buttons/3.png',
    '4': 'images/gui/set_gui_01/Sand/Buttons/4.png',
    '5': 'images/gui/set_gui_01/Sand/Buttons/5.png',
    '6': 'images/gui/set_gui_01/Sand/Buttons/6.png',
    '7': 'images/gui/set_gui_01/Sand/Buttons/7.png',
    '8': 'images/gui/set_gui_01/Sand/Buttons/8.png',
    '9': 'images/gui/set_gui_01/Sand/Buttons/9.png'
}
PATH_BUTTON_LEVELS_STAR = {
    '0': 'images/gui/jungle/level_select/star_0.png',
    '1': 'images/gui/jungle/level_select/star_1.png',
    '2': 'images/gui/jungle/level_select/star_2.png',
    '3': 'images/gui/jungle/level_select/star_3.png'
}
MENU_BG = 'images/gui/jungle/level_select/bg.png'
LEVELS_BG = 'images/gui/jungle/level_select/bg.png'




MENU_INITIAL = 'menu_initial'
MENU_LEVELS = 'menu_levels'
MENU_SETTINGS = 'menu_settings'
DISPLAY_PLAY = 'display_play'
DISPLAY_GAME_OVER = 'display_game_over'
DISPLAY_WIN = 'display_win'
DISPLAY_PAUSE = 'display_pause'
MENU_RANKING = 'menu_ranking'
FORM_INPUT_NAME = 'form_input_name'


BUTTON_SETTINGS = 'button_settings'
BUTTON_STAR = 'button_star'
BUTTON_EXIT = 'button_exit'
BUTTON_RANKNG = 'button_ranking'
BUTTON_SETTINGS = 'button_settings'
BUTTON_PAUSE = 'button_pause'
BUTTON_MENU = 'button_menu'
BUTTON_RESTART = 'button_restart'
BUTTON_SEND = 'button_send'
BUTTON_MUSIC_ON = 'button_music_on'
BUTTON_MUSIC_OFF = 'button_music_off'
BUTTON_SOUND_ON = 'button_sound_on'
BUTTON_SOUND_OFF = 'button_sound_off'

py.mixer.init()
sound = py.mixer.Sound('sound/click.wav')


MAX_LEVELS_ROW = 2
MAX_LEVELS_COL = 3
