from logic.graph import Graph
from logic.mazegenerator import maze_generator
from graphic.graphicForGame import draw_maze_stepwise

g1 = maze_generator()
g2 = g1.maze_generator_hunt_and_kill(30)
g3 = g1.maze_generator_dfs(100)
g4 = g1.maze_generateor_prim(100)
draw_maze_stepwise(g2,30,30)




