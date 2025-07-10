import pygame
from graphic.entity import Player, Ghost
from graphic.draw import draw_maze, draw_player, draw_ghost, draw_exit
from graphic.logicInGame import handle_player_input, update_ghost

def game_loop(screen, graph, size, cell_size, safe_places=None):
    running = True
    player = Player(0, 0)
    # Add ghosts at each corner
    ghost1 = Ghost(size - 1, 0)
    ghost2 = Ghost(0, size - 1)
    ghost3 = Ghost(size - 1, size - 1)
    ghost4 = Ghost(int(size/2), int(size/2))  
    ghosts = [ghost1, ghost2, ghost3, ghost4]
    # Each ghost gets its own target
    ghost_targets = [None for _ in ghosts]
    exit_pos = [size - 1, size - 1]
    clock = pygame.time.Clock()
    ghost_timer = 0
    ghost_delay = 5  # Number of frames to wait between ghost moves (increase for slower ghost)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_player_input(player, graph, size,event)
        # Only update ghosts every ghost_delay frames
        if ghost_timer == 0:
            for i, ghost in enumerate(ghosts):
                update_ghost(ghost, player, graph, size, safe_places=safe_places, target_dict=ghost_targets, ghost_index=i)
        ghost_timer = (ghost_timer + 1) % ghost_delay
        screen.fill((255, 255, 255))
        draw_maze(screen, graph, size, cell_size, safe_places=safe_places)
        draw_exit(screen, exit_pos[1], exit_pos[0], cell_size)
        draw_player(screen, player.pos_y, player.pos_x, cell_size)
        for ghost in ghosts:
            draw_ghost(screen, ghost.pos_y, ghost.pos_x, cell_size)
        pygame.display.flip()
        # Win condition
        if [player.pos_x, player.pos_y] == exit_pos:
            pygame.display.set_caption("You Win!")
            pygame.time.delay(1000)
            running = False
        # Lose condition (ignore if player is in safe place)
        for ghost in ghosts:
            if [ghost.pos_x, ghost.pos_y] == [player.pos_x, player.pos_y]:
                if safe_places and (player.pos_x, player.pos_y) in safe_places:
                    pass  # Player is safe, do not lose
                else:
                    pygame.display.set_caption("You Lose!")
                    pygame.time.delay(1000)
                    running = False
        clock.tick(10)
    pygame.quit()