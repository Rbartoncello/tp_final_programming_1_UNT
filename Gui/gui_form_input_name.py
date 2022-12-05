import pygame as py
from pygame.locals import *
import sys
from constantes import *
from Gui.gui_form import Form
from Gui.gui_button import Button
from Gui.gui_textbox import TextBox
from Gui.gui_text import Text
import sqlite3 as sql

def insertRow(name, score):
    with sql.connect("./data/ranking.db") as conexion:
        try:
            conexion.execute("insert into score(name,score) values (?,?)", (name, score))
            conexion.commit()
        except:
            print("Error")

class FormInputName(Form):
    def __init__(self, name, master_surface, pos, size, image_bg, color_bg, color_border, active):
        super().__init__(name, master_surface, pos, size,
                         image_bg, color_bg, color_border, active)

        self.__image_bg = py.image.load(PATH_BG_SELECT_LEVELS)
        self.__image_bg = py.transform.scale(self.__image_bg, (W_MENU-150, H_MENU-150)).convert_alpha()
        self.__rect_image_bg = self.surface.get_rect(topleft=(75, 75))
        
        self.__button_send = self.create_button(
            ((size[0] / 2) + 125, (size[1] / 2)), SIZE_BUTTON_SEND, PATH_BUTTON_SEND, self.__on_click_button_send, BUTTON_SEND)

        self.input_text = TextBox(
            master=self,
            pos=(200, (size[1] / 2)),
            size=(300, 100),
            color_bg=None,
            color_border=None,
            image_bg=PATH_BUTTON_IMAGE_BG,
            text="",
            font="Verdana",
            font_size=30,
            font_color=BLACK
        )

        self.msj_input_text = Text(
            master=self,
            pos=((size[0] / 2 - 250), 120),
            size=(475, 100),
            color_bg=None,
            color_border=None,
            image_bg=PATH_BG_SELECT_LEVELS,
            text='Ingrese su nombre',
            font="Verdana",
            font_size=50,
            font_color=BLACK
        )

        self.__lista_widget = [self.__button_send, self.input_text, self.msj_input_text]
        
        self.__score = 0
        
    @property
    def score(self): 
        return self.__score
    
    @score.setter
    def score(self, score): 
        self.__score = score

    def create_button(self, pos, size, path, on_click, on_click_param):
        return Button(
            master=self,
            pos=pos,
            size=size,
            color_bg=None, color_border=None,
            image_bg=path,
            on_click=on_click,
            on_click_param=on_click_param
        )

    def __on_click_button_send(self, parametro):
        if DEBUG:
            print(parametro, self.input_text.text)
        if self.input_text.text:
            insertRow(self.input_text.text, self.__score)
            py.quit()
            sys.exit()

    def update(self, lista_eventos):
        for aux_widget in self.__lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.surface.blit(self.__image_bg, self.__rect_image_bg)
        for aux_widget in self.__lista_widget:
            aux_widget.draw()
