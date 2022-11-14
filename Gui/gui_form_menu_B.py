import pygame
from pygame.locals import *
from Gui.gui_form import Form
from Gui.gui_button import Button
from constantes import *


class FormMenuB(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w,
                         h, color_background, color_border, active)

        self.boton1 = Button(master=self, x=0, y=150, w=200, h=50, color_background=GREEN2, color_border=YELLOW2,
                             on_click=self.on_click_boton1, on_click_param="form_menu_A", text="ABRIR A", font="Verdana", font_size=30, font_color=BLACK)
        self.boton2 = Button(master=self, x=250, y=150, w=200, h=50, color_background=BLUE2, color_border=RED1,
                             on_click=self.on_click_boton1, on_click_param="form_menu_A", text="MENU 2", font="Verdana", font_size=30, font_color=BLACK)
        self.lista_widget = [self.boton1, self.boton2]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_boton in self.lista_widget:
            aux_boton.draw()
