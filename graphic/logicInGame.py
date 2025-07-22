import pygame
from graphic.entity import Player, Ghost
from graphic.draw import draw_maze, draw_player, draw_ghost, draw_exit
import random
from logic.graph import Graph

def handle_player_input(player, graph, size, event):
    next_x, next_y = player.pos_x, player.pos_y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and player.pos_x > 0:
            next_x -= 1
        elif event.key == pygame.K_DOWN and player.pos_x < size - 1:
            next_x += 1
        elif event.key == pygame.K_LEFT and player.pos_y > 0:
            next_y -= 1
        elif event.key == pygame.K_RIGHT and player.pos_y < size - 1:
            next_y += 1
        else:
            return
    cell_cur = f"{player.pos_x},{player.pos_y}"
    cell_next = f"{next_x},{next_y}"
    if (next_x, next_y) != (player.pos_x, player.pos_y) and \
       cell_next in graph.vertices_list and \
       graph.is_neighbour(cell_cur, cell_next):
        player.pos_x, player.pos_y = next_x, next_y

def update_ghost(ghost, player, graph, size, safe_places=None, target_dict=None, ghost_index=None):
    def get_random_place(size, current_pos):
        # Select a random target at least 6 Manhattan distance away
        min_distance = 6
        while True:
            rand_x = random.randint(0, size-1)
            rand_y = random.randint(0, size-1)
            target = f'{rand_x},{rand_y}'
            if target != current_pos:
                dist = graph.manhattan([int(current_pos.split(',')[0]), int(current_pos.split(',')[1])], [rand_x, rand_y])
                if dist >= min_distance:
                    return target

    ghost_cell = f"{ghost.pos_x},{ghost.pos_y}"
    player_cell = f"{player.pos_x},{player.pos_y}"
    
    safe_places = [] if safe_places is None else safe_places
    is_player_safe = (player.pos_x, player.pos_y) in safe_places

    # Compute shortest path distance using Dijkstra's
    path = graph.dijkstra_path(ghost_cell, player_cell)
    path_distance = len(path) - 1 if path else float('inf')  # Number of edges in path

    target = None
    if target_dict is not None and ghost_index is not None:
        target = target_dict[ghost_index]
    
    if is_player_safe or path_distance > 5:  #
        # Roam to a random target using BFS
        if not target or ghost_cell == target:
            target = get_random_place(size, ghost_cell)
            if target_dict is not None and ghost_index is not None:
                target_dict[ghost_index] = target
        path = graph.bfs_path(ghost_cell, target)
    else:
        # Chase player using Dijkstra's path (already computed)
        if target_dict is not None and ghost_index is not None:
            target_dict[ghost_index] = player_cell

    if path and len(path) > 1:
        gx, gy = map(int, path[1].split(','))
        ghost.pos_x, ghost.pos_y = gx, gy

def get_random_safe_places(size, count=20):
    fixed = set()
    fixed.add((0, 0))
    fixed.add((0, size-1))
    fixed.add((size-1, 0))
    fixed.add((size-1, size-1))
    if size > 2:
        fixed.add((size//2, size//2))
        fixed.add((0, size//2))
        fixed.add((size-1, size//2))
        fixed.add((size//2, 0))
        fixed.add((size//2, size-1))
        fixed.add((size//4, size//4))
        fixed.add((size//4, 3*size//4))
        fixed.add((3*size//4, size//4))
        fixed.add((3*size//4, 3*size//4))
        fixed.add((1, 1))
        fixed.add((size-2, size-2))
        fixed.add((size//3, size//3))
        fixed.add((size//3, 2*size//3))
        fixed.add((2*size//3, size//3))
        fixed.add((2*size//3, 2*size//3))
    safe_places = set(fixed)
    while len(safe_places) < len(fixed) + count:
        y = random.randint(0, size-1)
        x = random.randint(0, size-1)
        safe_places.add((y, x))
    return list(safe_places)