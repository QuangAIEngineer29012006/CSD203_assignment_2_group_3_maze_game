import pygame
import random
import heapq
from collections import deque

class Graph:
    def __init__(self):
        self.vertices_list = {}
        self.build_steps = []
        self.deleted_edges = []

    def add_vertex(self, key):
        if key not in self.vertices_list:
            self.vertices_list[key] = {}

    def add_edge(self, v1, v2, weight=1):
        if v1 not in self.vertices_list:
            self.add_vertex(v1)
        if v2 not in self.vertices_list:
            self.add_vertex(v2)
        self.vertices_list[v1][v2] = weight
        self.vertices_list[v2][v1] = weight

    def is_neighbour(self, v1, v2):
        return v2 in self.vertices_list[v1]

    def add_grid(self, size):
        for row in range(size):
            for col in range(size):
                vertex = f"{row},{col}"
                self.add_vertex(vertex)
                if row > 0:
                    self.add_edge(vertex, f"{row-1},{col}", random.randint(1, 5))
                if col > 0:
                    self.add_edge(vertex, f"{row},{col-1}", random.randint(1, 5))

    def get_potential_connection(self, vertex, size):
        connections = []
        row, col = map(int, vertex.split(','))
        if row > 0:
            connections.append(f"{row-1},{col}")
        if row < size - 1:
            connections.append(f"{row+1},{col}")
        if col > 0:
            connections.append(f"{row},{col-1}")
        if col < size - 1:
            connections.append(f"{row},{col+1}")
        random.shuffle(connections)
        return connections


    def prim(self, start, size ):
        self.build_steps = []
        visited = set([start])
        frontier = []
        start_pos = tuple(map(int, start.split(',')))
        for neighbor in self.get_potential_connection(start, size):
            if neighbor in self.vertices_list and self.is_neighbour(start, neighbor):
                weight = self.vertices_list[start][neighbor]
                heapq.heappush(frontier, (weight, random.random(), start, neighbor))
        while frontier:
            weight,  _, u, v = heapq.heappop(frontier)
            if v not in visited:
                visited.add(v)
                self.build_steps.append((u, v))
                print(f"Adding edge: ({u}, {v}),  from start: ")  # Debug
                for next_neighbor in self.get_potential_connection(v, size):
                    if next_neighbor not in visited and v in self.vertices_list and next_neighbor in self.vertices_list[v]:
                        next_weight = self.vertices_list[v][next_neighbor]
                        
                        heapq.heappush(frontier, (next_weight, random.random(), v, next_neighbor))
    def kruskal(self, size):
        self.build_steps = []
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])
        def union(parent, rank, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1
        edges = []
        for r in range(size):
            for c in range(size):
                u = f"{r},{c}"
                if r + 1 < size:
                    v = f"{r+1},{c}"
                    edges.append((self.vertices_list[u][v], random.random(), u, v))
                if c + 1 < size:
                    v = f"{r},{c+1}"
                    edges.append((self.vertices_list[u][v], random.random(), u, v))
        edges.sort()
        parent = {vertex: vertex for vertex in self.vertices_list}
        rank = {vertex: 0 for vertex in self.vertices_list}
        for weight, _, u, v in edges:
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                self.build_steps.append((u, v))
                union(parent, rank, x, y)

    def dfs(self, vertex, size, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        potential_neighbors_from_grid = self.get_potential_connection(vertex, size)
        random.shuffle(potential_neighbors_from_grid)
        for neighbor in potential_neighbors_from_grid:
            if neighbor in self.vertices_list[vertex]:
                if neighbor not in visited:
                    self.build_steps.append((vertex, neighbor))
                    self.dfs(neighbor, size, visited)

    def bfs_path(self, start, goal):
        queue = deque([[start]])
        visited = set([start])
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == goal:
                return path
            for neighbor in self.vertices_list[node]:
                nkey = neighbor
                if nkey not in visited:
                    visited.add(nkey)
                    queue.append(path + [nkey])
        return []

    def dfs_path(self, start, goal):
        stack = [[start]]
        visited = set([start])
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == goal:
                return path
            for neighbor in self.vertices_list[node]:
                nkey = neighbor
                if nkey not in visited:
                    visited.add(nkey)
                    stack.append(path + [nkey])
        return []

    def dijkstra_path(self, start, goal):
        distances = {vertex: float('inf') for vertex in self.vertices_list}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices_list}
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            if current_vertex == goal:
                break
            for neighbor, weight in self.vertices_list[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        if not path or path[0] != start:
            return []
        return path

    def is_connected(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in self.vertices_list[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return len(visited) == len(self.vertices_list)

    def delete_random_edges(self, size):
        g = Graph()
        for vertex, neighbors in self.vertices_list.items():
            g.vertices_list[vertex] = neighbors.copy()
        g.build_steps = self.build_steps.copy()
        g.deleted_edges = []
        potential_edges = []
        for row in range(size):
            for col in range(size):
                vertex = f"{row},{col}"
                for neighbor in self.get_potential_connection(vertex, size):
                    if neighbor not in g.vertices_list[vertex]:
                        potential_edges.append((vertex, neighbor))
        random.shuffle(potential_edges)
        extra_edges = int(len(potential_edges) * 0.1)
        added_edges = []
        for i in range(min(extra_edges, len(potential_edges))):
            u, v = potential_edges[i]
            g.add_edge(u, v, random.randint(1, 5))
            added_edges.append((u, v))
        print(f"Added {len(added_edges)} extra edges: {added_edges[:10]}")
        return g

    def get_all_edges(self):
        edges = []
        added_edges = set()
        for vertex in self.vertices_list:
            for neighbor, weight in self.vertices_list[vertex].items():
                edge = tuple(sorted([vertex, neighbor]))
                if edge not in added_edges:
                    edges.append((vertex, neighbor, weight))
                    added_edges.add(edge)
        return edges