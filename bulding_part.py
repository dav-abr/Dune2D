from cell import Cell
from wall import Wall


class BuildingPart(Cell, Wall):
    def __init__(self, i, j, world_map, parent):
        super().__init__(i, j, world_map)
        self.parent = parent
