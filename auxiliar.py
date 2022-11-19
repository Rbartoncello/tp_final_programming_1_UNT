import pygame as py
from constantes import *


class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, cols, rows, flip=False, step=1, scale=1):
        lista = []
        surface_imagen = py.image.load(path)
        frame_widht = int(surface_imagen.get_width() / cols)
        frame_heigth_scaled = int(surface_imagen.get_height() / rows)
        frame_widht_scaled = int(frame_widht * scale)
        frame_heigth_scaled_scaled = int(frame_heigth_scaled * scale)
        x = 0

        for row in range(rows):
            for col in range(0, cols, step):
                x = col * frame_widht
                y = row * frame_heigth_scaled
                surface_frame = surface_imagen.subsurface(
                    x, y, frame_widht, frame_heigth_scaled)
                if scale != 1:
                    surface_frame = py.transform.scale(
                        surface_frame, (frame_widht_scaled, frame_heigth_scaled_scaled)).convert_alpha()
                if flip:
                    surface_frame = py.transform.flip(
                        surface_frame, True, False).convert_alpha()
                lista.append(surface_frame)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format, quantity, flip=False, step=1, scale=1, w=0, h=0, repeat_frame=1):
        lista = []
        for i in range(1, quantity + 1):
            path = path_format.format(i)
            surface_frame = py.image.load(path)
            frame_width_scaled = int(
                surface_frame.get_rect().w * scale)
            frame_height_scaled = int(surface_frame.get_rect().h * scale)
            if scale == 1 and w != 0 and h != 0:
                surface_frame = py.transform.scale(
                    surface_frame, (w, h)).convert_alpha()
            if scale != 1:
                surface_frame = py.transform.scale(
                    surface_frame, (frame_width_scaled, frame_height_scaled)).convert_alpha()
            if flip:
                surface_frame = py.transform.flip(
                    surface_frame, True, False).convert_alpha()

            for i in range(repeat_frame):
                lista.append(surface_frame)
        return lista

    @staticmethod
    def debuggerMod(screen, color_main, color_top, color_bottom, color_left, color_right, rect_main, rects):
        if DEBUG:
            py.draw.rect(screen, color_main, rect_main)
            py.draw.rect(screen, color_top, rects[TOP])
            py.draw.rect(screen, color_bottom, rects[GROUND])
            py.draw.rect(screen, color_left, rects[LEFT])
            py.draw.rect(screen, color_right, rects[RIGHT])
    
    @staticmethod
    def create_side_animation(data, path, side):
        return Auxiliar.getSurfaceFromSpriteSheet(path, data['cols'], data['rows'], data[side])

    @staticmethod
    def create_sides_animation(data, path):
        return {
            RIGHT: Auxiliar.create_side_animation(data, path, RIGHT),
            LEFT: Auxiliar.create_side_animation(data, path, LEFT)
        }
