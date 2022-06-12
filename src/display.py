import pygame
from pygame import surfarray

class Display:
    def __init__(self, side_length, scale, maze_disp_array) -> None:
        self.SIDE_LENGTH = side_length
        self.SCALE = scale
        self.disp_maze = maze_disp_array

    def show_window(self):
        bg_color = (0, 0, 0)
        screen = pygame.display.set_mode(
            ((self.SIDE_LENGTH + 1) * self.SCALE, (self.SIDE_LENGTH + 1) * self.SCALE))

        pygame.display.set_caption('Maze')
        screen.fill(bg_color)
        pygame.display.flip()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            surfarray.blit_array(screen, self.disp_maze)
            pygame.display.flip()