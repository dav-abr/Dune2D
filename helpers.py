import pygame as pg
import window
from math import ceil


def heuristic(a, b):
    return abs(a.i - b.i) + abs(a.j - b.j)


def heuristic_xy(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def get_sign(num):
    return 1 if num >= 0 else -1


def load_sprite(path, scale=window.cell_size):
    img = pg.image.load(path)
    img = img.convert_alpha()
    return pg.transform.scale(img, (ceil(scale), ceil(scale)))
    # return img


def load_building_sprite(path, width, height):
    img = pg.image.load(path)
    return pg.transform.scale(img, (window.cell_size * width, window.cell_size * height))


def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    valueScaled = float(value - leftMin) / float(leftSpan)

    return round(rightMin + (valueScaled * rightSpan))


def get_cell(x, y):
    return int(x / window.cell_size), int(y / window.cell_size)
