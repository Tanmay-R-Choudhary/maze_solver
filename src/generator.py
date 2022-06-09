import numpy as np
import enum


class CellMarker(enum.Enum):
    WALL = 1
    PATH = 0


class Dir(enum.Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


class MazeCell:
    def __init__(self, value: int, coordinates: list) -> None:
        self.value = value
        self.coordinates = coordinates

        self.wallsList = [None] * 4


class Generator:
    def __init__(self, side_length: int, entry_coordinates: list) -> None:
        # define the maze and entry_coordinates
        self.maze_template = np.array(
            [MazeCell(CellMarker.WALL, [0, 0])] * side_length * side_length)
        self.__entry_coordinates = entry_coordinates

        self.maze_template = self.maze_template.reshape(
            (side_length, side_length))

        for i in range(0, self.maze_template.shape[0]):
            for j in range(0, self.maze_template.shape[1]):
                self.maze_template[i, j].value = 1
                self.maze_template[i, j].coordinates = [i, j]

                if i == 0:
                    if j == 0:
                        self.maze_template[i, j].wallsList[Dir.DOWN] = [
                            i + 1, j]
                        self.maze_template[i, j].wallsList[Dir.RIGHT] = [
                            i, j + 1]
                    elif j == side_length - 1:
                        self.maze_template[i, j].wallsList[Dir.DOWN] = [
                            i + 1, j]
                        self.maze_template[i, j].wallsList[Dir.LEFT] = [
                            i, j - 1]
                    else:
                        self.maze_template[i, j].wallsList[Dir.LEFT] = [
                            i, j - 1]
                        self.maze_template[i, j].wallsList[Dir.DOWN] = [
                            i + 1, j]
                        self.maze_template[i, j].wallsList[Dir.RIGHT] = [
                            i, j + 1]
                if i == side_length - 1:
                    if j == 0:
                        self.maze_template[i, j].wallsList[Dir.UP] = [i - 1, j]
                        self.maze_template[i, j].wallsList[Dir.RIGHT] = [
                            i, j + 1]
                    elif j == side_length - 1:
                        self.maze_template[i, j].wallsList[Dir.UP] = [i - 1, j]
                        self.maze_template[i, j].wallsList[Dir.LEFT] = [
                            i, j - 1]
                    else:
                        self.maze_template[i, j].wallsList[Dir.LEFT] = [
                            i, j - 1]
                        self.maze_template[i, j].wallsList[Dir.UP] = [i - 1, j]
                        self.maze_template[i, j].wallsList[Dir.RIGHT] = [
                            i, j + 1]
                else:
                    if j == 0:
                        self.maze_template[i, j].wallsList[Dir.UP] = [i - 1, j]
                        self.maze_template[i, j].wallsList[Dir.DOWN] = [
                            i + 1, j]
                        self.maze_template[i, j].wallsList[Dir.RIGHT] = [
                            i, j + 1]
                    elif j == side_length - 1:
                        self.maze_template[i, j].wallsList[Dir.UP] = [i - 1, j]
                        self.maze_template[i, j].wallsList[Dir.LEFT] = [
                            i, j - 1]
                        self.maze_template[i, j].wallsList[Dir.DOWN] = [
                            i + 1, j]
                    else:
                        self.maze_template[i, j].wallsList[Dir.UP] = [i - 1, j]
                        self.maze_template[i, j].wallsList[Dir.LEFT] = [
                            i, j - 1]
                        self.maze_template[i, j].wallsList[Dir.DOWN] = [
                            i + 1, j]
                        self.maze_template[i, j].wallsList[Dir.RIGHT] = [
                            i, j + 1]

        self.maze_template[self.__entry_coordinates[0],
                           self.__entry_coordinates[1]].value = 0

    def get_maze_template(self):
        return self.maze_template

    def gen_maze(self):
        curr = self.__entry_coordinates
        walls = []

        for w in self.maze_template[curr[0], curr[1]].wallsList:
            walls.append(w)
