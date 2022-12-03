import pygame as py
from pygame.locals import *
from constantes import *
from Gui.gui_form import Form
from Gui.gui_button import Button
from Gui.gui_player_ranking import PlayerRanking
import sqlite3 as sql

def readRows():
    with sql.connect("./data/ranking.db") as conexion:
        try:
            cursor = conexion.cursor()
            instruccion = f"SELECT * FROM score ORDER BY score DESC"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            conexion.commit()
            return datos
        except:
            print("Error")

class MenuRanking(Form):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active):
        super().__init__(name, master_surface, pos, size,
                         image_bg, color_bg, color_border, active)

        self.__button_exit = None
        self.create_exit_button(size[0])

        self.__players = []
        self.__datos = readRows()
        self.create_levels_buttons()

        self.__image_bg = py.image.load(PATH_BG_SELECT_LEVELS)
        self.__image_bg = py.transform.scale(
            self.__image_bg, (W_MENU-150, H_MENU-150)).convert_alpha()
        self.__rect_image_bg = self.surface.get_rect(topleft=(75, 75))

        self.__image_header = py.image.load(PATH_HEADER_RANKING)
        self.__image_header = py.transform.rotozoom(
            self.__image_header, 0, 0.4).convert_alpha()
        self.__rect_image_header = self.__image_header.get_rect(
            midtop=(W_MENU/2, -15))

    def max_view_player(self):
        max_view = 3
        if len(self.__datos) < max_view:
            max_view = len(self.__datos)
        return max_view

    def create_levels_buttons(self):
        level = 0
        for row in range(self.max_view_player()):
            for col in range(1):
                level += 1
                self.__players.append(PlayerRanking(
                    master=self,
                    pos=(125 + col * 200, 125 + row * 115),
                    size=SIZE_BUTTON_LEVEL,
                    color_bg=None, color_border=None,
                    text=''
                ))

    def create_exit_button(self, w):
        self.__button_exit = Button(
            master=self,
            pos=((w/2)+250, 90),
            size=SIZE_BUTTON_EXIT,
            color_bg=None, color_border=None,
            image_bg=PATH_BUTTON_CLOSE,
            on_click=self.__on_click_button_exit,
            on_click_param=MENU_INITIAL
        )

    def __on_click_button_exit(self, parametro):
        if DEBUG: print(parametro)
        self.set_active(parametro)

    def update(self, lista_eventos):
        self.__button_exit.update(lista_eventos)
        for i, player in enumerate(self.__players):
            player.update(lista_eventos)
            player.value = self.__datos[i]

    def draw(self):
        super().draw()
        self.surface.blit(self.__image_bg, self.__rect_image_bg)
        for button in self.__players:
            button.draw()
        self.surface.blit(self.__image_header, self.__rect_image_header)
        self.__button_exit.draw()
