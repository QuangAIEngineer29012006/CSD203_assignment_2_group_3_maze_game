import pygame
import random
class Graph:
    def __init__(self):
       self.vertices_list = {}
       self.build_steps = []


    # function cơ bản của graph 
    def add_vertex(self, key):
        if key not in self.vertices_list:
            self.vertices_list[key] = {} 

    def add_edge(self,v1, v2, weight):
        if v1 not in self.vertices_list:
            self.add_vertex(v1)
        if v2 not in self.vertices_list:
            self.add_vertex(v2)
        self.vertices_list[v1][v2] = weight
        self.vertices_list[v2][v1] = weight
    def is_neighbour(self, v1, v2):
        return v2 in self.vertices_list[v1]


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
                self.build_steps.append((current, next_vertex))
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
                        self.build_steps.append((cell, next_vertex))
                        current = next_vertex 
                        found = True
                        break
                if not found:
                    break
    def prim(self, start, size):
        visited = set()
        visited.add(start)
        # 
        frontier = []

       
        for neighbor in self.get_potential_connection(start, size):
            frontier.append((start, neighbor))

        while frontier:
            idx = random.randrange(len(frontier))
            cell, neighbor = frontier.pop(idx)

            if neighbor not in visited:
                self.add_edge(cell, neighbor, 1)
                self.build_steps.append((cell, neighbor))
                visited.add(neighbor)

                for next_neighbor in self.get_potential_connection(neighbor, size):
                    if next_neighbor not in visited:
                        frontier.append((neighbor, next_neighbor))

    def dfs(self,vertex,size, visited = None): ##recursive backtracker
        if visited == None:
            visited = set()
        visited.add(vertex)
        potential = self.get_potential_connection(vertex,size)
        random.shuffle(potential)
        for i in potential:
            if i not in visited:
                self.add_edge(vertex,i,1)
                self.build_steps.append((vertex,i))
    def A_star(self): #tam
        pass
    def kurskal(self,size): #vinh
        pass
    def wilson(self,root, size):
        self.add_grid(size)
        all_cells = [f"{i},{j}" for i in range(size) for j in range(size)]
        in_tree = set()

        # Chọn ngẫu nhiên một đỉnh làm gốc
        in_tree.add(root)
        all_cells.remove(root)

        while all_cells:
            # Chọn một đỉnh chưa thuộc cây
            walk_start = random.choice(all_cells)
            walk = [walk_start]
            visited_in_walk = {walk_start}

            current = walk_start
            while current not in in_tree:
                neighbors = self.get_potential_connection(current, size)
                next_cell = random.choice(neighbors)
                # Loại bỏ vòng lặp: nếu đã đi qua next_cell thì cắt vòng
                if next_cell in visited_in_walk:
                    idx = walk.index(next_cell)
                    walk = walk[:idx+1]
                    visited_in_walk = set(walk)
                else:
                    walk.append(next_cell)
                    visited_in_walk.add(next_cell)
                current = next_cell
            # Thêm đường đi (đã loại vòng) vào cây
            for i in range(len(walk) - 1):
                u = walk[i]
                v = walk[i + 1]
                self.add_edge(u, v, 1)
                self.build_steps.append((u, v))
                in_tree.add(u)
                if u in all_cells:
                    all_cells.remove(u)
            # Đảm bảo cell cuối cùng cũng được thêm
            if walk[-1] in all_cells:
                all_cells.remove(walk[-1])
            in_tree.add(walk[-1])


    
        
        
    