from graph import Graph

g1 = Graph()
size = 5
g1.add_grid(size)
g1.hunt_and_kill('0,0', size)
g1.display()
