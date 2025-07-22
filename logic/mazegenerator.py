from logic.graph import Graph
import random
from collections import deque

def maze_generator_dfs(size):
    maze = Graph()
    maze.add_grid(size)
    col = random.randint(0, size-1)
    row = random.randint(0, size-1)
    vertex = f'{row},{col}'
    maze.dfs(vertex, size)
    final_edges = maze.build_steps
    maze.vertices_list = {}
    for u, v in final_edges:
        maze.add_edge(u, v, 1)  # Use fixed weight 1
    maze = maze.delete_random_edges(size)
    return maze

def maze_generator_prim(size):
    maze = Graph()
    maze.add_grid(size)
    col = random.randint(0, size-1)
    row = random.randint(0, size-1)
    vertex = f'{row},{col}'
    maze.prim(vertex, size)
    final_edges = maze.build_steps
    maze.vertices_list = {}
    for u, v in final_edges:
        maze.add_edge(u, v, 1)  # Use fixed weight 1
    maze = maze.delete_random_edges(size)
    return maze

def maze_generator_kruskal(size):
    maze = Graph()
    maze.add_grid(size)
    maze.kruskal(size)
    final_edges = maze.build_steps
    maze.vertices_list = {}
    for u, v in final_edges:
        maze.add_edge(u, v, 1)  # Use fixed weight 1
    maze = maze.delete_random_edges(size)
    return maze

def maze_generator(size, algorithm='kruskal'):
    if algorithm == 'dfs':
        maze = maze_generator_dfs(size)
    elif algorithm == 'prim':
        maze = maze_generator_prim(size)
    elif algorithm == 'kruskal':
        maze = maze_generator_kruskal(size)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    print(f"Generated maze with {len(maze.build_steps)} edges, deleted {len(maze.deleted_edges)} edges")
    return maze