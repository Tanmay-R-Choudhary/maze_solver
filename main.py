from src.generator import Generator
# from src.reader import Reader
from src.solver import MazeSolver
import numpy as np
import pygame
from pygame import surfarray

SIDE_LENGTH = 20
SCALE = int(700 / SIDE_LENGTH) # 700 OR 500

maze_generator = Generator(SIDE_LENGTH, [0, 1])
maze_generator.gen_maze()

solver_obj = MazeSolver(maze_generator.get_maze_template())
idx = solver_obj.solve()


bg_color = (0, 0, 0)
screen = pygame.display.set_mode(
    ((SIDE_LENGTH + 1) * SCALE, (SIDE_LENGTH + 1) * SCALE))

pygame.display.set_caption('Maze')
screen.fill(bg_color)
pygame.display.flip()
running = True

display_maze = solver_obj.get_disp_maze(SCALE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    surfarray.blit_array(screen, display_maze)
    pygame.display.flip()

# maze_generator.save_maze()
# print(maze_generator.get_maze_template())
# reader = Reader()
# print(reader.get_array())

# print(maze_generator.get_maze_template() == reader.get_array())
