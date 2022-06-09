from src.generator import Generator

maze_generator = Generator(10, [0, 1])
print(maze_generator.get_maze_template())
print("\n")
maze_generator.gen_maze()
print(maze_generator.get_maze_template())
