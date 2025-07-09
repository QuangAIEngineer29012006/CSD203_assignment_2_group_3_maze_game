import pygame
import time

def draw_maze_animation(graph, size, cell_size=40, delay=0.05):
    pygame.init()
    width = height = size * cell_size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Generation Animation")

    white = (204, 255, 2)
    black = (0, 0, 0)

    # Draw background and all walls
    screen.fill(white)
    for row in range(size):
        for col in range(size):
            x = col * cell_size
            y = row * cell_size
            # Draw right wall
            pygame.draw.line(screen, black, (x + cell_size, y), (x + cell_size, y + cell_size), 4)
            # Draw bottom wall
            pygame.draw.line(screen, black, (x, y + cell_size), (x + cell_size, y + cell_size), 4)
    # Draw outer border
    pygame.draw.line(screen, black, (0, 0), (width, 0), 5)
    pygame.draw.line(screen, black, (0, 0), (0, height), 5)

    pygame.display.flip()
    time.sleep(0.5)

    # Remove walls step by step based on build_steps
    for (cell1, cell2) in getattr(graph, 'build_steps', []):
        row1, col1 = map(int, cell1.split(','))
        row2, col2 = map(int, cell2.split(','))
        x1, y1 = col1 * cell_size, row1 * cell_size
        x2, y2 = col2 * cell_size, row2 * cell_size

        # Determine which wall to remove
        if row1 == row2:  # Same row, horizontal neighbors
            if col1 < col2:  # cell2 is to the right
                # Erase right wall of cell1
                pygame.draw.line(screen, white, (x1 + cell_size, y1), (x1 + cell_size, y1 + cell_size), 4)
            else:  # cell2 is to the left
                pygame.draw.line(screen, white, (x2 + cell_size, y2), (x2 + cell_size, y2 + cell_size), 4)
        elif col1 == col2:  # Same column, vertical neighbors
            if row1 < row2:  # cell2 is below
                # Erase bottom wall of cell1
                pygame.draw.line(screen, white, (x1, y1 + cell_size), (x1 + cell_size, y1 + cell_size), 4)
            else:  # cell2 is above
                pygame.draw.line(screen, white, (x2, y2 + cell_size), (x2 + cell_size, y2 + cell_size), 4)
        pygame.display.update()
        time.sleep(delay)

    # After animation, start the player control loop
    control_player_in_maze(graph, size, cell_size, screen, white, black)

def draw_maze(graph, size, cell_size=40, screen=None, white=(204, 255, 2), black=(0, 0, 0)):
    # If screen not passed, create one (for standalone use)
    if screen is None:
        pygame.init()
        width = height = size * cell_size
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Maze")
        clear_screen = True
    else:
        clear_screen = False

    if clear_screen:
        screen.fill(white)
    for row in range(size):
        for col in range(size):
            x = col * cell_size
            y = row * cell_size
            cell = f"{row},{col}"

            # Draw right wall
            right = f"{row},{col+1}"
            if col == size - 1 or not graph.vertices_list[cell].is_neighbor(graph.vertices_list.get(right, None)):
                pygame.draw.line(screen, black, (x + cell_size, y), (x + cell_size, y + cell_size), 4)

            # Draw bottom wall
            down = f"{row+1},{col}"
            if row == size - 1 or not graph.vertices_list[cell].is_neighbor(graph.vertices_list.get(down, None)):
                pygame.draw.line(screen, black, (x, y + cell_size), (x + cell_size, y + cell_size), 4)

    pygame.draw.line(screen, black, (0, 0), (size * cell_size, 0), 5)
    pygame.draw.line(screen, black, (0, 0), (0, size * cell_size), 5)

    if clear_screen:
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()

def control_player_in_maze(graph, size, cell_size, screen, white, black):
    player_pos = [0, 0]  # Start at top-left cell
    exit_pos = [size - 1, size - 1]  # Exit at bottom-right cell
    player_color = (255, 0, 0)  # Red
    exit_color = (0, 0, 255)    # Blue

    def draw_everything():
        screen.fill(white)
        draw_maze(graph, size, cell_size, screen=screen, white=white, black=black)
        # Draw exit
        x_exit = exit_pos[1] * cell_size + cell_size // 2
        y_exit = exit_pos[0] * cell_size + cell_size // 2
        pygame.draw.circle(screen, exit_color, (x_exit, y_exit), cell_size // 4)
        # Draw player
        x = player_pos[1] * cell_size + cell_size // 2
        y = player_pos[0] * cell_size + cell_size // 2
        pygame.draw.circle(screen, player_color, (x, y), cell_size // 4)
        pygame.display.update()

    draw_everything()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                next_pos = player_pos[:]
                if event.key == pygame.K_UP and player_pos[0] > 0:
                    next_pos[0] -= 1
                elif event.key == pygame.K_DOWN and player_pos[0] < size - 1:
                    next_pos[0] += 1
                elif event.key == pygame.K_LEFT and player_pos[1] > 0:
                    next_pos[1] -= 1
                elif event.key == pygame.K_RIGHT and player_pos[1] < size - 1:
                    next_pos[1] += 1
                # Check if move is allowed (cells are neighbors in maze graph)
                cell_cur = f"{player_pos[0]},{player_pos[1]}"
                cell_next = f"{next_pos[0]},{next_pos[1]}"
                if cell_next in graph.vertices_list and graph.vertices_list[cell_cur].is_neighbor(graph.vertices_list[cell_next]):
                    player_pos = next_pos
                    draw_everything()
                # Win condition
                if player_pos == exit_pos:
                    pygame.display.set_caption("You Win!")
        pygame.time.delay(30)
    pygame.quit()