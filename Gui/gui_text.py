from pygame.locals import *
from Gui.gui_widget import Widget
from constantes import *

class Text(Widget):
    def __init__(self, master, pos=(0, 0), size=(200, 50), color_bg=GREEN, color_border=RED1, image_bg=None, text="Text", font="Arial", font_size=14, font_color=BLUE):
        super().__init__(master, pos, size, color_bg, color_border, image_bg, text, font, font_size, font_color)

        self.state = M_STATE_NORMAL
        self.render()
    
    def render(self):
        super().render()
        
    @property
    def value(self): return self._text

    @value.setter
    def value(self, value): self._text = '{0}'.format(value)

    def update(self, lista_eventos):
        self.render()
