import math


class _TreeNode:
    def __init__(self, coords, weight) -> None:
        self.row_num = coords[0]
        self.col_num = coords[1]
        self.weight = weight


class MazeSolver:
    def __init__(self, maze_array) -> None:
        self.maze = maze_array

        self.__entry = [1, 0]
        self.__exit = [self.maze.shape[0] - 1, self.maze.shape[1]]

        self.node_list = []

        for r in range(self.maze.shape[0]):
            for c in range(self.maze.shape[1]):
                if self.maze[r][c] == 0:
                    self.node_list.append(
                        _TreeNode(
                            [r, c],
                            math.sqrt(
                                math.pow(
                                    r - self.__exit[0], 2) + math.pow(c - self.__exit[1], 2)
                            )
                        )
                    )

    def solve(self):
        pass

    def get_maze(self):
        return self.maze
