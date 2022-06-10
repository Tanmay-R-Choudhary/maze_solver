from src.generator import Generator
from src.reader import Reader
import numpy as np
import pygame
from pygame import surfarray

SIDE_LENGTH = 10
SCALE = int(700 / SIDE_LENGTH)

maze_generator = Generator(SIDE_LENGTH, [0, 1])
maze_generator.gen_maze()


def convert_to_disp_image(maze_array, scale_factor):

    for i in range(0, len(maze_array)):
        for j in range(0, len(maze_array[i])):
            if maze_array[i][j] == 1:
                maze_array[i][j] = 255

    maze_array = maze_array.T
    maze_array = np.repeat(maze_array[:, :, np.newaxis], 3, axis=2)
    return np.kron(maze_array, np.ones((scale_factor, scale_factor, 1)))


bg_color = (0, 0, 0)
screen = pygame.display.set_mode(
    ((SIDE_LENGTH + 1) * SCALE, (SIDE_LENGTH + 1) * SCALE))

pygame.display.set_caption('Maze')
screen.fill(bg_color)
pygame.display.flip()
running = True

display_maze = convert_to_disp_image(maze_generator.get_maze_template(), SCALE)

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
