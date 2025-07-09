from logic.graph import Graph
import random
def maze_generator_hunt_and_kill(size):
    maze = Graph()
    col = random.randint(1,size)
    row = random.randint(1,size)
    vertex = f'{row},{col}'
    maze.add_grid(size)
    maze.hunt_and_kill(vertex, size)
    return maze

def maze_generator_dfs(size):
    maze = Graph()
    col = random.randint(1,size)
    row = random.randint(1,size)
    vertex = f'{row},{col}'
    maze.add_grid(size)
    maze.dfs(vertex,size)
    return maze
def maze_generator_prim(size):
    maze = Graph()
    col = random.randint(1,size)
    row = random.randint(1,size)
    vertex = f'{row},{col}'
    maze.add_grid(size)
    maze.prim(vertex,size)
    return maze
def maze_generator_kurskal(size):
    maze = Graph()
    maze.kurskal(size)
    return maze
def maze_generator_wilson(size):
    maze = Graph()
    maze.add_grid(size)
    col = random.randint(1,size)
    row = random.randint(1,size)
    vertex = f'{row},{col}'
    maze.wilson(vertex, size)
    return maze
def maze_generator(size, algorithm='kurskal'):
    if algorithm == 'hunt_and_kill':
        return maze_generator_hunt_and_kill(size)
    elif algorithm == 'dfs':
        return maze_generator_dfs(size)
    elif algorithm == 'prim':
        return maze_generator_prim(size)
    elif algorithm == 'kurskal':
        return maze_generator_kurskal(size)
    elif algorithm == 'wilson':
       return maze_generator_wilson(size)
    
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")

