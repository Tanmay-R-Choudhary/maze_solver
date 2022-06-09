import random
import time
from tkinter import LEFT
import numpy as np

# 0 is PATH and 1 is WALL

UP = np.array([-1, 0])          # 0
LEFT = np.array([0, -1])        # 1
DOWN = np.array([1, 0])         # 2
RIGHT = np.array([0, 1])        # 3


class Cell:
    def __init__(self, coordinates: list) -> None:
        self.value = 1
        self.coordinates = np.array(coordinates)
        self.wallsList = [
            np.array([-1, 0]),
            np.array([0, -1]),
            np.array([1, 0]),
            np.array([0, 1])
        ]


class Generator:
    def __init__(self, side_length: int, entry_coordinates: list) -> None:
        # define the maze and entry_coordinates
        self.__entry_coordinates = np.array(entry_coordinates)

        self.maze_template = []

        for i in range(0, side_length - 1):
            self.maze_template.append([])
            for j in range(0, side_length - 1):
                self.maze_template[-1].append(Cell([i, j]))

    def get_maze_template(self):
        return self.maze_template

    def gen_maze(self):
        curr = self.__entry_coordinates
        walls = []

        for w in self.maze_template[curr[0]][curr[1]].wallsList:
            walls.append([curr, w])

        self.maze_template[curr[0]][curr[1]].value = 0

        while walls:
            for i in self.maze_template:
                print([a.value for a in i])

            print("\n")
            time.sleep(0.25)

            current_cell, w = walls.pop(
                random.randint(0, len(walls) - 1))
            next_cell = current_cell + w
            if (next_cell[0] >= 0 and next_cell[0] <= len(self.maze_template) - 1 and
                    next_cell[1] >= 0 and next_cell[1] <= len(self.maze_template) - 1 and
                    self.maze_template[next_cell[0]][next_cell[1]].value == 1):

                self.maze_template[next_cell[0]][next_cell[1]].value = 0

                if (w == UP).all():
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[0] = None
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[2] = None
                if (w == LEFT).all():
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[1] = None
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[3] = None
                if (w == DOWN).all():
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[2] = None
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[0] = None
                if (w == RIGHT).all():
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[3] = None
                    self.maze_template[next_cell[0]
                                       ][next_cell[1]].wallsList[1] = None

                for wall in self.maze_template[next_cell[0]][next_cell[1]].wallsList:
                    if type(wall) != type(None):
                        walls.append([next_cell, wall])
