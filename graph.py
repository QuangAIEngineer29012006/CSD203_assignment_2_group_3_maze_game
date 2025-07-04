from vertex import Vertex
import random
from queue_home_made import Queue
class Graph:
    def __init__(self):
       self.vertices_list = {}

    # function cơ bản của graph 
    def add_vertex(self, key):
        new_vertex = Vertex(key) 
        if key not in self.vertices_list:
            self.vertices_list[key] = new_vertex 

    def add_edge(self,v1, v2, weight):
        if v1 not in self.vertices_list:
            self.add_vertex(v1)
        if v2 not in self.vertices_list:
            self.add_vertex(v2)
        self.vertices_list[v1].add_neighbor(self.vertices_list[v2], weight)

    def display(self):
        for i in self.vertices_list:
            print(f'{i}: ',end ="")
            for neighbor in self.vertices_list[i].connected_to:
                print(neighbor.key, end = ' ')
            print()
    def bfs(self, start):
        visted = set()
        q = Queue()
        q.enqueue(start)
        visted.add(start)
        while q.size > 0:
            current = q.dequeue()
            print(f"{current.key} ", end = '')
            for neighbor in current.connected_to:
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor.key)


    ## function mở rộng thêm, đọc ma trận ( hứng lên cho vào ) 
    def int_to_char(self,i):
        return chr(i % 26 +65)
    def char_to_int(self,c):
        return ord(c.upper()) -65

    def read_matrix(self, adj_matrix):
        for i in range(len(adj_matrix)):
            u = self.int_to_char(i)
            new_vertice = Vertex(self.int_to_char(i))
            self.vertices_list[u] = new_vertice
            for j in range(len(adj_matrix[i])): 
                v = self.int_to_char(j)
                if adj_matrix[i][j] != 0:
                    self.add_edge(u,v, adj_matrix[i][j])
    
    
    # bắt đầu function mở rộng 
    # tạo grid để bắt đầu tạo ma trận
    def add_grid(self,x,):
        for row in range(x):
            for col in range(x):
                self.add_vertex(f'{row},{col}')
    
    # trả về các kết nôis tiềm năng nhât
    def  get_potential_connection(self,vertex,size):
        potential_connection_list = []
        row, col = map(int, vertex.split(","))
        if row - 1 >= 0: 
            potential_connection_list.append(f"{row-1},{col}")

        if row + 1 < size: 
            potential_connection_list.append(f"{row+1},{col}")
                
        if col - 1 >= 0: 
            potential_connection_list.append(f"{row},{col-1}")

        if col + 1 < size: 
            potential_connection_list.append(f"{row},{col+1}")
       
        return potential_connection_list

    def hunt_and_kill(self, vertex,size):
        visited = set()
        current = vertex
        visited.add(current)
        while True:
            neighbours = [neighbour for neighbour in self.get_potential_connection(current,size) if neighbour not in visited]
            if neighbours:
                next_vertex = random.choice(neighbours)
                self.add_edge(current, next_vertex,1)
                visited.add(next_vertex)
                current =next_vertex
            else:
                found = False 
                for cell in visited:
                    neighbours =[n for n in self.get_potential_connection(cell,size) if n not in visited]
                    if neighbours :
                        next_vertex = random.choice(neighbours)
                        self.add_edge(cell, next_vertex,1)
                        visited.add(next_vertex)
                        current = next_vertex 
                        found = True
                        break
                if not found:
                    break
        





       









        




    



