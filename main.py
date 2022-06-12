from src.generator import Generator
# from src.reader import Reader
from src.solver import MazeSolver
from src.display import Display

SIDE_LENGTH = 30 # increasing the number increases the complexity of the maze
SCALE = int(700 / SIDE_LENGTH) # 700 OR 500 (the size of the pygame window) / side length of maze gives the scale factor by which the maze needs to scaled down. window size generated is not exactly 700/500
                               # due to the casting operation

maze_generator = Generator(SIDE_LENGTH, [0, 1])
maze_generator.gen_maze()

# SAVE MAZE TO FILE OR READ MAZE FROM FILE
# maze_generator.save_maze()
# reader = Reader()  # READS THE FILE data.txt which is stored in the same directory src folder is in
# print(reader.get_array())  # to print the array

disp = Display(SIDE_LENGTH, SCALE, maze_generator.get_disp_maze(SCALE))
disp.show_window()

solver_obj = MazeSolver(maze_generator.get_maze_template())
solver_obj.solve()

disp = Display(SIDE_LENGTH, SCALE, solver_obj.get_disp_maze(SCALE))
disp.show_window()
