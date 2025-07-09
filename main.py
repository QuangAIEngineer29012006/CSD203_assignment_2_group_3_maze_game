import sys
import pygame
import random
from logic.mazegenerator import maze_generator
from graphic.core import init_window
from graphic.draw import draw_maze, draw_player, draw_ghost, draw_exit, draw_safe_places,  draw_maze_animation
from graphic.entity import Player, Ghost
from graphic.init import game_loop
from graphic.logicInGame import get_random_safe_places

# Config
MAZE_SIZE = 20  # Default size
ALGORITHM = 'wilson'  # Default algorithm
CELL_SIZE = 40
WINDOW_MARGIN = 20

# Allow user to specify size and algorithm via command line
if len(sys.argv) > 1:
    try:
        MAZE_SIZE = int(sys.argv[1])
    except ValueError:
        print("Invalid size argument, using default.")
if len(sys.argv) > 2:
    ALGORITHM = sys.argv[2]

# Generate maze
graph = maze_generator(MAZE_SIZE, ALGORITHM)

# Get build steps for animation (if available)
build_steps = getattr(graph, 'build_steps', None)

# Init window
win_size = MAZE_SIZE * CELL_SIZE
screen = init_window(win_size, win_size, f"Maze Game - {ALGORITHM}")

# Generate safe places
safe_places = get_random_safe_places(MAZE_SIZE, count=10)

# Draw maze animation if build_steps exist
if build_steps:
    draw_maze_animation(screen, graph, MAZE_SIZE, CELL_SIZE, build_steps)

# Start the main game loop (handles player, ghost, win/lose)
game_loop(screen, graph, MAZE_SIZE, CELL_SIZE, safe_places=safe_places)
