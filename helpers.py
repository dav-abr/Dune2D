import pygame as pg
from settings import *


def heuristic(a, b):
    return abs(a.i - b.i) + abs(a.j - b.j)


def get_sign(num):
    return 1 if num >= 0 else -1


def load_image(path):
    img = pg.image.load(path)
    return pg.transform.scale(img, (CELL_SIZE, CELL_SIZE))
