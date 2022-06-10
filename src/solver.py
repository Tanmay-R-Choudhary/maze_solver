import numpy as np


class MazeSolver:
    def __init__(self, maze_array, entry, exit) -> None:
        self.maze = maze_array
        self.entry_point = entry
        self.exit_point = exit
