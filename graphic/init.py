import pygame
from graphic.entity import Player, Ghost
from graphic.draw import draw_maze, draw_player, draw_ghost, draw_exit, draw_text # Import draw_text
from graphic.logicInGame import handle_player_input, update_ghost

ghost_speed = 20  # Number of frames to wait between ghost moves (increase for slower ghost)
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
    ghost_delay = ghost_speed  # Number of frames to wait between ghost moves (increase for slower ghost)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_player_input(player, graph, size, event)

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
            screen_width, screen_height = screen.get_size() # Get current screen size
            screen.fill((0, 200, 0)) # Fill screen with green background for win
            draw_text(screen, "YOU WIN!", 100, screen_width // 2, screen_height // 2, color=(255, 255, 255)) # White text
            pygame.display.flip() # Update the display to show the win message
            pygame.time.delay(3000) # Keep the message on screen for 3 seconds
            running = False

        # Lose condition (ignore if player is in safe place)
        for ghost in ghosts:
            if [ghost.pos_x, ghost.pos_y] == [player.pos_x, player.pos_y]:
                if safe_places and ([player.pos_x, player.pos_y] in [[s[0], s[1]] for s in safe_places]):
                    pygame.display.set_caption("You are SAFE!")
                else:
                    screen_width, screen_height = screen.get_size()
                    screen.fill((200, 0, 0)) # Fill screen with red background for game over
                    draw_text(screen, "GAME OVER!", 100, screen_width // 2, screen_height // 2, color=(255, 255, 255))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    running = False
        clock.tick(60) # Limit frame rate to 60 FPS
    pygame.quit()