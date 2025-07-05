from logic.graph import Graph
from logic.mazegenerator import maze_generator
from graphic.graphicForGame import draw_maze

g1 = maze_generator()
g2 = g1.maze_generator_hunt_and_kill(20)
draw_maze(g2,20,20)

