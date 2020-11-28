import pygame as pg
from heapq import *
from settings import *

class Cell:
    def __init__(self, x, y, map, sc):
        self.x = x
        self.y = y
        self.map = map
        self.sc = sc

    def get_neighbours(self, x, y):
        check_neighbour = lambda x, y: True if 0 <= x < self.map.cols and 0 <= y < self.map.rows else False
        ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
        return [(self.map.grid[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in ways if check_neighbour(x + dx, y + dy)]


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

    def goTo(self, dx, dy):
        graph = {}
        for y, row in enumerate(self.map.grid):
            for x, col in enumerate(row):
                graph[(x, y)] = graph.get((x, y), []) + self.get_neighbours(x, y)

        start = (self.x, self.y)
        goal = (dx, dy)
        queue = []
        heappush(queue, (0, start))
        path_segment = goal
        path = []

        visited = self.dijkstra(start, goal, graph)
        while path_segment and path_segment in visited:
            pg.draw.circle(self.sc, pg.Color('blue'), (path_segment[0] * CELL_SIZE + CELL_SIZE // 2, path_segment[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)
            path_segment = visited[path_segment]
            path.append(path_segment)
        path.reverse()
        self.moveTo(path[1:])

    def moveTo(self, path):
        for cords in path:
            while self.x != cords[0] and self.y != cords[1]:
                self.x -= self.x - cords[0]
                self.y -= self.y - cords[1]
            print(self.x, self.y)

    def get_circle(self):
        return (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4

    def draw(self):
        pg.draw.circle(self.sc, pg.Color('red'), *self.get_circle())
