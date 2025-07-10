import pygame

def init_window(width, height, title="Maze Game"):
    pygame.init()
    pygame.display.set_caption(title) # Set caption BEFORE set_mode
    screen = pygame.display.set_mode((width, height))
    return screen
