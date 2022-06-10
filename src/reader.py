import numpy as np
import csv


class Reader:
    def __init__(self) -> None:
        self.maze = []

        with open('data.txt', 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                self.maze.append(row)

        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze)):
                self.maze[i][j] = int(self.maze[i][j])

    def get_array(self):
        return np.array(self.maze)
