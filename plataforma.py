import pygame
from constantes import *
from auxiliar import Auxiliar


class Platform:
    def __init__(self, data, pos):
        self.image = pygame.image.load(data['path'])
        self.image = pygame.transform.scale(
            self.image, (data['width'], data['height']))
        self.rect = self.image.get_rect(topleft=(pos))
        self.rects = {
            TOP: pygame.Rect(self.rect.x + W_H_RECT, self.rect.bottom - W_H_RECT, self.rect.w - 2 * W_H_RECT, W_H_RECT),
            GROUND: pygame.Rect(self.rect.x + W_H_RECT, self.rect.top, self.rect.w - 2 * W_H_RECT, W_H_RECT),
            LEFT: pygame.Rect(self.rect.left, self.rect.top + W_H_RECT + 2, W_H_RECT, self.rect.h - 2 * W_H_RECT - 5),
            RIGHT: pygame.Rect(self.rect.right - W_H_RECT, self.rect.top + W_H_RECT + 2, W_H_RECT,
                               self.rect.h - 2 * W_H_RECT - 5)
        }

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        Auxiliar.debuggerMod(screen=screen, color_main=GRAY, color_top=GREEN, color_bottom=BLUE, color_left=YELLOW1,
                             color_right=BROWN, rect_main=self.rect, rects=self.rects)

    @property
    def platform(self):
        return self.rect

    def top(self):
        return self.rect_top_collition

    def ground(self):
        return self.rect_ground_collition

    def side(self, side):
        return self.rects[side]
    # @property
    # def type(self):
    #    return self.type
