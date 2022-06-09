import numpy as np
import random


# class MazeCell:
#     def __init__(self, value: int, coordinates: list) -> None:
#         self.value = value
#         self.coordinates = np.array(coordinates)
#         self.visited = False


class Generator:
    def __init__(self, side_length: int, entry_coordinates: list) -> None:
        # define the maze and entry_coordinates
        self.maze_template = np.ones((side_length, side_length))
        self.__entry_coordinates = entry_coordinates

        # set initial walls
        self.maze_template[0] = [1] * side_length
        self.maze_template[-1] = [1] * side_length

        self.maze_template[:, 0] = 1
        self.maze_template[:, -1] = 1

        self.maze_template[self.__entry_coordinates[0],
                           self.__entry_coordinates[1]] = 0

    def get_maze_template(self):
        return self.maze_template

    def gen_maze(self):
        pass
