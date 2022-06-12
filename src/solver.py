import numpy as np


class _TreeNode:
    def __init__(self, coords, weight) -> None:
        self.coords = np.array(coords)
        self.weight = weight
        self.visited = False

        self.dir = [
            np.array([-1, 0]),
            np.array([0, -1]),
            np.array([1, 0]),
            np.array([0, 1])
        ]


class MazeSolver:
    def __init__(self, maze_array) -> None:
        self.maze = maze_array
        self.maze_operation = self.maze.astype('object')

        self.__entry = np.array([1, 0])
        self.__exit = np.array(
            [self.maze_operation.shape[0] - 2, self.maze_operation.shape[1] - 1])

        indices = np.where(self.maze_operation == 1)
        indices = list(zip(indices[0], indices[1]))

        for idx in indices:
            self.maze_operation[idx[0], idx[1]] = _TreeNode(
                [idx[0], idx[1]], np.linalg.norm(np.array([idx[0], idx[1]]) - self.__exit))

        self.path_indices = indices

    def solve(self):
        path = []
        curr = self.maze_operation[self.__entry[0], self.__entry[1]]
        curr.visited = True
        path.append([curr, [curr.coords]])

        while path:
            path.sort(key=lambda x: x[0].weight)

            curr_node, path_list = path.pop(0)

            if (curr_node.coords == self.__exit).all() and (path_list[-1] == self.__exit).all():
                self.solved_path = path_list
                return None

            for dir in curr_node.dir:
                if tuple(curr_node.coords + dir) in self.path_indices:
                    next_node = self.maze_operation[(curr_node.coords + dir)[0], (curr_node.coords + dir)[1]]

                    if next_node.visited == False:
                        next_node.visited = True
                        path.append(
                            [next_node, path_list + [next_node.coords]]
                        )
    
    def get_disp_maze(self, scale_factor):
        disp_maze = self.maze.copy()

        for i in range(0, len(disp_maze)):
            for j in range(0, len(disp_maze[i])):
                if (disp_maze[i][j] == 1).all():
                    disp_maze[i][j] = 255

        disp_maze = np.repeat(disp_maze[:, :, np.newaxis], 3, axis=2)
        
        for i in self.solved_path:
            disp_maze[i[0], i[1], 0] = 0
            disp_maze[i[0], i[1], 1] = 255
            disp_maze[i[0], i[1], 2] = 0
        
        for i in range(0, 3):
            disp_maze[:, :, i] = disp_maze[:, :, i].T

        return np.kron(disp_maze, np.ones((scale_factor, scale_factor, 1)))
