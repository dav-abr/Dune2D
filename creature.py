from cell import Cell
from wall import Wall
from settings import *
from helpers import heuristic, get_sign


class Creature(Cell):
    def __init__(self, i, j, sc, world_map):
        super().__init__(i, j, sc, world_map)
        self.previous = None
        self.open_set = [self]
        self.closed_set = []
        self.goto_path = []
        self.direction = 90

    def accept_position(self):
        self.open_set = [self]
        self.closed_set = []
        self.goto_path = []
        self.add_neighbors()

    def go_to(self, end):
        self.accept_position()

        alt_path = []

        print(self.i, self.j, self.open_set, self.closed_set, self.goto_path)
        while len(self.open_set) > 0:
            winner = 0

            for i in range(len(self.open_set)):
                if self.open_set[i].f < self.open_set[winner].f:
                    winner = i

            current = self.open_set[winner]

            if current == end:
                print('Done')
                break

            self.open_set.remove(current)

            self.closed_set.append(current)

            neighbors = current.neighbors

            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                new_path = False

                if (neighbor not in self.closed_set) and type(neighbor) != Wall and type(neighbor) != Creature:
                    tempG = current.g + neighbor.g

                    if neighbor in self.open_set:
                        if tempG < neighbor.g:
                            neighbor.g = tempG
                            new_path = True
                    else:
                        neighbor.g = tempG
                        new_path = True
                        self.open_set.append(neighbor)

                    if new_path:
                        neighbor.h = heuristic(neighbor, end)
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.previous = current
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
                self.world_map.grid[col][row].previous = None

        path.reverse()

        print(list(map(lambda item: (item.i, item.j), path)))
        self.goto_path = path

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
                self.direction = (self.direction + 5) % 360
            else:
                self.direction = (self.direction - 5) % 360

    def move(self):
        if len(self.goto_path):
            next = self.goto_path[0]
            end = self.goto_path[-1]

            if next.i < self.i and next.j > self.j and self.direction != 315:
                self.rotate(315)
                return
            if next.i < self.i and self.j == next.j and self.direction != 270:
                self.rotate(270)
                return
            if next.i < self.i and next.j < self.j and self.direction != 225:
                self.rotate(225)
                return
            if self.i == next.i and next.j < self.j and self.direction != 180:
                self.rotate(180)
                return
            if next.i > self.i and next.j < self.j and self.direction != 135:
                self.rotate(135)
                return
            if next.i > self.i and self.j == next.j and self.direction != 90:
                self.rotate(90)
                return
            if next.i > self.i and next.j > self.j and self.direction != 45:
                self.rotate(45)
                return
            if self.i == next.i and next.j > self.j and self.direction != 0:
                self.rotate(0)
                return

            if self.x == next.x and self.y == next.y:
                self.goto_path.pop(0)
                return

            if not self.x == next.x:
                self.x += -get_sign(self.x - next.x) * 2
            if not self.y == next.y:
                self.y += -get_sign(self.y - next.y) * 2

            self.world_map.grid[self.i][self.j] = Cell(self.i, self.j, self.sc, self.world_map)
            self.world_map.grid[self.i][self.j].add_neighbors()
            self.world_map.grid[next.i][next.j] = self
            self.i = next.i
            self.j = next.j

            if self.x == end.x and self.y == end.y:
                self.accept_position()

    def draw(self):
        self.move()

