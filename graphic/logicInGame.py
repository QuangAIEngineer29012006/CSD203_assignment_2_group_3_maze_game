import pygame
from graphic.entity import Player, Ghost
from graphic.draw import draw_maze, draw_player, draw_ghost, draw_exit
import random


# Handles player input and updates player position
def handle_player_input(player, graph, size):
    keys = pygame.key.get_pressed()
    next_x, next_y = player.pos_x, player.pos_y
    if keys[pygame.K_UP] and player.pos_x > 0:
        next_x -= 1
    elif keys[pygame.K_DOWN] and player.pos_x < size - 1:
        next_x += 1
    elif keys[pygame.K_LEFT] and player.pos_y > 0:
        next_y -= 1
    elif keys[pygame.K_RIGHT] and player.pos_y < size - 1:
        next_y += 1
    cell_cur = f"{player.pos_x},{player.pos_y}"
    cell_next = f"{next_x},{next_y}"
    if cell_next in graph.vertices_list and graph.is_neighbour(cell_cur, cell_next):
        player.pos_x, player.pos_y = next_x, next_y

def bfs_path(graph, start, goal):
    from collections import deque
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.vertices_list[node]:
            nkey = neighbor
            if nkey not in visited:
                visited.add(nkey)
                queue.append(path + [nkey])
    return []
#distance to calculate manhattan distance between two points
def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Handles ghost movement logic
def update_ghost(ghost, player, graph, size):
    ghost_cell = f"{ghost.pos_x},{ghost.pos_y}"
    player_cell = f"{player.pos_x},{player.pos_y}"
    dist = manhattan([ghost.pos_x, ghost.pos_y], [player.pos_x, player.pos_y])
    if dist > 10:
        # Move randomly to a neighbor
        neighbors = list(graph.vertices_list[ghost_cell])
        if neighbors:
            next_cell = random.choice(neighbors)
            gx, gy = map(int, next_cell.split(','))
            ghost.pos_x, ghost.pos_y = gx, gy
    else:
        path = bfs_path(graph, ghost_cell, player_cell)
        if len(path) > 1:
            gx, gy = map(int, path[1].split(','))
            ghost.pos_x, ghost.pos_y = gx, gy

def get_random_safe_places(size, count=5):
    safe_places = set()
    while len(safe_places) < count:
        y = random.randint(0, size-1)
        x = random.randint(0, size-1)
        safe_places.add((y, x))
    return list(safe_places)