import pygame as pg
from settings import *
import window


def heuristic(a, b):
    return abs(a.i - b.i) + abs(a.j - b.j)


def get_sign(num):
    return 1 if num >= 0 else -1


def load_sprite(path):
    img = pg.image.load(path)
    img = img.convert_alpha()
    return pg.transform.scale(img, (window.cell_size, window.cell_size))
    # return img


def load_building_sprite(path, width, height):
    img = pg.image.load(path)
    return pg.transform.scale(img, (window.cell_size * width, window.cell_size * height))
