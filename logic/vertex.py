class Vertex:
    def __init__(self,key):
        self.key = key
        self.connected_to = {}
    def add_neighbor(self,v2,weight):
        self.connected_to[v2] = weight
    def is_neighbor(self, other):
        return other in self.connected_to



