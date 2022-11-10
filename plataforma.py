import pygame
from constantes import *


class Platform:
    def __init__(self, data):
        self.image = pygame.image.load(data['path'])
        self.image = pygame.transform.scale(
            self.image, (data['width'], data['height']))
        self.rect = self.image.get_rect(topleft=(data['x'], data['y']))
        self.rects = {
            TOP: pygame.Rect(self.rect.x, self.rect.bottom-W_H_RECT, self.rect.w, W_H_RECT),
            GROUND: pygame.Rect(self.rect.x, self.rect.top, self.rect.w, W_H_RECT),
            LEFT: pygame.Rect(self.rect.left, self.rect.top+W_H_RECT+2, W_H_RECT, self.rect.h-2*W_H_RECT-5),
            RIGHT: pygame.Rect(self.rect.right-W_H_RECT, self.rect.top +
                               W_H_RECT+2, W_H_RECT, self.rect.h-2*W_H_RECT-5)
        }

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if DEBUG:
            pygame.draw.rect(screen, GRAY, self.rect)
            pygame.draw.rect(screen, GREEN, self.rects[TOP])
            pygame.draw.rect(screen, BLUE, self.rects[GROUND])
            pygame.draw.rect(screen, YELLOW1, self.rects[LEFT])
            pygame.draw.rect(screen, BROWN, self.rects[RIGHT])

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
