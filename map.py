import pygame as pg
from heapq import *
from settings import *
from cell import Cell

class Map:
    def __init__(self, width, height, cellSize, sc, grid = []):
        self.cols = width // cellSize
        self.rows = height // cellSize
        self.cellSize = cellSize
        self.sc = sc

        print(self.cols, self.rows)

        if grid:
            self.grid = grid
        else:
            self.grid = [[0 for col in range(self.cols)] for row in range(self.rows)]

    def get_circle(self, x, y):
        return (x * self.cellSize + self.cellSize // 2, y * self.cellSize + self.cellSize // 2), self.cellSize // 4

    def get_neighbours(self, x, y):
        check_neighbour = lambda x, y: True if 0 <= x < self.cols and 0 <= y < self.rows else False
        ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
        return [(self.grid[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in ways if check_neighbour(x + dx, y + dy)]


    def get_click_mouse_pos(self):
        x, y = pg.mouse.get_pos()
        grid_x, grid_y = x // self.cellSize, y // self.cellSize
        pg.draw.circle(self.sc, pg.Color('red'), * self.get_circle(grid_x, grid_y))
        click = pg.mouse.get_pressed()
        return (grid_x, grid_y) if click[0] else False


    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def dijkstra(self, start, goal, graph):
        queue = []
        heappush(queue, (0, start))
        cost_visited = {start: 0}
        visited = {start: None}

        while queue:
            cur_cost, cur_node = heappop(queue)
            if cur_node == goal:
                break

            neighbours = graph[cur_node]
            for neighbour in neighbours:
                neigh_cost, neigh_node = neighbour
                new_cost = cost_visited[cur_node] + neigh_cost

                if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                    priority = new_cost + self.heuristic(neigh_node, goal)
                    heappush(queue, (priority, neigh_node))
                    cost_visited[neigh_node] = new_cost
                    visited[neigh_node] = cur_node
        return visited

    def drawGrid(self):
        for x in range(WINDOW_WIDTH // CELL_SIZE):
            for y in range(WINDOW_HEIGHT // CELL_SIZE):
                rect = pg.Rect(x*CELL_SIZE, y*CELL_SIZE,
                                   CELL_SIZE, CELL_SIZE)
                pg.draw.rect(self.sc, pg.Color('white'), rect, 1)

    def draw(self):
        self.sc.fill(pg.Color('black'))

        self.drawGrid()
