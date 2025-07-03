from graph import Graph
class maze_generator:
    def __init__(self,size):
        self.grid = Graph() 
        self.grid.add_grid(size)
    

    def add_grid(self,x,y):
        for row in range(x):
            for col in range(x):
                self.grid.add_vertex(f'{row}{col}')

    def maze_generator(self):
        pass


    def hunt_and_kill(self):

        pass