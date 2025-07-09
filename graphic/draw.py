import pygame
import random
from logic.graph import Graph
from logic.mazegenerator import maze_generator
from graphic.core import init_window
from graphic.entity import Player
from graphic.entity import Ghost

def draw_grid(screen, size, cell_size, color=(200, 200, 200)):
    for row in range(size):
        for col in range(size):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size), 1)
    

def draw_maze(screen, graph, size, cell_size, wall_color=(0, 0, 0), bg_color=(255, 255, 255), safe_places=None):
    screen.fill(bg_color)
    if safe_places is None:
        safe_places = []
    draw_safe_places(screen, safe_places, cell_size)
    for row in range(size):
        for col in range(size):
            current = f"{row},{col}"
            x = col * cell_size
            y = row * cell_size

            neighbors = graph.vertices_list.get(current, {})

            # Top wall
            if f"{row-1},{col}" not in neighbors:
                pygame.draw.line(screen, wall_color, (x, y), (x + cell_size, y), 2)
            # Left wall
            if f"{row},{col-1}" not in neighbors:
                pygame.draw.line(screen, wall_color, (x, y), (x, y + cell_size), 2)
            # Bottom wall
            if f"{row+1},{col}" not in neighbors:
                pygame.draw.line(screen, wall_color, (x, y + cell_size), (x + cell_size, y + cell_size), 2)
            # Right wall
            if f"{row},{col+1}" not in neighbors:
                pygame.draw.line(screen, wall_color, (x + cell_size, y), (x + cell_size, y + cell_size), 2)

# Draw the player at a given position

def draw_player(screen, x, y, cell_size, color=(255,0,0)):
    px = x * cell_size + cell_size // 2
    py = y * cell_size + cell_size // 2
    pygame.draw.circle(screen, color, (px, py), cell_size // 4)

# Draw the ghost at a given position
def draw_ghost(screen, x, y, cell_size, color=(0,255,255)):
    gx = x * cell_size + cell_size // 2
    gy = y * cell_size + cell_size // 2
    pygame.draw.circle(screen, color, (gx, gy), cell_size // 4)

# Draw the exit
def draw_exit(screen, x, y, cell_size, color=(0,0,255)):
    ex = x * cell_size + cell_size // 2
    ey = y * cell_size + cell_size // 2
    pygame.draw.circle(screen, color, (ex, ey), cell_size // 4)

def draw_safe_places(screen, safe_places, cell_size, color=(0, 255, 0)):
    for y, x in safe_places:
        pygame.draw.rect(screen, color, (x * cell_size + 2, y * cell_size + 2, cell_size - 4, cell_size - 4))

def get_random_safe_places(size, count=5):
    safe_places = set()
    while len(safe_places) < count:
        y = random.randint(0, size-1)
        x = random.randint(0, size-1)
        safe_places.add((y, x))
    return list(safe_places)

def draw_maze_animation(screen, graph, size, cell_size, build_steps, wall_color=(0,0,0), bg_color=(255,255,255), delay=0.05):
    import time
    screen.fill(bg_color)
    draw_grid(screen, size, cell_size, color=wall_color)
    pygame.display.flip()
    time.sleep(0.5)
    highlight_color = (255, 0, 0)  # Red
    visited = set()
    for (cell1, cell2) in build_steps:
        if cell1 in visited and cell2 not in visited:
            from_cell, to_cell = cell1, cell2
        elif cell2 in visited and cell1 not in visited:
            from_cell, to_cell = cell2, cell1
        else:
            from_cell, to_cell = cell1, cell2
        visited.add(to_cell)
        row_from, col_from = map(int, from_cell.split(','))
        row_to, col_to = map(int, to_cell.split(','))
        x_from, y_from = col_from * cell_size, row_from * cell_size
        x_to, y_to = col_to * cell_size, row_to * cell_size
        # Highlight only the from_cell
        pygame.draw.rect(screen, highlight_color, (x_from+2, y_from+2, cell_size-4, cell_size-4))
        pygame.display.update()
        time.sleep(delay/2)
        # Carve the wall between them
        if row_from == row_to:  # Same row, horizontal neighbors
            if col_from < col_to:
                pygame.draw.line(screen, bg_color, (x_from + cell_size, y_from), (x_from + cell_size, y_from + cell_size), 4)
            else:
                pygame.draw.line(screen, bg_color, (x_from, y_from), (x_from, y_from + cell_size), 4)
        elif col_from == col_to:  # Same column, vertical neighbors
            if row_from < row_to:
                pygame.draw.line(screen, bg_color, (x_from, y_from + cell_size), (x_from + cell_size, y_from + cell_size), 4)
            else:
                pygame.draw.line(screen, bg_color, (x_from, y_from), (x_from + cell_size, y_from), 4)
        pygame.display.update()
        time.sleep(delay/2)
        # Remove highlight only from from_cell
        pygame.draw.rect(screen, bg_color, (x_from+2, y_from+2, cell_size-4, cell_size-4))
        pygame.display.update()



