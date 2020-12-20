from biulding import Building
from cell import Cell
from wall import Wall
from settings import *
from helpers import heuristic, get_sign
import window


class Creature(Cell):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.previous = None
        self.open_set = [self.world_map.ground[self.i][self.j]]
        self.closed_set = []
        self.goto_path = []
        self.direction = 90
        self.ready_for_update_neighbors = True
        self.hp = 0
        self.max_hp = 0

    def accept_position(self):
        self.open_set = [self.world_map.ground[self.i][self.j]]
        self.closed_set = []
        self.goto_path = []
        self.update_neighbors()

    def go_to(self, end):
        self.accept_position()

        alt_path = []

        while len(self.open_set) > 0:
            winner = 0

            for i in range(len(self.open_set)):
                if self.open_set[i].f < self.open_set[winner].f:
                    winner = i

            current = self.open_set[winner]

            if current == end:
                break

            self.open_set.remove(current)
            self.closed_set.append(current)
            neighbors = current.neighbors

            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                ground_neighbor = neighbor[0]
                new_path = False

                if (ground_neighbor not in self.closed_set) and\
                   not isinstance(neighbor[0], Wall) and\
                   not isinstance(neighbor[1], Creature) and \
                   not isinstance(neighbor[2], Building):
                    tempG = current.g + ground_neighbor.g

                    if ground_neighbor in self.open_set:
                        if tempG < ground_neighbor.g:
                            ground_neighbor.g = tempG
                            new_path = True
                    else:
                        ground_neighbor.g = tempG
                        new_path = True
                        self.open_set.append(ground_neighbor)

                    if new_path:
                        ground_neighbor.h = heuristic(ground_neighbor, end)
                        ground_neighbor.f = ground_neighbor.g + ground_neighbor.h
                        ground_neighbor.previous = current
                        alt_path.append(current)

        if len(self.open_set) == 0:
            print('No solution')
            return []

        path = []
        temp = current
        path.append(temp)

        while temp and temp.previous:
            path.append(temp)
            temp = temp.previous

        for col in range(COLS):
            for row in range(ROWS):
                self.world_map.ground[col][row].previous = None
                self.world_map.creatures[col][row].previous = None

        path.reverse()
        self.goto_path = path[:-1]

    def rotate(self, to):
        self.direction = (self.direction + 360) % 360

        if self.direction % 360 != to:
            left = (360 - self.direction) + to
            right = self.direction - to

            if self.direction < to:
                if to > 0:
                    left = to - self.direction
                    right = (360 - to) + self.direction
                else:
                    left = (360 - to) + self.direction
                    right = to - self.direction

            if left <= right:
                self.direction = (self.direction + 11.25) % 360
            else:
                self.direction = (self.direction - 11.25) % 360

    def rotate_to_next(self):
        next = self.goto_path[0]

        if next.i < self.i and next.j > self.j and self.direction != 135:
            self.rotate(135)
            return False
        elif next.i < self.i and self.j == next.j and self.direction != 90:
            self.rotate(90)
            return False
        elif next.i < self.i and next.j < self.j and self.direction != 45:
            self.rotate(45)
            return False
        elif self.i == next.i and next.j < self.j and self.direction != 0:
            self.rotate(0)
            return False
        elif next.i > self.i and next.j < self.j and self.direction != 315:
            self.rotate(315)
            return False
        elif next.i > self.i and self.j == next.j and self.direction != 270:
            self.rotate(270)
            return False
        elif next.i > self.i and next.j > self.j and self.direction != 225:
            self.rotate(225)
            return False
        elif self.i == next.i and next.j > self.j and self.direction != 180:
            self.rotate(180)
            return False
        else:
            return True

    def move(self):
        next = self.goto_path[0]
        next_creature = self.world_map.creatures[next.i][next.j]
        end = self.goto_path[-1]

        if (isinstance(next_creature, Creature) or isinstance(next, Creature)) and next_creature != self:
            if next == end:
                self.accept_position()
            else:
                self.go_to(end)
            return

        if self.i != next.i or self.j != next.j:
            new_cell = Cell(self.i, self.j, self.sc, self.world_map)
            self.world_map.creatures[self.i][self.j] = new_cell
            self.world_map.creatures[next.i][next.j] = self
            self.i = next.i
            self.j = next.j
            new_cell.update_neighbors()
            self.update_neighbors()

        if self.x == end.x and self.y == end.y:
            self.accept_position()

        if self.x == next.x and self.y == next.y and len(self.goto_path) > 0:
            self.ready_for_update_neighbors = True
            self.goto_path.pop(0)

        if not self.x == next.x:
            self.x += get_sign(next.x - self.x) * window.cell_size / 8
        if not self.y == next.y:
            self.y += get_sign(next.y - self.y) * window.cell_size / 8

    def draw(self):
        super().draw()
        if len(self.goto_path):
            if self.rotate_to_next():
                self.move()

