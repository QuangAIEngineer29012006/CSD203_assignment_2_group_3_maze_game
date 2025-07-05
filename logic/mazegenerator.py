from logic.graph import Graph
import random
class maze_generator:
    def __init__(self):
        pass
        



    def maze_generator_hunt_and_kill(self,size):
        maze = Graph()
        col = random.randint(1,size)
        row = random.randint(1,size)
        vertex = f'{row},{col}'
        maze.add_grid(size)
        maze.hunt_and_kill(vertex, size)
        return maze

    def maze_generator_bfs(self,size):
        maze = Graph()
        col = random.randint(1,size)
        row = random.randint(1,size)
        vertex = f'{row},{col}'
        maze.add_grid(size)
        maze.bfs(vertex)
        return maze
