if __name__ == "__main__":
    from graphic.core import init_window
    from logic.mazegenerator import maze_generator
    from graphic.logicInGame import game_loop
    size = 20
    cell_size = 40
    screen = init_window(size * cell_size, size * cell_size, title="Maze Game")
    g1 = maze_generator()
    graph = g1.maze_generator_prim(size)
    from graphic.draw import draw_maze_animation
    draw_maze_animation(screen, graph, size, cell_size, graph.build_steps)
    game_loop(screen, graph, size, cell_size)
