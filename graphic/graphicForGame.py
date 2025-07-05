
import pygame
def draw_maze(graph, size, cell_size=40):
    pygame.init()
    width = height = size * cell_size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze")

    white = (204, 255, 2)
    black = (0, 0, 0)

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

    # Draw outer border
    pygame.draw.line(screen, black, (0, 0), (width, 0), 5)
    pygame.draw.line(screen, black, (0, 0), (0, height), 5)

    pygame.display.flip()

    # Basic event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()







    








            




        



