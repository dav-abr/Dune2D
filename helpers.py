import pygame as pg
import window
from math import ceil


def heuristic(a, b):
    return abs(a.i - b.i) + abs(a.j - b.j)


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


def timings(_from, to, speed, parts):
    distance = to - _from
    per_tick_distance = distance / parts
    per_tick_time = abs(per_tick_distance) / speed
    res = []
    temp_distance = _from
    temp_time = per_tick_time

    for i in range(parts):
        temp_distance += per_tick_distance
        res.append([temp_distance, temp_time])
        temp_time += per_tick_time

    return res


# print(timings(200, 100, 10, 8))
