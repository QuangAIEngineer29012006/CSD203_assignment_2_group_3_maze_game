import pygame
from graphic.entity import Player, Ghost
from graphic.draw import draw_maze, draw_player, draw_ghost, draw_exit
import random
from logic.graph import Graph


# Handles player input and updates player position
def handle_player_input(player, graph, size, event): # Added 'event' parameter
    next_x, next_y = player.pos_x, player.pos_y

    if event.type == pygame.KEYDOWN: # Only process on key down event
        if event.key == pygame.K_UP and player.pos_x > 0:
            next_x -= 1
        elif event.key == pygame.K_DOWN and player.pos_x < size - 1:
            next_x += 1
        elif event.key == pygame.K_LEFT and player.pos_y > 0:
            next_y -= 1
        elif event.key == pygame.K_RIGHT and player.pos_y < size - 1:
            next_y += 1
        else: # If it's not a directional key, no movement
            return

    cell_cur = f"{player.pos_x},{player.pos_y}"
    cell_next = f"{next_x},{next_y}"

    # Only move if the target cell is different and a valid neighbor
    if (next_x, next_y) != (player.pos_x, player.pos_y) and \
        cell_next in graph.vertices_list and \
        graph.is_neighbour(cell_cur, cell_next):
        player.pos_x, player.pos_y = next_x, next_y


#distance to calculate manhattan distance between two points


# Handles ghost movement logic
def update_ghost(ghost, player, graph, size, safe_places=None, target_dict=None, ghost_index=None):
    def get_random_place(size):
        rand_x = random.randint(0, size-1)
        rand_y = random.randint(0, size-1)
        return f'{rand_x},{rand_y}'
    ghost_cell = f"{ghost.pos_x},{ghost.pos_y}"
    player_cell = f"{player.pos_x},{player.pos_y}"
    dist = graph.manhattan([ghost.pos_x, ghost.pos_y], [player.pos_x, player.pos_y])

    # If player is in a safe place, always go random
    if safe_places and (player.pos_x, player.pos_y) in safe_places:
        if target_dict is not None and ghost_index is not None:
            target = target_dict[ghost_index]
            if not target or ghost_cell == target:
                target = get_random_place(size)
                while target == ghost_cell:
                    target = get_random_place(size)
                target_dict[ghost_index] = target
        else:
            target = get_random_place(size)
            while target == ghost_cell:
                target = get_random_place(size)
        path = graph.dfs_path(ghost_cell, target)
        if len(path) > 1:
            gx, gy = map(int, path[1].split(','))
            ghost.pos_x, ghost.pos_y = gx, gy
        return

    # If far from player, go random (commit to a target)
    if dist > 3:
        if target_dict is not None and ghost_index is not None:
            target = target_dict[ghost_index]
            if not target or ghost_cell == target:
                target = get_random_place(size)
                while target == ghost_cell:
                    target = get_random_place(size)
                target_dict[ghost_index] = target
        else:
            target = get_random_place(size)
            while target == ghost_cell:
                target = get_random_place(size)
        path = graph.bfs_path( ghost_cell, target)
        if len(path) > 1:
            gx, gy = map(int, path[1].split(','))
            ghost.pos_x, ghost.pos_y = gx, gy
    else:
        # Chase player
        if target_dict is not None and ghost_index is not None:
            target_dict[ghost_index] = None  # Reset target when chasing
        path = graph.bfs_path( ghost_cell, player_cell)
        if len(path) > 1:
            gx, gy = map(int, path[1].split(','))
            ghost.pos_x, ghost.pos_y = gx, gy

def get_random_safe_places(size, count=20):
    fixed = set()
    fixed.add((0, 0))
    fixed.add((0, size-1))
    fixed.add((size-1, 0))
    fixed.add((size-1, size-1))
    if size > 2:
        fixed.add((size//2, size//2))  # Center
        fixed.add((0, size//2))        # Top edge middle
        fixed.add((size-1, size//2))   # Bottom edge middle
        fixed.add((size//2, 0))        # Left edge middle
        fixed.add((size//2, size-1))   # Right edge middle
        # Four quarter-centers
        fixed.add((size//4, size//4))
        fixed.add((size//4, 3*size//4))
        fixed.add((3*size//4, size//4))
        fixed.add((3*size//4, 3*size//4))
        # Two more near corners (just inside the corners)
        fixed.add((1, 1))
        fixed.add((size-2, size-2))
        # 1/3 and 2/3 positions
        fixed.add((size//3, size//3))
        fixed.add((size//3, 2*size//3))
        fixed.add((2*size//3, size//3))
        fixed.add((2*size//3, 2*size//3))
    # Add more random safe places, avoiding duplicates
    safe_places = set(fixed)
    while len(safe_places) < len(fixed) + count:
        y = random.randint(0, size-1)
        x = random.randint(0, size-1)
        safe_places.add((y, x))
    return list(safe_places)


            


