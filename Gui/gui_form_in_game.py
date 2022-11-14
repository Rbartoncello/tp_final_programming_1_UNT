from pygame.locals import *
from constantes import *
from Gui.gui_form import Form
from Gui.gui_displaybox import DisplayBox
from Gui.gui_lives_bar import LivesBar
from Gui.gui_button import Button


class FormInGame(Form):
    def __init__(self, name, master_surface, pos, size, color_bg, color_border, value, active):
        super().__init__(name, master_surface, pos, size, color_bg, color_border, active)

        self.pause_button = Button(master=self,pos=(0, 0), size=(size[1], size[1]), color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/gui/jungle/btn/pause.png",on_click=self.__on_click,on_click_param="form_menu_B",text=None,font="Verdana",font_size=30,font_color=WHITE)
        
        self.score_display = DisplayBox(master=self, pos=(0, 0), size=(
            W_SCORE_TIMER*10, size[1]), color_bg=None, color_border=None, image_bg=PATH_BG_SCORE_DISPLAY, text="Time: 0   Score: 0", font="Verdana", font_size=30, font_color=BLACK)

        self.lives_bar = LivesBar(master=self, pos=(W_WINDOWN-120, 0), size=(
            120, size[1]), color_bg=None, color_border=None, image_bg=PATH_BG_LIVES_BAR, image_progress="pngwing.com.png", value=value.live, value_max=value.live)

        self.lista_widget = [self.score_display, self.lives_bar, self.pause_button]

    def __on_click(self, parametro):
        print('click')
        print(self.timer)
    
    def update(self, lista_eventos, player, timer):
        self.timer = timer
        self.lives_bar.value = player.live
        self.score_display.value = (timer, player.score)

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:
            aux_widget.draw()
