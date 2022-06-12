import random
import csv
# import time
import numpy as np

# 1 is PATH and 0 is WALL

_UP = np.array([-1, 0])          # 0
_LEFT = np.array([0, -1])        # 1
_DOWN = np.array([1, 0])         # 2
_RIGHT = np.array([0, 1])        # 3


class _Cell:
    def __init__(self, coordinates: list) -> None:
        self.value = 0
        self.coordinates = np.array(coordinates)
        self.wallsList = [
            np.array([-1, 0]),
            np.array([0, -1]),
            np.array([1, 0]),
            np.array([0, 1])
        ]


class Generator:
    def __init__(self, side_length: int, entry_coordinates: list) -> None:
        self.__entry_coordinates = np.array(entry_coordinates)

        self.maze_template = []

        for i in range(0, side_length):
            self.maze_template.append([])
            for j in range(0, side_length):
                self.maze_template[-1].append(_Cell([i, j]))

    def get_maze_template(self):
        array = []

        for i in self.maze_template:
            array.append([])
            for element in i:
                array[-1].append(element.value)

        array.insert(0, [0] * len(self.maze_template))

        for i in array:
            i.append(0)

        array[self.__entry_coordinates[1]][self.__entry_coordinates[0]] = 1
        array[-2][-1] = 1

        return np.array(array)
    
    def get_disp_maze(self, scale_factor):
        maze = self.get_maze_template()

        for i in range(0, len(maze)):
            for j in range(0, len(maze[i])):
                if (maze[i][j] == 1).all():
                    maze[i][j] = 255

        maze = maze.T
        maze = np.repeat(maze[:, :, np.newaxis], 3, axis=2)

        return np.kron(maze, np.ones((scale_factor, scale_factor, 1)))

    def gen_maze(self):
        curr = self.__entry_coordinates
        walls = []

        for w in self.maze_template[curr[0]][curr[1]].wallsList:
            walls.append([curr, w])

        self.maze_template[curr[0]][curr[1]].value = 1

        while walls:

            current_cell, w = walls.pop(random.randint(0, len(walls) - 1))

            next_cell = current_cell + 2 * w
            if (next_cell[0] >= 0 and next_cell[0] <= len(self.maze_template) - 1 and
                    next_cell[1] >= 0 and next_cell[1] <= len(self.maze_template) - 1 and
                    self.maze_template[next_cell[0]][next_cell[1]].value == 0):

                self.maze_template[next_cell[0]][next_cell[1]].value = 1

                if (w == _UP).all():
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[0] = None
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[2] = None
                elif (w == _LEFT).all():
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[1] = None
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[3] = None
                elif (w == _DOWN).all():
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[2] = None
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[0] = None
                elif (w == _RIGHT).all():
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[3] = None
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[1] = None
                else:
                    pass

                self.maze_template[next_cell[0] - w[0]
                                   ][next_cell[1] - w[1]].value = 1

                for wall in self.maze_template[next_cell[0]][next_cell[1]].wallsList:
                    if type(wall) != type(None):
                        walls.append([next_cell, wall])

    def save_maze(self):
        maze = self.get_maze_template()

        with open("data.txt", 'w') as f:
            csv_writer = csv.writer(
                f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in maze:
                csv_writer.writerow(row)
