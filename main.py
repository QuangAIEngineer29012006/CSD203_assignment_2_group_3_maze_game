from graph import Graph
from mazegenerator import maze_generator
g1 = Graph()

matrix =[
    [0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
]

g2 = maze_generator()

