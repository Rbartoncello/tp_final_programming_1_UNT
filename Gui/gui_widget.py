import pygame as py
from pygame.locals import *
from constantes import *

class Widget:
    def __init__(self,master_form,pos,size,color_background,color_border,image_bg,text,font,font_size,font_color):
        self.master_form = master_form
        self.pos = py.math.Vector2(pos)
        self.size = (size)
        self.color_background = color_background
        self.color_border = color_border
        if image_bg != None:
            self.image_bg = py.image.load(image_bg)
            self.image_bg = py.transform.scale(self.image_bg,size).convert_alpha()
        else:
            self.image_bg = None
        self._text = text
        if(self._text != None):
            py.font.init()
            self._font_sys = py.font.SysFont(font,font_size)
            self._font_color = font_color

    def render(self):
        self.slave_surface = py.Surface(self.size, py.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect(topleft = self.pos)
        self.slave_rect_collide = py.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y

        if self.color_background:
            self.slave_surface.fill(self.color_background)
        
        if self.image_bg:
            self.slave_surface.blit(self.image_bg,(0,0))
        
        if(self._text != None):
            image_text = self._font_sys.render(self._text,True,self._font_color,self.color_background)
            self.slave_surface.blit(image_text,[
                self.slave_rect.width/2 - image_text.get_rect().width/2,
                self.slave_rect.height/2 - image_text.get_rect().height/2
            ])
            
        if self.color_border:
            py.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)

    def update(self):
        pass

    def draw(self):
        self.master_form.surface.blit(self.slave_surface,self.slave_rect)