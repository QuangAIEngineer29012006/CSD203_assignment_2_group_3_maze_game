import pygame
from graphic.entity import Player, Ghost
from graphic.draw import draw_maze, draw_player, draw_ghost, draw_exit
from graphic.logicInGame import handle_player_input, update_ghost

def game_loop(screen, graph, size, cell_size):
    running = True
    player = Player(0, 0)
    ghost = Ghost(size - 1, 0)
    exit_pos = [size - 1, size - 1]
    clock = pygame.time.Clock()
    ghost_timer = 0
    ghost_delay = 5  # Number of frames to wait between ghost moves (increase for slower ghost)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        handle_player_input(player, graph, size)
        # Only update ghost every ghost_delay frames
        if ghost_timer == 0:
            update_ghost(ghost, player, graph, size)
        ghost_timer = (ghost_timer + 1) % ghost_delay
        screen.fill((255, 255, 255))
        draw_maze(screen, graph, size, cell_size)
        draw_exit(screen, exit_pos[1], exit_pos[0], cell_size)
        draw_player(screen, player.pos_y, player.pos_x, cell_size)
        draw_ghost(screen, ghost.pos_y, ghost.pos_x, cell_size)
        pygame.display.flip()
        # Win condition
        if [player.pos_x, player.pos_y] == exit_pos:
            pygame.display.set_caption("You Win!")
            pygame.time.delay(1000)
            running = False
        # Lose condition
        if [ghost.pos_x, ghost.pos_y] == [player.pos_x, player.pos_y]:
            pygame.display.set_caption("You Lose!")
            pygame.time.delay(1000)
            running = False
        clock.tick(10)
    pygame.quit()