# system.py
import sys
import pygame
import random
from logic.mazegenerator import maze_generator
from graphic.core import init_window
from graphic.draw import draw_maze, draw_player, draw_ghost, draw_exit, draw_safe_places, draw_maze_animation, main_menu
from graphic.entity import Player, Ghost
from graphic.init import game_loop
from graphic.logicInGame import get_random_safe_places

def start_game(ALGORITHM='kruskal', MAZE_SIZE=30):
    CELL_SIZE = 30
    WINDOW_MARGIN = 20
    win_size = MAZE_SIZE * CELL_SIZE
    screen = init_window(win_size, win_size, f"Maze Game - {ALGORITHM}")
    menu_choice = main_menu(screen, win_size, win_size)
    if menu_choice != "start":
        pygame.quit()
        sys.exit()
    graph = maze_generator(MAZE_SIZE, ALGORITHM)
    print(f"Graph has {len(graph.vertices_list)} vertices, {len(graph.get_all_edges())} edges, {len(graph.deleted_edges)} deleted edges")
    build_steps = getattr(graph, 'build_steps', [])
    safe_places = get_random_safe_places(MAZE_SIZE, count=10)
    if build_steps:
        draw_maze_animation(screen, graph, MAZE_SIZE, CELL_SIZE, build_steps)
    game_loop(screen, graph, MAZE_SIZE, CELL_SIZE, safe_places=safe_places)